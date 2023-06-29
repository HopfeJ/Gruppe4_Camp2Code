from sonic_car import SonicCar
from basisklassen import Infrared
import time

class SensorCar(SonicCar):

    def __init__(self):
        super().__init__()
        self.line_sensor = Infrared()

    @property 
    def sensordaten(self):
        #return self.line_sensor.get_average()
        return self.line_sensor.read_analog()

    def auswertung_sensordaten(self):
        wert = 80 # Tisch: 30, Boden: 50
        hell = 100 # Tisch: 50, Boden: 120
        print(self.sensordaten)
        if self.sensordaten[0] < wert:
            print('Links ist es dunkel.')
            self.steering_angle = 45
        elif self.sensordaten[1] < wert:
            print('Links Mitte ist es dunkel.')
            self.steering_angle = 70 # 70
        elif self.sensordaten[2] < wert:
            print("In der Mitte ist es dunkel.")
            self.steering_angle = 90     
        elif self.sensordaten[3] < wert:
            print('Rechts Mitte ist es dunkel.')
            self.steering_angle = 115
        elif self.sensordaten[4] < wert:
            print('Rechts ist es dunkel.')
            self.steering_angle = 135


        if self.sensordaten[0] > hell and self.sensordaten[1] > hell and self.sensordaten[2] > hell and self.sensordaten[3] > hell and self.sensordaten[4] > hell:
            self.drive(30,-1) # 40
            self.steering_angle = 45
            time.sleep(0.1) #0.3
            if self.sensordaten[0] > hell and self.sensordaten[1] > hell and self.sensordaten[2] > hell and self.sensordaten[3] > hell and self.sensordaten[4] > hell:
                self.drive(30,1)
                time.sleep(0.2) #0.5
            self.drive(30,-1)
            self.steering_angle = 135
            time.sleep(0.1) #0.5
            if self.sensordaten[0] > hell and self.sensordaten[1] > hell and self.sensordaten[2] > hell and self.sensordaten[3] > hell and self.sensordaten[4] > hell:
                self.steering_angle
                self.stop()
                quit()
            else:    
                self.drive(30,1)
            

if __name__ == '__main__':
    my_car = SensorCar()
    # print(my_car.line_sensor.test())
    
    print(my_car.sensordaten)
    my_car.steering_angle = 90
    
    my_car.drive(30,1)
    while True:
        my_car.auswertung_sensordaten()