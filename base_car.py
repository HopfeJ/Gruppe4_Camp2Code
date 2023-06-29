import basisklassen

class BaseCar():

    def __init__(self):
        self.antriebsraeder = basisklassen.BackWheels()
        self.lenkungsraeder = basisklassen.FrontWheels()
        self.__direction = 0
        self.__speed = 0
        self.__steering_angle = 90

    @property
    def steering_angle(self):
        return self.__steering_angle
    
    @steering_angle.setter
    def steering_angle(self, steering_angle):
        self.__steering_angle = steering_angle
        self.lenkungsraeder.turn(self.__steering_angle)

    def stop(self):
        self.antriebsraeder.stop()
        self.__speed = 0
        self.__direction = 0

    @property
    def speed(self): # Getter Methode für Attribut speed
        return self.__speed
    
    @speed.setter
    def speed(self, speed):
        self.__speed = speed
        if self.__speed == 0: # Wenn speed null, dann fährt das Auto nicht, also direction = 0
            self.__direction == 0
        elif self.__speed >0 and speed <101 and self.__direction == 0:
            print("Fehlende Fahrtrichtung. Speed auf null gesetzt!")
            self.__speed = 0
        else:
            self.drive(self.__speed, self.__direction)

    @property
    def direction(self):
        return self.__direction
    
    @direction.setter
    def direction(self, new_direction):
        self.__direction = new_direction
    
    def drive(self, geschwindigkeit: int, fahrtrichtung: int):
        """
            Args:

            geschwindigkeit: Ein ganzzahliger Wert zwischen 0 (stop) und 100 (Max-Speed)
            fahrtrichtung: 1: vorwärts, 0: stop, -1: rückwärts
        """
        if fahrtrichtung == 1:
            self.direction = fahrtrichtung
            self.__speed = geschwindigkeit
            self.antriebsraeder.speed = self.__speed
            self.antriebsraeder.forward()
        elif fahrtrichtung == -1:
            self.direction = fahrtrichtung
            self.__speed = geschwindigkeit
            self.antriebsraeder.speed = self.__speed
            self.antriebsraeder.backward()
        elif fahrtrichtung == 0:
            self.stop()
        else:
            self.__direction == 0
            return
            
        
        
       





