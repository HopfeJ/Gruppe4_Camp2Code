from sonic_car import SonicCar
from basisklassen import Infrared
import time

class SensorCar(SonicCar):

    def __init__(self):
        super().__init__()
        self.line_sensor = Infrared()

    @property 
    def sensordaten(self):
        return self.line_sensor.get_average()
    

    def auswertung_sensordaten(self):
        if self.sensordaten[0] < 5:
            print('Links ist es dunkel.')
            self.steering_angle = 45
        elif self.sensordaten[1] < 5:
            print('Links Mitte ist es dunkel.')
            self.steering_angle = 70
        elif self.sensordaten[2] < 5:
            print("In der Mitte ist es dunkel.")
            self.steering_angle = 90
        
        if self.sensordaten[4] < 5:
            print('Rechts ist es dunkel.')
            self.steering_angle = 135
        elif self.sensordaten[3] < 5:
            print('Rechts Mitte ist es dunkel.')
            self.steering_angle = 115
        elif self.sensordaten[2] < 5:
            print("In der Mitte ist es dunkel.")
            self.steering_angle = 90
        
        if self.sensordaten[0] > 10 and self.sensordaten[1] > 10 and self.sensordaten[2] > 10 and self.sensordaten[3] > 10 and self.sensordaten[4] > 10:
            self.drive(40,-1)
            self.steering_angle = 45
            time.sleep(0.3)
            if self.sensordaten[0] > 10 and self.sensordaten[1] > 10 and self.sensordaten[2] > 10 and self.sensordaten[3] > 10 and self.sensordaten[4] > 10:
                self.drive(40,1)
                time.sleep(0.5)
            self.drive(40,-1)
            self.steering_angle = 135
            time.sleep(0.3)
            if self.sensordaten[0] > 10 and self.sensordaten[1] > 10 and self.sensordaten[2] > 10 and self.sensordaten[3] > 10 and self.sensordaten[4] > 10:
                self.steering_angle
                self.stop()
                quit()
            else:    
                self.drive(40,1)
            

if __name__ == '__main__':
    my_car = SensorCar()
    # print(my_car.line_sensor.test())
    print(my_car.sensordaten)
    my_car.steering_angle = 90
    
    my_car.drive(40,1)
    while True:
        my_car.auswertung_sensordaten()