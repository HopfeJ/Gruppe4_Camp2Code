class Mensch():

    def __init__(self, haarfarbe: str, schuhgroesse: int, koerpergroesse: int):
        self.haarfarbe = haarfarbe
        self.schuhgroesse = schuhgroesse
        self.koerpergroesse = koerpergroesse
        self.anzahl_faerbungen = 0

    def haare_faerben(self, farbe): # Setter-Methode für Haarfarbe = Ändern eines Attributes (Eigenschaft)
        self.haarfarbe = farbe
        self.anzahl_faerbungen = self.anzahl_faerbungen + 1
    
    def get_haarfarbe(self): # Getter-Methode für Haarfarbe = Abfrage eines Attributes (Eigenschaft)
        return self.haarfarbe

class Klavier():
   
    def __init__(self, anz_tasten: int, fabrikant: str, farbe: str):
        self.anz_tasten = anz_tasten
        self.fabrikant = fabrikant
        self.farbe = farbe

class Auto():

    def __init__(self, akt_geschwindigkeit: int, farbe: str, max_geschwindigkeit: int):
        self.akt_geschwindigkeit = akt_geschwindigkeit
        self.farbe = farbe
        self.max_geschwindigkeit = max_geschwindigkeit