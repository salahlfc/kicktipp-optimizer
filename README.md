# KickTipp · Häuser Buli Cup

Online: https://salahlfc-kicktipp.streamlit.app/

Die App öffnet direkt KickTipp. KickTipp-Seiten: Hauptseite, Deep Dive und Info. Papiermodus samt Schein und Tagebuch, Startportal, SportBet, Betting-Analyse und Mitfiebern sind entfernt, einschließlich ihrer Module, des SportBet-Scheins und der Forschungsberichte im ausgelieferten Anwendungspaket. Alte Navigations- und Widget-Zustände werden beim Öffnen verworfen.

## Hauptseite und Deep Dive

Bundesliga-Spieltagstipps nach der4/2/1-Punkteregel, Expected Points, Chance-Ampel, Teamlogos und Spieltag-Auswertung. Bereits gespeicherte Vorabtipps bleiben nach Anpfiff sichtbar. Öffentliche Spielstände werden etwa minütlich aus OpenLigaDB abgefragt, solange die Seite geöffnet ist. Die Quelle kann verzögert melden. Unbekannt wird niemals als0:0 gewertet; nur bestätigte Endergebnisse werden bewertet.

Im Deep Dive stehen die Auswertungen des gesamten Spieltags und der einzelnen Spiele. Die Info-Seite erläutert Modell, Gewichtung, Datenquellen und Grenzen; dort bleibt die Darstellung System/Dunkel/Hell auswählbar. Vorabtipps, Bundesliga-Daten, Modellkonfiguration und bestehende KickTipp-Rückblicke werden durch die Bereinigung nicht verändert.

## Cloudbetrieb

Streamlit-Einstieg:app.py, Python3.11, feste Paketversionen in requirements.txt. Das geprüfte Anwendungspaket liegt in kicktipp.zip. Der Einstieg entpackt es und übernimmt bestehende KickTipp-Archive auf demselben Server bei normalen Code-Updates. Das Cloud-Dateisystem ist bei einem Serveraustausch nicht dauerhaft garantiert. Keine Mac-Anbindung und keine neuen Kontorechte.

## Automatischer Teamcheck

Optionale Live Football API über Streamlit Secrets (`LIVE_FOOTBALL_API_KEY`). Der Bundesliga-Spielplan der Saison wird beim Optimieren einmal pro Tag geladen und bestätigt damit den API-Zugang. Beim Optimieren werden Verletzungen und Sperren für alle kommenden Spiele geprüft; der API-Abruf wird 24 Stunden zwischengespeichert und der Datenstand des letzten Optimierungslaufs im Deep Dive angezeigt. Die Zuordnung nutzt das eindeutige Heim-/Auswärtspaar aus dem Bundesliga-Spielplan und toleriert Zeitzonenunterschiede zwischen den Datenquellen. Erwartete oder bestätigte Startelfen mit Spielerbildern erscheinen, sobald der Anbieter sie ungefähr eine Stunde vor Anpfiff meldet; ein späterer Abruf kann die bestätigte Elf übernehmen. Verletzte mit belegten Einsätzen und Tor-/Assistdaten können die Team-Torerwartung vorsichtig um höchstens 0,14 senken. Dieser Zusatz ist noch nicht separat historisch kalibriert. Neue Konten erhalten laut Anbieter 500 Gratis-Credits, jeder Aufruf kostet einen Credit. Bei bekanntem Stand von null werden keine weiteren Abrufe gestartet; die App löst keine Käufe aus. Die Credits können für eine ganze Saison knapp sein. Bei fehlendem Schlüssel, Fehlern oder unklarer Zuordnung bleibt das Basismodell unverändert.

