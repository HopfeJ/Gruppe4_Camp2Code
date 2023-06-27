from base_car import BaseCar
import basisklassen
from datetime import datetime
import time
import random
import csv


class SonicCar(BaseCar):
   
    
    def __init__(self):
        super().__init__()
        self.ultraschall = basisklassen.Ultrasonic()
        self.__distance = None
        
    @property   
    def distance(self):
        self.__distance = self.ultraschall.distance()
        self.ultraschall.stop()
        return self.__distance
    
    def distance_schleife(self,zeit:int):
        lenkwinkel_list =[0,180] 
        start = datetime.now()
        while (datetime.now()-start).seconds<= zeit:
            abstand = self.ultraschall.distance()
            time.sleep(0.2)
            print(abstand)
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
        with open('fahrdaten.txt', 'w', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(["Geschwindigkeit", "Fahrtrichtung", "Lenkwinkel", "Abstand", "Zeitstempel", "Fahrparcours"])

    def save_data(self,speed,direction,steering_angle,distance, fahrparcours):
        with open('fahrdaten.txt','a',encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow([speed,direction,steering_angle,distance,datetime.now().replace(microsecond=0), fahrparcours])

if __name__ == '__main__':
    car = SonicCar()
    car.save_data(50,1,90,290)