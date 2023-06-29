import base_car
import time
"""
Fahrparcours 2 - Kreisfahrt mit maximalem Lenkwinkel: 

Das Auto fährt 1 Sekunde mit 50 geradeaus, 
dann für 8 Sekunden mit maximalen Lenkwinkel im Uhrzeigersinn und stoppt.

Dann fährt das Auto diesen Fahrplan in umgekehrter Weise ab und kehrt an den Ausgangs-
punkt zurück. Die Vorgehensweise wird für eine Fahrt im entgegengesetzten Uhrzei-
gersinn wiederholt.

Methoden:
    fahrparcours_2(BaseCar-Objekt)
"""

def fahrparcours_2(my_car):
    """Führt den Fahrparcours #2 aus.

    Kreisfahrt (vorwärts und rückwärts) mit maximalem Lenkwinkel.

    Args:
        my_car: Das Autoobjekt, aus der Klasse BaseCar() das den Fahrparcours durchführen soll.

    """
    my_car.drive(50,1)
    time.sleep(1)
    my_car.steering_angle = 135
    time.sleep(8)
    my_car.stop()
    time.sleep(1) #kurzer stopp (visualisierung)
    my_car.drive(50,-1)
    my_car.steering_angle = 135
    time.sleep(8)
    my_car.steering_angle = 90
    time.sleep(1)
    my_car.stop()

    my_car.drive(50,1)
    time.sleep(1)
    my_car.steering_angle = 45
    time.sleep(8)
    my_car.stop()
    time.sleep(1) #kurzer stopp (visualisierung)
    my_car.drive(50,-1)
    my_car.steering_angle = 45
    time.sleep(8)
    my_car.steering_angle = 90
    time.sleep(1)
    my_car.stop()

if __name__ == "__main__":
    """Hauptfunktion des Programms:

    Erzeugt ein BaseCar-Objekt my_car und ruft die Methode fahrparcours_2 auf,
    so dass my_car den Fahrparcours #2 durchlaufen kann.

    """
    my_car = base_car.BaseCar()
    fahrparcours_2(my_car)




