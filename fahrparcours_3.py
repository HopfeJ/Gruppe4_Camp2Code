from sonic_car import SonicCar
import time

"""
Fahrparcours 3 - Vorwärtsfahrt bis Hindernis: 

Fahren bis ein Hindernis im Weg ist und dann stoppen. 
Während dieser Fahrt werden die Fahrdaten 
(Geschwindigkeit, Lenkwinkel, Fahrrichtung, Sensordaten) 
aufgezeichnet.

Methoden:
    fahrparcours_3(BaseCar-Objekt)
"""

def fahrparcours_3(my_car):
    """Führt Fahrparcours #3 mit Hinderniserkennung und Datenspeicherung durch.

    Der Fahrparcours #3 beginnt mit der Erstellung einer TXT-Datei für die Datenspeicherung.
    Das Auto fährt mit einer Geschwindigkeit von 50 vorwärts und speichert Daten
    wie Geschwindigkeit, Richtung, Lenkwinkel und zurückgelegte Strecke für Fahrparcours #3.
    Dazu wird die Methode save_data() verwendet.

    Währenddessen wird der Abstand zu einem eventuellem Hindernis überwacht. Sobald der Abstand unter 15 liegt
    und größer als 0 ist, wird das Auto angehalten und die relevanten Daten werden gespeichert.
    Anschließend wird der Fahrparcours beendet.

    Args:
        my_car (SonicCar): Das Autoobjekt aus Klasse SonicCar, das den Fahrparcours mit Hinderniserkennung durchführen soll.

    """
    my_car.create_data_table()
    my_car.drive(50,1)
    my_car.save_data(my_car.speed, my_car.direction, my_car.steering_angle, my_car.distance, 3)
    while True:
        distance = my_car.distance
        # print(distance)
        time.sleep(0.2)
        if distance < 15 and distance > 0:
            print(f'Ergebnis Stop (Abstand Hindernis) {distance}')
            my_car.stop()
            my_car.save_data(my_car.speed, my_car.direction, my_car.steering_angle, distance, 3)
            break


if __name__ == "__main__":
    """Hauptfunktion des Programms:

    Erzeugt ein SonicCar-Objekt my_car und ruft die Methode fahrparcours_3 auf,
    so dass my_car den Fahrparcours #3 durchlaufen kann.

    """
    my_car = SonicCar()
    fahrparcours_3(my_car)