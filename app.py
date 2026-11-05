"""Streamlit entry point for the bundled, reviewed Kicktipp test application."""
from pathlib import Path, PurePosixPath
import hashlib
import os
import runpy
import sys
import zipfile
import fcntl

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
if str(RUNTIME) not in sys.path:
    sys.path.insert(0, str(RUNTIME))
runpy.run_path(str(RUNTIME / 'app.py'), run_name='__main__')
