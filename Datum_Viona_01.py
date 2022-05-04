#       Vorsetzen des jeweiligen
#           Datums an die reuntergeladenen
#               vitero Dateien in den Ordnern
#########################################################
#
#		_01 nach vitero online.... own folders...
#
import os

# Inhalt des Verzeichnis in Liste auslesen
def readfiles():
    daten = []
    for file in os.listdir():       # Dateien einlesen
        daten.append(file)          # Liste mit file erstellen
    return daten

# Den passenden Datumsstempel aus dem Tagesordner ziehen
def tagdatum():
    namen = []
    namen = readfiles()
    dias = []
    for i in namen:
        if len(i) > 10:         # für Vitero-Ordner
            day = i[20:30]
            tag = day[0:4] + day[5:7] + day[8:10] + "_"
        else:
            tag = i + "_"       # für JJJJMMTT - Ordner
        dias.append(tag)
    return dias

# Den Datumsstempel vor den Dateinamen setzen
def umbenennen():
    t = o[s]
    d = readfiles()
    for x in d:
        if t == x[0:9]:		# schon gestempelt?
            continue
        new = t + x
        os.rename(x,new)
        print (new)

# Main Programm
p = "C:\\Users\\_userkonto_\\Desktop\\vitero Dateien\\"
os.chdir(p)
verzeichnisse = readfiles()
o = tagdatum()
s = 0
for a in verzeichnisse:
    p1 = p + a
    os.chdir(p1)
    currentday = o[s]             #   Datumsstempel
    if len(a) < 10:         # für JJJJMMTT - Ordner
        readfiles()
        umbenennen()
    else:
        unterverzeichnis = ["\\Dateien","\\Screenshots\\Anzeigefläche","\\Screenshots\\Raum"]
        for b in unterverzeichnis:
            p2 = p1 + b
            print (p2)
            if os.path.exists(p2):            
                    os.chdir(p2)
                    readfiles()
                    umbenennen()
    s = s + 1
print("Fertig!")
#a=input("mach")


