import r_basisklassen
import time


class BaseCar(object):

    def __init__(self) -> None:
        self.bw = r_basisklassen.BackWheels() # BackWheels aus basisklassen.py erzeugen -> die Hinterräder treiben an
        self.fw = r_basisklassen.FrontWheels()
        self.bw.speed = 0

    # Methode zum Anhalten des Autos
    def stop(self):
        self.bw.stop()

    # Setzen und Zugriff auf Geschwindigkeit
    @property
    def speed(self):
        return self.bw._speed

    @speed.setter
    def speed(self, speed):
        self.bw.speed = speed
        
    # Methode zum Setzen von Geschwindigkeit und Fahrtrichtung der Hinterräder
    def drive(self, geschwindigkeit: int, fahrtrichtung: int):
        
        self.speed = geschwindigkeit
        if fahrtrichtung == 1:
            self._direction = 1
            self.bw.forward()
        elif fahrtrichtung == -1:
            self._direction = -1
            self.bw.backward()
        else:
            self._direction = 0
            self.bw.stop()

    def lenken(self, angle: int):
        self.fw.turn(angle)
        
    def lenktest(self):
        self.fw.test()

    # Zugriff auf die Fahrtrichtung erhalten 
    @property
    def direction(self):
        return self._direction
    
    # steering_angle: Setzen und Zugriff auf Lenkwinkel
    @property
    def steering_angle(self):
        return self._steering_angle
    
    @steering_angle.setter
    def steering_angle(self, angle):
        self._steering_angle = angle












