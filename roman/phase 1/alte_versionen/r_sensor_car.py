from mycar import *
from r_basisklassen import *
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
        wert = 25
        print(self.sensordaten)
        if self.sensordaten[0] <= wert:
            print('Links ist es dunkel.')
            self.steering_angle = 120
        elif self.sensordaten[1] <= wert:
            print('2. von Links ist es dunkel.')
            self.steering_angle = 105
        elif self.sensordaten[2] <= wert:
            print('Mitte ist es dunkel.')
            self.steering_angle = 90
        elif self.sensordaten[3] <= wert:
            print('2. von Rechts ist es dunkel.')
            self.steering_angle = 75
        elif self.sensordaten[4] <= wert:
            print('Rechts ist es dunkel.')
            self.steering_angle = 60
        time.sleep(0.2)   
         
        if self.sensordaten[0] > wert and self.sensordaten[1] > wert and self.sensordaten[2] > wert and self.sensordaten[3] > wert and self.sensordaten[4] > wert:
            print(self.sensordaten)
            self.drive(30,-1)
            time.sleep(0.5)
            self.drive(30, 1)


            # self.stop()
            # print("stop")
            # quit()





if __name__ == '__main__':

    my_car = SensorCar()
    # print(my_car.sensordaten)
    # print(my_car.auswertung_sensordaten())
    my_car.drive(30, 1)
    my_car.steering_angle = 90
    while True:
        my_car.auswertung_sensordaten()


    #print(my_car.line_sensor.test())
    #time.sleep(5)
    #my_car.stop()