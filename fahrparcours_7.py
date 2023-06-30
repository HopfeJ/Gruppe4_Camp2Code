import time
from sensor_car import SensorCar
"""
Fahrparcours #7 - Erweiterte Linienverfolgung mit Hinderniserkennung. 

Kombination von Fahrparcours #6 und der Hinderniserkennung aus Fahrparcours #4.
Das Auto folget einer Linie bis über den Ultraschallsensor ein Hinderniss erkannt wird.
Bei Erfassung des Hindernisses stoppt das Auto.

Dabei wird die Klasse SensorCar genutzt.

Methoden:
    fahrparcours_6(SensorCar-Objekt)
"""

def fahrparcours_7(my_car):
    """
    Führt den Fahrparcours #7 durch, bei dem das Auto mithilfe des Line-Follower-Sensors gesteuert wird.

    Der Fahrparcours beginnt mit der Erstellung der TXT-Datei und dem Start des Autos mit einer Geschwindigkeit von 40.
    Der Lenkwinkel wird auf 90 Grad eingestellt, um das Auto geradeaus zu halten. Das Auto wird dann kontinuierlich mithilfe
    des Line-Follower-Sensors gesteuert, bis es die Linie vollständig verlassen hat oder ein Hindernis erkannt wurde.
    Bei einem erkannten Hindernis wird das Auto gestoppt, die Daten werden gespeichert und der Fahrparcours endet.

    Args:
        my_car (SensorCar): Das Autoobjekt aus der Klasse SensorCar, das den Fahrparcours durchführt.

    """
    my_car.create_data_table()
    my_car.drive(40,1) # Volle Fahrt voraus
    my_car.steering_angle = 90 # Räder gerade stellen
    while True:
        fertig = my_car.drive_with_line_follower(7)
        if fertig:
            break
        if my_car.distance < 15 and my_car.distance > 0: # Hinderniserkennung
            print(f'Ergebnis Stop (Abstand Hindernis) {my_car.distance}')
            my_car.stop()
            my_car.save_data(my_car.speed, my_car.direction, my_car.steering_angle, my_car.distance, 3, my_car.sensordaten)
            break
        
if __name__ == "__main__":
    """
    Hauptfunktion des Programms:

    Erzeugt ein SensorCar-Objekt my_car und ruft die Methode fahrparcours_7 auf,
    so dass my_car den Fahrparcours #7 durchlaufen kann.

    """
    my_car = SensorCar()
    fahrparcours_7(my_car)  