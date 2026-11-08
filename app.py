"""Streamlit entry point for the bundled, reviewed Kicktipp test application."""
from pathlib import Path, PurePosixPath
import hashlib
import os
import json
import shutil
import runpy
import sys
import zipfile
import fcntl

RELEASE = '2026-11-08-betting-combos-v1'
BASE = Path(__file__).resolve().parent
ARCHIVE = BASE / 'kicktipp.zip'
BUILD = hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()[:20]
RUNTIME = BASE / '.kicktipp-runtime' / BUILD
RUNTIME.mkdir(parents=True, exist_ok=True)
with (RUNTIME / '.unpack.lock').open('a') as lock:
    fcntl.flock(lock, fcntl.LOCK_EX)
    if not (RUNTIME / '.ready').exists():
        with zipfile.ZipFile(ARCHIVE) as bundle:
            for entry in bundle.infolist():
                name = PurePosixPath(entry.filename)
                if name.is_absolute() or '..' in name.parts or '\\' in entry.filename:
                    raise ValueError('Ungültiger Paketpfad')
                if (entry.external_attr >> 16) & 0o170000 == 0o120000:
                    raise ValueError('Verknüpfungen sind im Paket nicht erlaubt')
            bundle.extractall(RUNTIME)
        (RUNTIME / '.ready').write_text(BUILD)
    fcntl.flock(lock, fcntl.LOCK_UN)
# Reuse existing on-server archives across ordinary code updates. This remains
# local cloud storage, not a promise of persistence after machine replacement.
STATE = BASE / '.kicktipp-state' / 'output'
STATE.mkdir(parents=True, exist_ok=True)
with (STATE.parent / '.migration.lock').open('a') as lock:
    fcntl.flock(lock, fcntl.LOCK_EX)
    marker = STATE.parent / ('migrated-' + BUILD)
    if not marker.exists():
        sources = sorted((BASE / '.kicktipp-runtime').glob('*/output'))
        for source in sources:
            for path in source.rglob('*'):
                if not path.is_file() or path.suffix not in {'.json','.csv'}:
                    continue
                dest = STATE / path.relative_to(source)
                dest.parent.mkdir(parents=True, exist_ok=True)
                copy = not dest.exists()
                if dest.exists() and path.name == 'lean_latest.json':
                    try:
                        copy = json.loads(path.read_text())['created_at'] > json.loads(dest.read_text())['created_at']
                    except (ValueError, KeyError):
                        copy = False
                if copy:
                    shutil.copy2(path, dest)
        marker.write_text(BUILD)
    fcntl.flock(lock, fcntl.LOCK_UN)
os.environ['KICKTIPP_OUTPUT_DIR'] = str(STATE)
# Streamlit may rerun this entry without restarting the Python process.
for name in ('leanflow','webcore','presentation','weekly_review','matchday_live','football_context','model_info','appearance','sportbet','sports_portal','betting_optimizer'):
    module = sys.modules.get(name)
    origin = getattr(module, '__file__', None)
    if origin and '.kicktipp-runtime' in Path(origin).parts and Path(origin).parent != RUNTIME:
        sys.modules.pop(name, None)
if str(RUNTIME) not in sys.path:
    sys.path.insert(0, str(RUNTIME))
runpy.run_path(str(RUNTIME / 'app.py'), run_name='__main__')
