from base_car import BaseCar
import basisklassen

class SonicCar(BaseCar):
    
    def __init__(self):
        super().__init__()
        self.ultraschall_sensor = basisklassen.Ultrasonic()
        self.__distance = None

    @property
    def distance(self):
        self.__distance = self.ultraschall_sensor.distance()
        return self.__distance

    def save_data(self, distance, speed, direction, steering_angle):
        """
            Diese Daten in einen DataFrame schreiben und in CSV sichern
        """
        pass
        