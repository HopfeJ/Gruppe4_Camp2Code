import bauplaene

ingo = bauplaene.Mensch("Blond", 46, 194)
print(ingo.haarfarbe)
print(ingo.koerpergroesse)

ralf = bauplaene.Mensch("Blond", 46, 194)
print(ralf.schuhgroesse)


ingo.haarfarbe = "Lila" # ganz schlecht. Attribute nur über Methoden verändern !!!
ingo.haare_faerben("Schwarz") # So werden Attribute verändert !!! Recht so ! Setter-Methode
print(ingo.anzahl_faerbungen)
print(ingo.haarfarbe) # Eigentlich ist das auch nicht so ideal, besser Getter-Methode verwenden
print(ingo.get_haarfarbe()) # Richtig gut. Ausgabe von attributen mit den sogn. Getter-Methoden
ingo.haare_faerben("Grün")
print(ingo.anzahl_faerbungen)
print(ingo.get_haarfarbe())

ingo.altersbedingtes_schrumpfen(192)
print(ingo.get_koerpergroesse())