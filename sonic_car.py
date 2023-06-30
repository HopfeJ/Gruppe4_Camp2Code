from base_car import BaseCar
import basisklassen
from datetime import datetime
import time
import random
import csv


class SonicCar(BaseCar):
    """
        Diese Klasse steuert einen Sunfounder PiCar-S Bausatz.
        Die Klasse SonicCar erbt von der Klasse BaseCar die Fahr- und Steuerbefehle.
        In SonicCar wird nun der Ultraschall-Sensor implementiert, der den Abstand zu einem Hindernis in cm zurück gibt.
        Zur Nutzung dieser Klasse ist die Klasse Ultrasonic aus basisklassen.py erforderlich.

        Attribute:

        distance: int
            Gibt den Abstand zu einem Hindernis vor dem Fahrzeug in cm zurück

        Methoden:

        distance_schleife(self,zeit:int):
            Diese Methode wird benötigt zur Realisierung des Fahrparcours 4 in der Projektphase 1 Camp2Code 2023 
        create_data_table(self):
            Erzeugt eine csv-Datei mit Headlines zur Speicherung der Fahrdaten
        save_data(self,speed,direction,steering_angle,distance, fahrparcours):
            Speichert die Fahrdaten des Fahrzeugs während der Fahrt
    """
    
    def __init__(self):
        """
            Im Konstruktor wird die Instanz für die Ansteuerung des Ultraschallsensors erzeugt.
            Außerdem wird das Attribut zur Erfassung des Abstandes dieses Sensors initialisiert.

            Attribute:

            distance: int
                Abstand eines Hindernisses vor dem Fahrzeug in cm
        """
        super().__init__()
        self.ultraschall = basisklassen.Ultrasonic()
        self.__distance = None
        
    @property   
    def distance(self) -> int: # Getter Methode für distance
        self.__distance = self.ultraschall.distance()
        self.ultraschall.stop()
        return self.__distance
    
    def distance_schleife(self,zeit:int):
        """
            Diese Methode wird benötigt zur Realisierung des Fahrparcours 4 in der Projektphase 1 Camp2Code 2023 

            Args:

            zeit: int
                zeit ist die Laufzeit der while-Schleife in Sekunden 
        """
        lenkwinkel_list =[0,180] 
        start = datetime.now()
        while (datetime.now()-start).seconds<= zeit:
            abstand = self.ultraschall.distance()
            time.sleep(0.2)
            # print(abstand)
            if abstand < 15 and abstand > 0:
                self.ultraschall.stop()
                self.stop()
                self.drive(30,-1)
                self.save_data(self.speed, self.direction, self.steering_angle, abstand, 4)
                self.steering_angle = random.choice(lenkwinkel_list)
                time.sleep(2)
                self.steering_angle = 90
                self.stop()
                break
    
    def create_data_table(self):
        """
            Erzeugt eine csv-Datei mit Headlines zur Speicherung der Fahrdaten
        """
        with open('fahrdaten.txt', 'w', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(["Geschwindigkeit", "Fahrtrichtung", "Lenkwinkel", "Abstand", "Zeitstempel", "Fahrparcours"])

    def save_data(self,speed: int,direction: int,steering_angle: int,distance: int, fahrparcours: int):
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
        """
        with open('fahrdaten.txt','a',encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow([speed,direction,steering_angle,distance,datetime.now().replace(microsecond=0), fahrparcours])

if __name__ == '__main__':
    car = SonicCar()
    car.save_data(50,1,90,290)