import base_car
import time

"""
Fahrparcours #1 - Vorwärts und Rückwärts: 

Das Auto soll mit langsamer Geschwindigkeit 
für 3 Sekunden geradeaus, 
für 1 Sekunde stoppen
und wieder für 3 Sekunden rückwärts
fahren.

Methoden:
    fahrparcours_1(BaseCar-Objekt)
"""

def fahrparcours_1(my_car):

    """Führt den Fahrparcours #1 aus.

    Das Auto fährt zunächst mit einer Geschwindigkeit von 50 für 3 Sekunden geradeaus,
    stoppt für 1 Sekunde, fährt anschließend mit einer
    Geschwindigkeit von 30 rückwärts für 3 Sekunden und stoppt erneut.

    Args:
        my_car: Das Autoobjekt, aus der Klasse BaseCar() das den Fahrparcours durchführen soll.

    """

    my_car.drive(50,1)
    time.sleep(3)
    my_car.stop()
    time.sleep(1)
    my_car.drive(30,-1)
    time.sleep(3)
    my_car.stop()

if __name__ == "__main__":
    """Hauptfunktion des Programms:

    Erzeugt ein BaseCar-Objekt my_car und ruft die Methode fahrparcours_1 auf,
    so dass my_car den Fahrparcours #1 durchlaufen kann.

    """

    my_car = base_car.BaseCar()
    fahrparcours_1(my_car)