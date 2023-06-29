from sonic_car import SonicCar
from basisklassen import Infrared
import time
import csv
from datetime import datetime

class SensorCar(SonicCar):

    def __init__(self):
        super().__init__()
        self.line_sensor = Infrared()

    @property 
    def sensordaten(self):
        return self.line_sensor.get_average()
    
    def create_data_table(self):
        with open('fahrdaten.txt', 'w', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(["Geschwindigkeit", "Fahrtrichtung", "Lenkwinkel", "Abstand", "Zeitstempel", "Fahrparcours", "Sensordaten"])

    def save_data(self,speed,direction,steering_angle,distance, fahrparcours, sensordaten):
        with open('fahrdaten.txt','a',encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow([speed,direction,steering_angle,distance,datetime.now().replace(microsecond=0), fahrparcours, sensordaten])

    def drive_with_line_follower(self, fahrparcours):
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
        self.save_data(my_car.speed, my_car.direction, my_car.steering_angle, my_car.distance, fahrparcours, self.sensordaten)

        if self.sensordaten[0] > 10 and self.sensordaten[1] > 10 and self.sensordaten[2] > 10 and self.sensordaten[3] > 10 and self.sensordaten[4] > 10:
            self.drive(40,-1)
            self.steering_angle = 45
            self.save_data(my_car.speed, my_car.direction, my_car.steering_angle, my_car.distance, fahrparcours, self.sensordaten)
            time.sleep(0.3)
            if self.sensordaten[0] > 10 and self.sensordaten[1] > 10 and self.sensordaten[2] > 10 and self.sensordaten[3] > 10 and self.sensordaten[4] > 10:
                self.drive(40,1)
                self.save_data(my_car.speed, my_car.direction, my_car.steering_angle, my_car.distance, fahrparcours, self.sensordaten)
                time.sleep(0.5)
            self.drive(40,-1)
            self.steering_angle = 135
            self.save_data(my_car.speed, my_car.direction, my_car.steering_angle, my_car.distance, fahrparcours, self.sensordaten)
            time.sleep(0.3)
            if self.sensordaten[0] > 10 and self.sensordaten[1] > 10 and self.sensordaten[2] > 10 and self.sensordaten[3] > 10 and self.sensordaten[4] > 10:
                self.steering_angle
                self.stop()
                self.save_data(my_car.speed, my_car.direction, my_car.steering_angle, my_car.distance, fahrparcours, self.sensordaten)
                return True
            else:    
                self.drive(40,1)
                self.save_data(my_car.speed, my_car.direction, my_car.steering_angle, my_car.distance, fahrparcours, self.sensordaten)
            

if __name__ == '__main__':
    my_car = SensorCar()
    # print(my_car.line_sensor.test())
    print(my_car.sensordaten)
    
    my_car.drive(40,1) # Volle Fahrt voraus
    my_car.steering_angle = 90 # Räder gerade stellen
    
    while True:
        my_car.drive_with_line_follower()