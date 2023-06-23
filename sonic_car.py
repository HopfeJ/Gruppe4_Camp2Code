from base_car import BaseCar
import basisklassen
from datetime import datetime
import time
import random


class Sonic_Car(BaseCar):
   
    
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
        start = datetime.now()
        while (datetime.now()-start).seconds<= zeit:
            abstand = self.ultraschall.distance()
            time.sleep(0.2)
            print(abstand)
            if abstand < 10:
                self.ultraschall.stop()
                self.stop()
                self.drive(30,-1)
                self.steering_angle = random.randrange(0,180)
                time.sleep(2)
                self.steering_angle = 90
                self.stop()
                break
    
    
            
            
            
car = Sonic_Car()

car.steering_angle = 90
car.drive(30,1) #auto fährt los
car.distance_schleife(3) #beginn schleife
car.drive(50,1)
#car.steering_angle = 110
car.distance_schleife(3)
car.drive(80,1)
car.distance_schleife(3)
car.drive(100,1)
car.distance_schleife(3)

car.stop()
#if car.distance < 10 :
#    car.stop()
     
#time.sleep(2)
#car.stop()  