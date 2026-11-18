# KickTipp · Häuser Buli Cup

Online: https://salahlfc-kicktipp.streamlit.app/

Die App öffnet direkt KickTipp. KickTipp-Seiten: Hauptseite, Deep Dive und Info. Papiermodus samt Schein und Tagebuch, Startportal, SportBet, Betting-Analyse und Mitfiebern sind entfernt, einschließlich ihrer Module, des SportBet-Scheins und der Forschungsberichte im ausgelieferten Anwendungspaket. Alte Navigations- und Widget-Zustände werden beim Öffnen verworfen.

## Hauptseite und Deep Dive

Bundesliga-Spieltagstipps nach der4/2/1-Punkteregel, Expected Points, Chance-Ampel, Teamlogos und Spieltag-Auswertung. Bereits gespeicherte Vorabtipps bleiben nach Anpfiff sichtbar. Öffentliche Spielstände werden etwa minütlich aus OpenLigaDB abgefragt, solange die Seite geöffnet ist. Die Quelle kann verzögert melden. Unbekannt wird niemals als0:0 gewertet; nur bestätigte Endergebnisse werden bewertet.

Im Deep Dive stehen die Auswertungen des gesamten Spieltags und der einzelnen Spiele. Die Info-Seite erläutert Modell, Gewichtung, Datenquellen und Grenzen; dort bleibt die Darstellung System/Dunkel/Hell auswählbar. Vorabtipps, Bundesliga-Daten, Modellkonfiguration und bestehende KickTipp-Rückblicke werden durch die Bereinigung nicht verändert.

## Cloudbetrieb

Streamlit-Einstieg:app.py, Python3.11, feste Paketversionen in requirements.txt. Das geprüfte Anwendungspaket liegt in kicktipp.zip. Der Einstieg entpackt es und übernimmt bestehende KickTipp-Archive auf demselben Server bei normalen Code-Updates. Das Cloud-Dateisystem ist bei einem Serveraustausch nicht dauerhaft garantiert. Keine Mac-Anbindung und keine neuen Kontorechte.

## Automatischer Teamcheck

Optionaler API-Football Gratisplan über Streamlit Secrets (`API_FOOTBALL_KEY`). Abruf von Bundesliga-Prognosen und Ausfallmeldungen; Startelfen werden im Zeitfenster vor Anpfiff geprüft. Eindeutig zugeordnete 1X2-Providerprognosen fließen mit vorläufig 10 % ein; die App optimiert danach erneut nach 4/2/1. Das ist ein konservativer, noch nicht separat historisch kalibrierter Zusatz und keine Garantie. Bei fehlendem Schlüssel, API-Fehlern oder uneindeutigen Spielen bleibt das Ergebnismodell unverändert. API-Football begrenzt den Gratisplan auf 100 Anfragen täglich.

