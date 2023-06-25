import r_basisklassen
import time
import csv
from datetime import datetime
import random
import os

os.chdir("/home/pi/Gruppe4_Camp2Code/roman")



class BaseCar(object):

    def __init__(self) -> None:
        self.bw = r_basisklassen.BackWheels() # BackWheels aus basisklassen.py erzeugen -> die Hinterräder treiben an
        self.fw = r_basisklassen.FrontWheels() # -30 scheint zu passen. wurde in r_Basisklassen bereits gesetzt.
        self.bw.speed = 0
        self._direction = 0
        self._steering_angle = 90

    # Methode zum Anhalten des Autos
    def stop(self):
        self.bw.stop()
        self._speed = 0
        self._direction = 0

    # Methode zum Setzen von Geschwindigkeit und Fahrtrichtung der Hinterräder
    def drive(self, geschwindigkeit: int, fahrtrichtung: int):
        
        self.speed = geschwindigkeit
        self.set_direction(fahrtrichtung)

    def set_direction(self, new_direction):
        if new_direction == 1:
            self._direction = 1
            return self.bw.forward()
        elif new_direction == -1:
            self._direction = -1
            return self.bw.backward()
        else:
            self._direction = 0
            return self.bw.stop()

    # Zugriff auf die Fahrtrichtung erhalten 
    @property
    def direction(self):
        return self._direction
    
    @direction.setter
    def direction(self, new_direction):
        self.set_direction(new_direction)
        
    # Setzen und Zugriff auf Geschwindigkeit
    @property
    def speed(self):
        return self.bw._speed
       
    @speed.setter # setzt nur speed, direction bleibt so wie es vorher mal war
    def speed(self, new_speed):
            self.bw.speed = new_speed
            #self.last_speed_set = new_speed
    
    # steering_angle: Setzen und Zugriff auf Lenkwinkel
    @property
    def steering_angle(self):
        return self._steering_angle
    
    @steering_angle.setter
    def steering_angle(self, angle):
        self._steering_angle = angle
        self.fw.turn(angle)


class SonicCar(BaseCar):

    def __init__(self) -> None:
        super().__init__()
        self.sonic_sensor = r_basisklassen.Ultrasonic()
        self.__last_distance_measured = self.sonic_sensor.distance()

    @property   
    def last_distance_measured(self):
        return self.__last_distance_measured
    
    def get_distance(self):
        self.__last_distance_measured = self.sonic_sensor.distance()
        self.sonic_sensor.stop()
        return self.__last_distance_measured
    
    #Schleife neu für Fahrparcours4
    def measure_distance(self):
        while True:
            abstand = self.get_distance()
            time.sleep(0.2)
            print(abstand)
            if abstand < 0:
                print(f"Sensor-Fehler #{abstand}")
                self.log_data(datetime.now(), self.speed, self.direction, self.steering_angle, self.last_distance_measured, "supersonic_sensor_error")
            elif abstand < 10: # Hinderniss erkannt:
                #self.stop()
                print("Hinderniss erkannt!")
                self.log_data(datetime.now(), self.speed, self.direction, self.steering_angle, self.last_distance_measured, "Hinderniss")
                
                print("zurücksetzen")
                self.direction = -1 # Rückwärtsgang
                self.speed = 30
                left_or_right = random.randint(1, 2)
                if left_or_right == 1:
                    self.steering_angle = 135 # max. Lenkeinschlag setzen
                else:
                    self.steering_angle = 45
                self.log_data(datetime.now(), self.speed, self.direction, self.steering_angle, self.last_distance_measured, "set_back")
                time.sleep(3)
                
                print("weiterfahren")
                self.direction = 1 # wieder Vorwärts
                self.speed = 50
                self.steering_angle = 90 # wieder gerade aus
                self.log_data(datetime.now(), self.speed, self.direction, self.steering_angle, self.last_distance_measured, "continue_driving")
                #break
        self.sonic_sensor.stop()
        #self.stop()

    # #Schleife ALT:
    # def BAKUP_measure_distance(self):
    #     while True:
    #         abstand = self.get_distance()
    #         time.sleep(0.2)
    #         print(abstand)
    #         if abstand < 0:
    #             print(f"Sensor-Fehler #{abstand}")
    #             self.log_data(datetime.now(), self.speed, self.direction, self.steering_angle, self.last_distance_measured, "supersonic_sensor_error")
    #         elif abstand < 10: # Hinderniss erkannt:
    #             self.sonic_sensor.stop()
    #             self.stop()
    #             self.log_data(datetime.now(), self.speed, self.direction, self.steering_angle, self.last_distance_measured, "low_distance_stop")
    #             print("Auto gestoppt: Distance < 10.")
    #             break
    #     self.sonic_sensor.stop()
    #     #self.stop()

    def log_data(self, zeit, speed, direction, steering_angle, distance, reason):
        with open('roman_fahrdaten.txt','a',encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow([zeit, speed, direction, steering_angle, distance, reason])