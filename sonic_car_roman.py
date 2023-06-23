from base_car import BaseCar
import basisklassen
import time



class Sonic_Car(BaseCar):
   
    
    def __init__(self):
        super().__init__()
        self.ultraschall = basisklassen.Ultrasonic()
        self.__distance = None
        
    @property   
    def last_distance_measured(self):
        #self.__distance = self.ultraschall.distance()
        #self.ultraschall.stop()
        return self.__last_distance_measured
    
    def get_distance(self):
        self.__last_distance_measured = self.ultraschall.distance()
        self.ultraschall.stop()
        return self.__last_distance_measured
        
    def distance_schleife(self):
        while True :
            #abstand = self.ultraschall.distance() 
            abstand = self.get_distance()
            time.sleep(0.2)
            print(abstand)

            if abstand < 10:
                self.ultraschall.stop()
                self.stop()
                self.drive(30,-1)
                self.steering_angle = 110
                time.sleep(3)
                self.steering_angle = 90
                self.stop()
                break
    
    
car = Sonic_Car()


car.drive(60,1) #auto fährt los
car.distance_schleife() #beginn schleife
car.drive(50,1)
car.steering_angle = 110
car.distance_schleife()
car.stop()
#if car.distance < 10 :
#    car.stop()
     
#time.sleep(2)
#car.stop()  