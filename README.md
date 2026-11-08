# Kicktipp

Online: https://salahlfc-kicktipp.streamlit.app/

Streamlit-Einstieg: app.py · Python 3.11 · feste Paketversionen in requirements.txt.
Das geprüfte Anwendungspaket liegt in kicktipp.zip. Der Einstieg entpackt es und erhält bestehende Archive auf demselben Server bei normalen Code-Updates. Kein externer Prozess, keine Mac-Anbindung, keine neuen Kontorechte.

## Live und Rückblick
Alle gültigen Vorabtipps eines Spieltags bleiben sichtbar. Angezeigte Zwischenstände werden etwa minütlich aus OpenLigaDB abgefragt, solange die Seite geöffnet ist; die Quelle kann verzögert melden. Unbekannt wird niemals als 0:0 gewertet. Nur bestätigte Endergebnisse werden bewertet und für späteres Training verwendet.
Nach Abpfiff: Vergleich von Tipp, Ergebnis, Punkten und Torverteilung, gegebenenfalls Halbzeitstand. Gesamtbewertung erst nach Abschluss aller Partien, zuvor Zwischenbilanz. Rückblicke benennen Prüfpunkte; sie erfinden keine Verletzungs-, Aufstellungs- oder Spielverlaufsursachen und ändern keine Modellgewichte.

## Speichergrenze der Testversion
Bestehende Dateien werden bei normalen Updates auf derselben Maschine übernommen. Das Cloud-Dateisystem ist bei Austausch oder Neustart der Maschine nicht dauerhaft garantiert. Eine externe dauerhafte Speicherung bleibt erforderlich. Keine Verlustfreiheit versprechen.
