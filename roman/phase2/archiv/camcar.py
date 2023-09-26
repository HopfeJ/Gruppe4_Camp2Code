from basecar import BaseCar
from basisklassen_cam import *


class CamCar(BaseCar):
    
    def __init__(self, camera, config: str = "config.json"):
        super().__init__(config)
        self.__camera = camera # hier wird ein Camera-Objekt übergeben
        
    def get_frame(self):
        return self.__camera.get_frame()

    def release(self):
        self.__camera.release()
    
    