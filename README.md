## Dokumentation zu „Storytime"

# Ziel
Das Programm Storytime soll einen kleinen Text generieren, welcher mithilfe von kleinen Eingaben eine gewisse Interaktivität erzeugen soll.
So soll man zu Beginn der Geschichte zum Beispiel den Namen unserer Figur und auch einige weitere Informationen einfügen, welche dann wiederum ein Stück weit in die Geschichte einfließen soll. Durch unterschiedliche Geschichtsteile soll eine zusätzliche Variation entstehen. 

# Vorbereitung:
Um das Programm möglichst schnell zu schreiben, haben wir zuerst einzelne Geschichtsteile formuliert und ein Beispiel erstellt, um damit die Sinnhaftigkeit der Sätze zu prüfen.
In dem Prozess haben wir uns für englische Sätze entschieden, da diese im Satzbau wesentlich einfacher handzuhaben sind als deutsche Sätze.

# Programm
Stroytime ist in Python programmiert, dort läuft das Programm linear ab.
Zu Beginn wird ein Dictionary erstellt, welches dann durch die Usereingaben befüllt wird.
Um die verschiedenen Geschichtsteile in das Programm aufzunehmen, sind diese in verschiedenen Listen gespeichert, damit eine Trennung zwischen den unterschiedlichen Geschichtszeitpunkten möglich ist. Um dann eine zufällige Wahl des Textes zu ermöglichen wird das Modul „Random.choice“ verwendet, da dies genau dafür gemacht ist, ein Element aus einer Liste auszuwählen.
Um dann die Teile in der Konsole auszugeben nutzten wir die „string.format“-Funktion, welche benannte Elemente durch die jeweiligen Werte im zuvor befüllten Dictionary Werte ersetzt. 
