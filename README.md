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

## SportBet: Aufmerksamkeit und Live-Soll

Kompakte Karten untereinander: Ist, Soll, Delta und Fehlt zum Endziel, bei Under Puffer. Standard „Beobachten“ sortiert laufende Spiele Rot → Gelb → Grün. Innerhalb einer Farbe entscheidet der ungünstige Delta-Rückstand pro verbleibender Minute; NFL-Punkte werden auf sieben Punkte, Fußball auf ein Tor normiert. Danach zählt die kürzere Restzeit. Offene und unbekannte Spiele folgen, beendete Spiele stehen zuletzt.

Soll folgt der gemeldeten Spielzeit einschließlich NFL-Sekunden: Endziel × gespielte Zeit / reguläre Dauer. Datenaktualisierung etwa minütlich. Bei NFL ist Delta bei Over Ist minus Soll, bei Under Soll minus Ist. Grün ab null. Die gelbe Rückstandstoleranz von sieben Punkten sinkt in den letzten 30 Minuten proportional zur Restzeit bis mindestens 7/30 Punkte. Ein noch unerreichtes Over ist in den letzten zwei regulären Minuten Rot, ein erreichtes Over bleibt Grün. Ein Under mit günstigem Puffer wird bei weniger Restzeit nicht pauschal kritisch. Fußball und Siegerwetten behalten ihre zusätzlichen Restzeit-/Tor-/Führungsregeln. Ohne verlässliche Uhr keine erfundene Restzeit.

Oben stehen eine kurze Gesamtbewertung und der aktuelle Grün-Anteil der bewerteten Auswahlen. Das sind Beobachtungsregeln und keine berechneten Gewinnwahrscheinlichkeiten.
