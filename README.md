# Kicktipp – Online-Testversion

Vorbereitet aus der laufenden lokalen Website. Noch nicht veröffentlicht.

## Bereitstellen
1. Ein neues privates GitHub-Repository anlegen und diese Ordnerinhalte hochladen. Keine Passwörter oder Tokens hochladen.
2. Streamlit Community Cloud mit GitHub verbinden und dieses Repository auswählen.
3. Startdatei: `app.py`. Unter Advanced settings Python **3.11** wählen.
4. App-Zugriff in den Freigabeeinstellungen auf die vorgesehenen Nutzer begrenzen; private Quelltexte allein sind kein Zugriffsschutz für die Website.
5. Zunächst gespeicherte Tipps und Deep Dive prüfen. Danach einen Optimierungslauf testen und Laufzeit/Ressourcen beobachten.
6. Die neue HTTPS-Adresse in Safari öffnen und zum Home-Bildschirm hinzufügen.

## Vor dem dauerhaften Einsatz
Die mitgelieferten historischen Daten, Modellprüfungen und bisherigen Tipps sind enthalten. Neue Tipps und Rückblicke schreibt die Anwendung derzeit auf das Server-Dateisystem. Dieses ist bei Community Cloud **nicht dauerhaft garantiert**. Externe dauerhafte Speicherung samt Wiederherstellung muss noch ergänzt und getestet werden. Diese Fassung deshalb nur als Online-Test verwenden; neue Prognosen könnten bei einem Serverneustart verloren gehen. Keine zuverlässige spätere Bewertung ohne erhaltenes Vorabarchiv versprechen.

Die historische Modellauswahl wird aus den bestehenden Prüfberichten geladen, sofern deren Daten- und Codeprüfsummen übereinstimmen. Paketversionen sind festgelegt. Bei abweichenden Prüfsummen kann die bestehende Anwendung eine aufwendige Neuberechnung beginnen; vor der Freigabe den Cloud-Start prüfen.

Keine Mac-spezifische Installation, kein Xcode, kein Zugriff auf das Heimnetz erforderlich. Der Mac muss nach erfolgreicher Bereitstellung nicht eingeschaltet sein. Das iPhone benötigt Internet. Die Fußballtexte sind weiterhin eine getrennte Einordnung und kein zusätzlicher numerischer Modellfaktor.
