# KickTipp · Häuser Buli Cup

Online: https://salahlfc-kicktipp.streamlit.app/

Die App öffnet direkt KickTipp. KickTipp-Seiten: Hauptseite, Deep Dive und Info. Zusätzlich gibt es den privaten Papiermodus. Startportal, SportBet, Betting-Analyse und Mitfiebern sind entfernt, einschließlich ihrer Module, des SportBet-Scheins und der Forschungsberichte im ausgelieferten Anwendungspaket. Alte Navigations- und Widget-Zustände werden beim Öffnen verworfen.

## Hauptseite und Deep Dive

Bundesliga-Spieltagstipps nach der4/2/1-Punkteregel, Expected Points, Chance-Ampel, Teamlogos und Spieltag-Auswertung. Bereits gespeicherte Vorabtipps bleiben nach Anpfiff sichtbar. Öffentliche Spielstände werden etwa minütlich aus OpenLigaDB abgefragt, solange die Seite geöffnet ist. Die Quelle kann verzögert melden. Unbekannt wird niemals als0:0 gewertet; nur bestätigte Endergebnisse werden bewertet.

Im Deep Dive stehen die Auswertungen des gesamten Spieltags und der einzelnen Spiele. Die Info-Seite erläutert Modell, Gewichtung, Datenquellen und Grenzen; dort bleibt die Darstellung System/Dunkel/Hell auswählbar. Vorabtipps, Bundesliga-Daten, Modellkonfiguration und bestehende KickTipp-Rückblicke werden durch die Bereinigung nicht verändert.

## Cloudbetrieb

Streamlit-Einstieg:app.py, Python3.11, feste Paketversionen in requirements.txt. Das geprüfte Anwendungspaket liegt in kicktipp.zip. Der Einstieg entpackt es und übernimmt bestehende KickTipp-Archive auf demselben Server bei normalen Code-Updates. Das Cloud-Dateisystem ist bei einem Serveraustausch nicht dauerhaft garantiert. Keine Mac-Anbindung und keine neuen Kontorechte.


## Papiermodus: Nichtwetten-Tagebuch

Auf ausdrücklichen Wunsch zusätzlicher Reiter Papiermodus. Ein selbst markierter Nichtwetten-Tag zählt einmalig20Euro als fiktiv nicht eingesetzten Vergleichsbetrag. Kein echter Geldtransfer, kein berechneter Gewinn, keine Behauptung vermiedener Verluste. Öffnen oder Tageswechsel erzeugen keinen Eintrag. Heutiger Eintrag kann zurückgenommen werden; Doppelklick und erneutes Markieren verdoppeln den Betrag nicht.

Der Verlauf liegt ausschließlich in browserlokalem localStorage. Das Frontend enthält keine Remote-Skripte und keine Netzwerkabfragen. Es sendet keine Tagebucheinträge oder Beträge an Streamlit zurück; an den Container gehen nur die normalen Bereitschafts-/Höhenmeldungen. Private Einträge sind weder im GitHub-Paket noch im gemeinsamen Cloud-Dateisystem. Das Backend übergibt nur Darstellung und aktuelles deutsches Datum. Bei gesperrtem Speicher wird keine erfolgreiche Speicherung behauptet. Lokales JSON-Backup und validierter Merge-Import sind vorhanden; zukünftige/ungültige Tage und unbekannte Schemafelder werden verworfen, vorhandener Verlauf nicht still überschrieben. Geräte/Browserspeicher synchronisieren nicht automatisch.

Keine neuen Tipps, Wettkombinationen, Quoten, Einsatzempfehlungen oder automatischen Tageswetten. Der im geteilten Chat erwähnte10-Euro-Papierschein wird nur als ungeprüfter Hinweis beschrieben; keine Ergebnisse oder Ersparnis daraus gebucht. Im anderen Chat behauptete Automationen wurden nicht übernommen. Bestehende KickTipp-Modelle, Daten und Auswertungen unverändert. Keine zusätzlichen Mac-Prozesse.
