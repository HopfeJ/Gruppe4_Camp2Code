from BaseCar import BaseCar
import basisklassen

class SonicCar(BaseCar):
    def __init__(self):
        super().__init__()
        self.ultraschall = basisklassen.Ultrasonic() #jan
        self.__abstand = self.ultraschall.distance() #roman
    def distance(self):
        abstand = self.ultraschall.distance

        print(abstand)

    @property
    def abstand(self): # getter methode für abstand
        return self.__abstand

#y_car = SonicCar()
#my_car.abstand