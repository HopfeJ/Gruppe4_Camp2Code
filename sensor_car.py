from sonic_car import SonicCar
from basisklassen import Infrared

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

if __name__ == '__main__':

    my_car = SensorCar()
    print(my_car.sensordaten)
    print(my_car.auswertung_sensordaten())