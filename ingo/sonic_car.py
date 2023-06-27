from base_car import BaseCar
import basisklassen
from datetime import datetime
import csv

class SonicCar(BaseCar):
    
    def __init__(self):
        super().__init__()
        self.ultraschall_sensor = basisklassen.Ultrasonic()
        self.__distance = None

    @property
    def distance(self):
        self.__distance = self.ultraschall_sensor.distance()
        self.ultraschall_sensor.stop()
        return self.__distance

    def create_data_table(self):
        with open('fahrdaten.txt', 'w', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(["Geschwindigkeit", "Fahrtrichtung", "Lenkwinkel", "Abstand", "Zeitstempel", "Fahrparcours"])

    def save_data(self,speed,direction,steering_angle,distance, fahrparcours):
        with open('fahrdaten.txt','a',encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow([speed,direction,steering_angle,distance,datetime.now().replace(microsecond=0), fahrparcours])

if __name__ == "__main__":
    my_car = SonicCar()
    my_car.save_data(50,1,135,240)