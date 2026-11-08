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

## SportBet: Viertelplan und Delta
NFL-Punktewetten werden nach einem kumulierten Viertelplan bewertet: 25/50/75/100 Prozent des nötigen Over-Endziels beziehungsweise des erlaubten Under-Maximums. Innerhalb des Viertels zählt die Spielzeit anteilig. Beispiel: Over 39,5 erfordert 40 Punkte; Soll zur Halbzeit 20. Ist 9 ergibt Delta -11 und Rot. Over: Delta = Ist minus Soll. Under: Delta = Soll minus Ist. Grün ab null, Gelb bis einschließlich -7 Punkte, darunter Rot. Eine bereits überschrittene Under-Grenze bleibt Rot. Keine Uhrzeit seit Anpfiff als Ersatz für die gemeldete Spieluhr; ohne reguläre Uhr oder in einer Verlängerung bleibt die Einschätzung vorsichtig.

Die Übersicht zeigt Ist, Soll und Delta sowie das noch nötige Ergebnis bis zum Endziel. NFL-Punktewetten stehen zuerst nach dem größten ungünstigen Delta, andere Marktarten folgen danach. Siegerwetten werden nicht mit einer Gesamtpunkte-Wette verwechselt. Fußball behält seine Tor-/Zeitregeln. Die Ampeln sind transparente Regeln und keine kalibrierten Gewinnwahrscheinlichkeiten.
