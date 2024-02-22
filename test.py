print("Willkommen zum Raum-Messungs-Tool!")
print("Bitte geben Sie zunächst ihren Namen und dann das heutige Datum ein")
print("Name:")
Name = input()
print("Datum:")
Datum = input()

Fertig = False
alleRäume = 0
ErgebnisGroßraumSumme = 0

while not Fertig:
    print("Ist der Raum Rechteckig? (ja/nein):")
    raumAntwort = input()
    if raumAntwort.lower() == "nein":
        raumAntwortLoop = True
        ErgebnisGroßraum = 0  
        while raumAntwortLoop:
            print("Bitte geben Sie die Länge des Raumes ein")
            Raumlänge = input()
            print("Bitte geben Sie nun die Breite des Raumes ein")
            Raumbreite = input()
            ErgebnisGroßraum += int(Raumlänge) * int(Raumbreite)
            raumAntwortFertig = input("Ist der Raum fertig? (ja/nein): ")
            if raumAntwortFertig.lower() != "ja":
                continue
            else:
                raumAntwortLoop = False  
        
        ErgebnisGroßraumSumme += ErgebnisGroßraum
    else:
        print("Bitte geben Sie die Länge des Raumes ein")
        Raumlänge = input()
        print("Bitte geben Sie nun die Breite des Raumes ein")
        Raumbreite = input()
        Ergebnis = int(Raumlänge) * int(Raumbreite)
        alleRäume += Ergebnis 

        print("Der Raum ist " + str(Ergebnis) + " Quadratmeter groß")
        print("Länge: " + Raumlänge)
        print("Breite: " + Raumbreite)
        
    
    antwort = input("Möchten Sie weitere Messungen durchführen? (ja/nein): ")
    if antwort.lower() != "ja":
        Fertig = True

print("Fertig")
print("Messergebnisse von " + Name + " am " + Datum + ":")
print("Gesamtfläche aller Räume: " + str(alleRäume + ErgebnisGroßraumSumme))
