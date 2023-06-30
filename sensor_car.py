from sonic_car import SonicCar
from basisklassen import Infrared
import time
import csv
from datetime import datetime

class SensorCar(SonicCar):
    """
        Diese Klasse steuert einen Sunfounder PiCar-S Bausatz.
        Die Klasse SensorCar erbt von den Klassen SonicCar und BaseCar die Fahr- und Steuerbefehle.
        
        In SensorCar wird nun das Line-Follower-Modul implementiert, das es dem Auto ermöglicht, 
        einer auf dem Boden aufgeklebten schwarzen Linie zu folgen. Möglich wird dies durch Auswertung
        der von den fünf integrierten Infrarotsensoren gemessenen Helligkeitswerte. 
    
        Zur Nutzung dieser des Line-Follower-Moduls ist die Klasse Infrared aus basisklassen.py erforderlich.

        Attribute:

        sensordaten: list
            Gibt die vom Line-Follower-Modul gemessenen 5 Werte der einzelnen Infrarotsenoren als Liste zurück.

        Methoden:

        create_data_table(self):
            Erzeugt eine csv-Datei mit Headlines zur Speicherung der Fahrdaten
        save_data(self,speed,direction,steering_angle,distance, fahrparcours):
            Speichert die Fahrdaten des Fahrzeugs während der Fahrt
        drive_with_line_follower(self, fahrparcours):
            Steuerung des Fahrzeugs mithilfe der gemessenen Sensordaten der Infrarotsensoren
    """
    def __init__(self):
        """
            Im Konstruktor wird die Instanz für die Ansteuerung der Infrarotsensoren erzeugt.

        """
        super().__init__()
        self.line_sensor = Infrared()

    @property 
    def sensordaten(self):
        return self.line_sensor.get_average()
    
    def create_data_table(self):
        """
            Erzeugt eine csv-Datei mit Headlines zur Speicherung der Fahrdaten
        """
        with open('fahrdaten.txt', 'w', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(["Geschwindigkeit", "Fahrtrichtung", "Lenkwinkel", "Abstand", "Zeitstempel", "Fahrparcours", "Sensordaten"])

    def save_data(self,speed,direction,steering_angle,distance, fahrparcours, sensordaten):
        """
            Speichert die Fahrdaten des Fahrzeugs während der Fahrt.
            Mit jedem Methodenaufruf wird eine neue Zeile erzeugt.

            Args:

            speed: int
                Geschwindigkeit des Fahrzeugs
            direction: int
                Fahrtrichtung des Fahrzeugs
            steering_angle: int
                Lenkwinkel des Fahrzeugs (Vorderräder)
            distance:
                Abstand eines Hindernisses zum Fahrzeug
            fahrparcours:
                Fahrparcours Nummer, dessen Daten erfasst werden sollen
            sensordaten: list
                Messwerte der fünf Infrarotsensoren
        """
        with open('fahrdaten.txt','a',encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow([speed,direction,steering_angle,distance,datetime.now().replace(microsecond=0), fahrparcours, sensordaten])

    def drive_with_line_follower(self, fahrparcours):
        """
        Führt das Fahren mit dem Line-Follower-Sensor durch.

        Der Line-Follower-Sensor wird verwendet, um das Auto entsprechend der Linien auf der Fahrbahn
        zu steuern. Je nach Sensorwerten werden der Lenkwinkel und Fahrtrichtung angepasst sowie die Daten gespeichert.
        Es wird auch überprüft, ob das Auto die Linie vollständig verlassen hat und entsprechend gestoppt.

        Args:
            self (object): Das Autoobjekt, auf dem die Methode aufgerufen wird.
            fahrparcours (int): Die Nummer des Fahrparcours für die Datenbank.

        Returns:
            bool: True, wenn das Auto die Linie vollständig verlassen hat, ansonsten False.

        """
        if self.sensordaten[0] < 5:
            # print('Links ist es dunkel.')
            self.steering_angle = 45
        elif self.sensordaten[1] < 5:
            # print('Links Mitte ist es dunkel.')
            self.steering_angle = 70
        elif self.sensordaten[2] < 5:
            # print("In der Mitte ist es dunkel.")
            self.steering_angle = 90
        
        if self.sensordaten[4] < 5:
            # print('Rechts ist es dunkel.')
            self.steering_angle = 135
        elif self.sensordaten[3] < 5:
            # print('Rechts Mitte ist es dunkel.')
            self.steering_angle = 115
        elif self.sensordaten[2] < 5:
            # print("In der Mitte ist es dunkel.")
            self.steering_angle = 90
        self.save_data(self.speed, self.direction, self.steering_angle, self.distance, fahrparcours, self.sensordaten)

        if self.sensordaten[0] > 10 and self.sensordaten[1] > 10 and self.sensordaten[2] > 10 and self.sensordaten[3] > 10 and self.sensordaten[4] > 10:
            self.drive(40,-1)
            self.steering_angle = 45
            self.save_data(self.speed, self.direction, self.steering_angle, self.distance, fahrparcours, self.sensordaten)
            time.sleep(0.3)
            if self.sensordaten[0] > 10 and self.sensordaten[1] > 10 and self.sensordaten[2] > 10 and self.sensordaten[3] > 10 and self.sensordaten[4] > 10:
                self.drive(40,1)
                self.save_data(self.speed, self.direction, self.steering_angle, self.distance, fahrparcours, self.sensordaten)
                time.sleep(0.5)
            self.drive(40,-1)
            self.steering_angle = 135
            self.save_data(self.speed, self.direction, self.steering_angle, self.distance, fahrparcours, self.sensordaten)
            time.sleep(0.3)
            if self.sensordaten[0] > 10 and self.sensordaten[1] > 10 and self.sensordaten[2] > 10 and self.sensordaten[3] > 10 and self.sensordaten[4] > 10:
                self.steering_angle
                self.stop()
                self.save_data(self.speed, self.direction, self.steering_angle, self.distance, fahrparcours, self.sensordaten)
                return True
            else:    
                self.drive(40,1)
                self.save_data(self.speed, self.direction, self.steering_angle, self.distance, fahrparcours, self.sensordaten)
            

if __name__ == '__main__':
    """
    Hauptfunktion des Programms:

    Erzeugt ein SensorCar-Objekt my_car, setzt das Auto in Bewegung und startet 
    über die Methode drive_with_line_follower() die Linienverfolgung.

    """
    my_car = SensorCar()
    # print(my_car.line_sensor.test())
    print(my_car.sensordaten)
    
    my_car.drive(40,1) # Volle Fahrt voraus
    my_car.steering_angle = 90 # Räder gerade stellen
    
    while True:
        my_car.drive_with_line_follower()