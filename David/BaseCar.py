import basisklassen
import time

class BaseCar(object):

    def __init__(self):
            self.my_back_wheels = basisklassen.BackWheels()

    def stop(self):
        self.my_back_wheels.stop()

    def drive(self, geschwindigkeit: int, fahrtrichtung: int):

        """

        Argumente:

        geschwindigkeit: ganzzahliger Wert zw. 0(Stop) und 100(Max. Speed)
        fahrtichtung: 1: vorwärts, 0: stop, -1: rückwärts

        """

        self.my_back_wheels.speed = geschwindigkeit
        if fahrtrichtung == 1: 
            self.my_back_wheels.forward()
        elif fahrtrichtung == -1:
            self.my_back_wheels.backward()
        else:
            self.my_back_wheels.stop()

my_car = BaseCar()
my_car.drive(100, 1)
time.sleep(10)
my_car.stop()
