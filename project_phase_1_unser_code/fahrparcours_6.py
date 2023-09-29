import time
from sensor_car import SensorCar
"""
Fahrparcours #6 - Erkundungstour mit erweiterter Linienverfolgung: 

Wie Fahrparcours #5, jedoch mit Links- und Rechtskurven mit
Kurvenradien kleiner als der maximale Lenkwinkel.

Folgen einer etwas 1,5 bis 2 cm breiten Linie auf
dem Boden. Das Auto stoppt, sobald das Ende der Linie erreicht wird. 

Dabei soll ein "Parcours" durchfahren werden, der sowohl eine Rechts- 
als auch eine Linkskurve macht. Die Kurvenradien sind deutlich kleiner als der maximale Radius, 
den das Auto ohne ausgleichende Fahrmanöver fahren kann.

Dabei wird die Klasse SensorCar genutzt.

Methoden:
    fahrparcours_6(SensorCar-Objekt)
"""

def fahrparcours_6(my_car):
    """
    Führt den Fahrparcours #6 durch.

    Die Fahrt duch den Parcours beginnt mit einer 10-sekündigen Wartezeit. 
    Danach wird die TXT-Datei erstellt
    und das Auto fährt mit einer Geschwindigkeit von 40 vorwärts. Der Lenkwinkel wird auf 90 Grad eingestellt,
    um das Auto geradeaus zu halten. 
    
    Das Auto wird dann kontinuierlich mithilfe des Line-Follower-Sensors gesteuert,
    bis es die Linie vollständig verlassen hat.

    Der Line-Follower-Sensor wird verwendet, um das Auto entsprechend der Linien auf der Fahrbahn
    zu steuern. Je nach Sensorwerten wird der Lenkwinkel angepasst und die Daten werden gespeichert.
    Es wird auch überprüft, ob das Auto die Linie vollständig verlassen hat und entsprechend reagiert.

    Args:
        my_car (SensorCar): Das Autoobjekt aus der Klasse SensorCar.

    """
    my_car.create_data_table()
    my_car.drive(40,1) # Volle Fahrt voraus
    my_car.steering_angle = 90 # Räder gerade stellen
    while True:
        fertig = my_car.drive_with_line_follower(6)
        if fertig:
            break

if __name__ == "__main__":
    """
    Hauptfunktion des Programms:

    Erzeugt ein SensorCar-Objekt my_car und ruft die Methode fahrparcours_6 auf,
    so dass my_car den Fahrparcours #6 durchlaufen kann.

    """
    my_car = SensorCar()
    fahrparcours_6(my_car)  