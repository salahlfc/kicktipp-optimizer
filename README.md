# Matchday · KickTipp & SportBet

Online: https://salahlfc-kicktipp.streamlit.app/

Streamlit-Einstieg: app.py · Python 3.11 · feste Paketversionen in requirements.txt.
Das geprüfte Anwendungspaket liegt in kicktipp.zip. Der Einstieg entpackt es und erhält bestehende Archive auf demselben Server bei normalen Code-Updates. Kein externer Prozess, keine Mac-Anbindung, keine neuen Kontorechte.

## Live und Rückblick
Alle gültigen Vorabtipps eines Spieltags bleiben sichtbar. Angezeigte Zwischenstände werden etwa minütlich aus OpenLigaDB abgefragt, solange die Seite geöffnet ist; die Quelle kann verzögert melden. Unbekannt wird niemals als 0:0 gewertet. Nur bestätigte Endergebnisse werden bewertet und für späteres Training verwendet.
Nach Abpfiff: Vergleich von Tipp, Ergebnis, Punkten und Torverteilung, gegebenenfalls Halbzeitstand. Gesamtbewertung erst nach Abschluss aller Partien, zuvor Zwischenbilanz. Rückblicke benennen Prüfpunkte; sie erfinden keine Verletzungs-, Aufstellungs- oder Spielverlaufsursachen und ändern keine Modellgewichte.

## Speichergrenze der Testversion
Bestehende Dateien werden bei normalen Updates auf derselben Maschine übernommen. Das Cloud-Dateisystem ist bei Austausch oder Neustart der Maschine nicht dauerhaft garantiert. Eine externe dauerhafte Speicherung bleibt erforderlich. Keine Verlustfreiheit versprechen.

## Startseite und SportBet
Die neue Startseite führt zu KickTipp und SportBet. Der vorhandene Bundesliga-Optimierer bleibt erhalten. SportBet verfolgt nur den vom Nutzer gelieferten 13er-Schein vom 08.11.2026. Die Zuordnung zu ESPN erfolgt über feste Ereignis-IDs, Datum und beide Team-IDs. Öffentliche Spielstände werden etwa minütlich bei geöffneter Seite abgerufen; Detailstatistiken nur für die ausgewählte Partie, höchstens alle zwei Minuten. Unbekannte Daten werden nicht als 0:0 oder Gewinn gewertet. Live erfüllte Schwellen sind keine bestätigten Gewinne. Es gibt keine Wettabgabe, Cashout-Funktion, Prognose neuer Wetten oder Berechnung von Gewinnwahrscheinlichkeiten. Buchmacherabrechnung und abweichende Verlängerungsregeln bleiben maßgeblich.

## SportBet: mobile Liste und Fünf-Minuten-Plan
Einzelne Spiele stehen als kompakte Karten untereinander. Spielstand, Uhr, Ist, Soll, Delta und noch fehlende Punkte bis zum Endziel stehen direkt auf der Karte. Bei Under steht stattdessen der verbleibende Puffer. Die Liste sortiert NFL-Punktewetten nach dem ungünstigsten Delta zuerst. Erläuterungen, Scheindaten und optionale Detailstatistiken stehen eingeklappt unten.

NFL-Soll wird am zuletzt vollständig gespielten Fünf-Minuten-Abschnitt berechnet: Endziel × (5 × floor(gespielte Minuten / 5)) / 60. Es gibt zwölf Abschnitte; 40 benötigte Punkte ergeben 3,333 Punkte je Abschnitt, nach zehn Spielminuten 6,667. Die Daten werden weiterhin etwa minütlich abgefragt. Delta ist bei Over Ist minus Soll und bei Under Soll minus Ist. Grün ab null, Gelb bis einschließlich -7, darunter Rot. Fußball behält seine Tor-/Zeit-Ampel; seine Tor-Planwerte beziehen sich auf 90 reguläre Minuten. Siegerwetten zeigen Führung gegenüber der nötigen positiven Differenz. Keine berechneten Gewinnwahrscheinlichkeiten.
