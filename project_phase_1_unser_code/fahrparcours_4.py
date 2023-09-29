from sonic_car import SonicCar
import time
"""
Fahrparcours #4 - Erkundungstour: 

Das Auto variiert bei freier Fahrt die Fahrrichtung und die Geschwindigkeit variieren. 
Im Falle eines Hindernisses ändert das Auto die Fahrrichtung und setzt die Fahrt fort. 
Zur Änderung der Fahrtrichtung wird dabei
ein maximaler Lenkwinkel eingeschlagen und rückwärts gefahren. 
Dabei wird bei jeder relevanten Änderung die aktuellen Fahrdaten mitgeloggt.

Als Ergebnis wird das Auto den hindernsfreien Raum “erkunden”. 

Dabei wird die Klasse SonicCar genutzt.

Methoden:
    fahrparcours_4(BaseCar-Objekt)
"""


def fahrparcours_4(my_car):
    """Führt den Fahrparcours #4 durch:

    Der Fahrparcours #4 umfasst mehrere Schritte, bei denen das Auto bestimmte Geschwindigkeiten
    und Lenkwinkel verwendet. Es wird eine TXT-Datei für die Datenspeicherung erstellt.
    In einer Schleife werden die folgenden Schritte ausgeführt:
    - Fahren mit 50 km/h im Geradeauslauf
    - Speichern der aktuellen Daten wie Geschwindigkeit, Richtung, Lenkwinkel und Abstand
    - Warten für eine bestimmte Zeit
    - Fahren mit 80 km/h im Geradeauslauf
    - Wiederholtes Speichern der Daten und Warten
    - Fahren mit 50 km/h geradeaus und einem Lenkwinkel von 60 Grad
    - Wiederholtes Speichern der Daten und Warten
    - Fahren mit 60 km/h geradeaus und einem Lenkwinkel von 90 Grad
    - Wiederholtes Speichern der Daten und Warten

    Nachdem die Schleife einmal durchlaufen wurde, wird das Auto angehalten und die aktuellen
    Daten werden gespeichert.

    Args:
        my_car (SonicCar): Das Autoobjekt aus der Klasse SonicCar, das den spezifischen Fahrparcours durchführen soll.

    """
    my_car.create_data_table()
    zaehler = 0
    while zaehler < 1:
        my_car.drive(50,1)
        my_car.save_data(my_car.speed, my_car.direction, my_car.steering_angle, my_car.distance, 4)
        my_car.distance_schleife(3)
        my_car.drive(80,1)
        my_car.save_data(my_car.speed, my_car.direction, my_car.steering_angle, my_car.distance, 4)
        my_car.distance_schleife(3)
        my_car.drive(50,1)
        my_car.steering_angle = 60
        my_car.save_data(my_car.speed, my_car.direction, my_car.steering_angle, my_car.distance, 4)
        my_car.distance_schleife(2)
        my_car.drive(60,1)
        my_car.steering_angle = 90
        my_car.save_data(my_car.speed, my_car.direction, my_car.steering_angle, my_car.distance, 4)
        my_car.distance_schleife(8)
        zaehler +=1

    if zaehler == 1:
        my_car.stop()  
        my_car.save_data(my_car.speed, my_car.direction, my_car.steering_angle, my_car.distance, 4)


if __name__ == "__main__":
    """Hauptfunktion des Programms:

    Erzeugt ein SonicCar-Objekt my_car und ruft die Methode fahrparcours_4 auf,
    so dass my_car den Fahrparcours #4 durchlaufen kann.

    """
    my_car = SonicCar()
    fahrparcours_4(my_car)      