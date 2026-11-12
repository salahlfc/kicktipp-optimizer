# KickTipp · Häuser Buli Cup

Online: https://salahlfc-kicktipp.streamlit.app/

Die App öffnet direkt KickTipp. KickTipp-Seiten: Hauptseite, Deep Dive und Info. Zusätzlich gibt es den Papiermodus für einen bereits vorhandenen fiktiven Schein. Startportal, SportBet, Betting-Analyse und Mitfiebern sind entfernt, einschließlich ihrer Module, des SportBet-Scheins und der Forschungsberichte im ausgelieferten Anwendungspaket. Alte Navigations- und Widget-Zustände werden beim Öffnen verworfen.

## Hauptseite und Deep Dive

Bundesliga-Spieltagstipps nach der4/2/1-Punkteregel, Expected Points, Chance-Ampel, Teamlogos und Spieltag-Auswertung. Bereits gespeicherte Vorabtipps bleiben nach Anpfiff sichtbar. Öffentliche Spielstände werden etwa minütlich aus OpenLigaDB abgefragt, solange die Seite geöffnet ist. Die Quelle kann verzögert melden. Unbekannt wird niemals als0:0 gewertet; nur bestätigte Endergebnisse werden bewertet.

Im Deep Dive stehen die Auswertungen des gesamten Spieltags und der einzelnen Spiele. Die Info-Seite erläutert Modell, Gewichtung, Datenquellen und Grenzen; dort bleibt die Darstellung System/Dunkel/Hell auswählbar. Vorabtipps, Bundesliga-Daten, Modellkonfiguration und bestehende KickTipp-Rückblicke werden durch die Bereinigung nicht verändert.

## Cloudbetrieb

Streamlit-Einstieg:app.py, Python3.11, feste Paketversionen in requirements.txt. Das geprüfte Anwendungspaket liegt in kicktipp.zip. Der Einstieg entpackt es und übernimmt bestehende KickTipp-Archive auf demselben Server bei normalen Code-Updates. Das Cloud-Dateisystem ist bei einem Serveraustausch nicht dauerhaft garantiert. Keine Mac-Anbindung und keine neuen Kontorechte.


## Papiermodus: vorhandenen Schein fiktiv verfolgen

Der Reiter verfolgt die zehn bereits im vom Nutzer vorgelegten Chat festgelegten Auswahlen vom12.11.2026: acht Nations-League-Spiele, Seattle–Carolina und Philadelphia–Toronto. Keine neue Tippgenerierung oder Optimierung. Auswahl, Torgrenzen, Teamwahl und Annahmequoten sind unverändert festgeschrieben. Die zehn Ereignis-IDs, beide Team-IDs und Startzeiten wurden mit öffentlichen ESPN-Spielplänen abgeglichen. Tatsächliche Heim-/Auswärtsorientierung kommt aus dem Datenfeed. Kein Bwin-Zugang und keine Wettabgabe.

Fester Vergleich mit20Euro fiktivem Einsatz; im ursprünglichen Chat standen10Euro. Quoten sind unbestätigte Annahmen aus dem Chat, bei Philadelphia ausdrücklich eine Vergleichsmarktquote. Daraus wird kein verfügbarer Bwin-Preis behauptet. Papierauswertung: Fußball90Minuten inklusive Nachspielzeit, NBA/NHL-Sieger inklusive Verlängerung, NHL auch Shootout. Nur bestätigte Endergebnisse samt numerischem Score werden ausgewertet; zukünftige Endstände, veränderte Teilnehmer/Termine, Abbrüche, Verschiebungen oder unklare Spielzeitregeln bleiben unbestätigt.

Ein bestätigter falscher Tipp lässt den bestehenden Kombischein scheitern; hypothetischer Verlust20Euro. Gewinn erst nach zehn bestätigten Treffern; hypothetische Auszahlung aus den unveränderten Annahmequoten, ohne behauptete Steuern oder Anbieterabrechnung. Keine laufende Führung, vorzeitig erfüllte Torgrenze oder fehlende Daten als Treffer/Verlust behandeln. Fehlend ist nie0:0. Papierbilanz und hypothetisch vermiedener Verlust bleiben getrennt vom real nicht eingesetzten Geld und dem optionalen Zähler. Ein positiver Papierschein zählt nicht als vermiedener Verlust.

Automatische Ergebnisabfrage etwa minütlich bei geöffneter Seite; historische Ergebnisse werden beim erneuten Öffnen für denselben festen Spieltag abgefragt. Kein unbeaufsichtigter Zeitplan. Der nachträgliche Chat-Import ist kein nachgewiesener Vorab-Modelltest. Definition samt Fingerabdruck, Regeln und Quotenhinweis sind einsehbar.

Das bisherige Nichtwetten-Tagebuch bleibt optional eingeklappt, ausschließlich im lokalen Browser-Speicher, mit Rückgängig und JSON-Backup. Seine selbst markierten Tage werden nicht zur Papierbilanz addiert und nicht an den Server geschickt. Keine neue Kontoverbindung, keine neuen privaten Cloud-Finanzdaten und keine zusätzlichen Mac-Prozesse. KickTipp-Daten und Modelle unverändert.
