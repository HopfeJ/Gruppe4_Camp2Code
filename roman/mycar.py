import r_basisklassen
import time


class BaseCar(object):

    def __init__(self) -> None:
        self.bw = r_basisklassen.BackWheels() # BackWheels aus basisklassen.py erzeugen -> die Hinterräder treiben an
        self.fw = r_basisklassen.FrontWheels()

    # Methode zum Anhalten des Autos
    def stop(self):
        self.bw.stop()
        
    # Methode zum Setzen von Geschwindigkeit und Fahrtrichtung der Hinterräder
    def drive(self, geschwindigkeit: int, fahrtrichtung: int):
        self.bw.speed = geschwindigkeit
        if fahrtrichtung == 1:
            self.bw.forward()
        elif fahrtrichtung == -1:
            self.bw.backward()
        else:
            self.bw.stop()

    def lenken(self, angle: int):
        self.fw.turn(angle)
        
    def lenktest(self):
        self.fw.test()

    # Zugriff auf die Fahrtrichtung (1: vorwärts, 0: Stillstand, -1: Rückwärts)    
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

    # Setzen und Zugriff auf Geschwindigkeit
    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        self._speed = speed


# Hauptprogramms
# Auto initialisieren:
mycar = BaseCar()

# Fahrparcours #1 aus Lastenheft
def fahrparcours1(speed, richtung, dauer):
    mycar.drive(speed, richtung)
    
    time.sleep(dauer)
    mycar.stop()

#fahrparcours1(30, 1, 10)
#mycar.steering_angle = 90
#print(mycar.steering_angle)





