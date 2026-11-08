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

## Betting Optimizer: Analyse und Test, kein Echtgeldbetrieb

Dritte Kategorie mit täglichem lokalen historischen Datencheck beim Öffnen (kein unbeaufsichtigter Scheduler), Datenqualitäts-Gates, fest definierter explorativer 1X2-Testregel und Risiko-/Erwartungswert-Rechner. Archiviertes früheres Einzelmodell und BWH/BWD/BWA-Quoten werden über Datum und beide Teams samt Endergebnis abgeglichen. Pro Spiel nur ein virtueller Tipp, ab 5 % Modell-EV, 10 € virtueller Einsatz, vor Kosten. Keine Strategieoptimierung auf dieser Testsaison. Bei fehlerhaften oder widersprüchlichen Daten keine Freigabe. Wochen-Bootstrap, Drawdown und negative Ergebnisse werden angezeigt. Unbekannte Quotenzeitpunkte schließen eine handelbare ROI-Validierung ausdrücklich aus.

Kein Bwin-Login, keine Wetten, keine Transaktionen, keine neuen Konten oder kostenpflichtigen Dienste. Keine echte Einsatzempfehlung: angezeigt werden 0 €. Aktuelle deutsche Bwin-Quoten, festes Budget, validiertes Wettmodell, weitere Sportmodelle, dauerhafter Speicher und täglicher Cloud-Zeitplan fehlen weiterhin. Der Rechner verwendet frei angenommene Trefferchancen und unabhängige identische Scheine, keine vom Modell geschätzte Kombichance. Kostenlose Football-Data-Quoten sind laut Anbieter periodische Freitags-/Dienstagssnapshots, kein Livefeed.

## Vertiefte Modelltests

Reproduzierbare initiale und erweiterte retrospektive Forschung: 216 feste Konfigurationen, acht Prognose-Saisons, sechs spätere Test-Saisons. Auswahl auf vorherigen Saisons; wöchentliche Modellfits mit strikter Datumsschranke. 2.448 Prognosen, 2.322 mit brauchbaren Quoten, 126 unvollständige Quotensätze ausgeschlossen. 1.076 spätere virtuelle Tipps: −811,80 € vor Kosten, −1.309,21 € bei 5 % angenommenem Auszahlungsabzug, −1.781,75 € bei zusätzlich 5 % schlechteren Quoten. Szenarioabzüge sind keine Behauptung zur tatsächlichen Bwin-Abrechnung. Kein belastbar positiver Business Case und keine Echtgeld-Freigabe. Positive rückblickend ausgewählte Varianten werden ausdrücklich als nachträgliche Auswahl gekennzeichnet.

Quotenzeitpunkte unbekannt; 2025/26 war bereits in vorherigen Analysen betrachtet. Kein unberührter Vorab-Test. In der Cloud werden nur gespeicherte Berichte geladen; keine Dauerschleife und keine neue Modellrechnung durch den Aufruf der Seite. Der Nutzer kann den Bericht herunterladen.

## Weitere Forschungsrunde

318 zusätzliche feste Konfigurationen: Form-/Schussdaten mit vorigen sechs Ligaspielen und vorab standardisierten wöchentlichen Markt-Offset-Regressionen, Über/Unter 2,5 sowie Preisvergleich mit Pinnacle-Vorabquoten und proportionaler/Power-Margenbereinigung. Zusammen534 Konfigurationen, keine unabhängigen534 Experimente. 1X2 mit Bwin: 918 spätere virtuelle Tipps, −489,90 € vor Kosten; OU2,5 mit Bet365 als ausdrücklich markiertem Vergleich: 604 Tipps, −639,40 €. Vorgeschaltete Freigabe hätte jeweils keine Wetten zugelassen. Preisvergleich nach Abzug: nicht genug frühere Fälle für mindestens30 Beobachtungen. Kein positiver Business Case, keine Echtgeld-Freigabe. Neue und bisherige Prüfungen sind separat einsehbar und herunterladbar.
