import basisklassen

class BaseCar():
    """
        Diese Klasse steuert einen Sunfounder PiCar-S Bausatz.
        Die Klasse BaseCar stellt die Fahrbefehle für das Fahrzeug zur Verfügung.
        Zur Nutzung dieser Klasse sind die Klassen BackWheels und FrontWheels aus basisklassen.py erforderlich.

        Attribute:

        direction: int
            Gibt die Fahrtrichtung des Fahrzeuges an 1: vorwärts, 0: stop, -1: rückwärts
        speed: int
            Gibt die Geschwindigkeit des Fahrzeuges an (0-100)
        steering_angle: int
            Gibt den Lenkwinkel des Fahrzeuges an

        Methoden:

        stop(self):
            Stoppt das Fahrzeug
        drive(self, geschwindigkeit: int, fahrtrichtung: int):
            Gibt einen Fahrbefehl an das Fahrzeug
    """

    def __init__(self):
        """
            Im Konstruktor werden 2 Instanzen für die Ansteuerung der Hinterräder (Antriebsräder) und der 
            Vorderräder (Lenkbewegung) erzeugt.
            Außerdem werden die Attribute der Klassen initialisiert

            Attribute:

            direction: int
            Gibt die Fahrtrichtung des Fahrzeuges an 1: vorwärts, 0: stop, -1: rückwärts
            speed: int
                Gibt die Geschwindigkeit des Fahrzeuges an (0-100)
            steering_angle: int
                Gibt den Lenkwinkel des Fahrzeuges an
        """
        self.antriebsraeder = basisklassen.BackWheels()
        self.lenkungsraeder = basisklassen.FrontWheels()
        self.__direction = 0
        self.__speed = 0
        self.__steering_angle = 90

    @property
    def steering_angle(self) -> int: # Getter Methode für Attribut steering_angle
        return self.__steering_angle
    
    @steering_angle.setter
    def steering_angle(self, steering_angle: int):
        """
            Setter Methode für den Lenkwinkel

            Args:
            steering_angle:
                Lenkwinkel des Fahrzeuges (45 - 135 Grad)
        """
        self.__steering_angle = steering_angle
        self.lenkungsraeder.turn(self.__steering_angle)

    def stop(self):
        """
            Die Methode stop hält das Fahrzeug an, indem die Attribute speed und direction auf null gesetzt werden
        """
        self.antriebsraeder.stop()
        self.__speed = 0
        self.__direction = 0

    @property
    def speed(self) -> int: # Getter Methode für Attribut speed
        return self.__speed
    
    @speed.setter
    def speed(self, speed: int):
        """
            Setter Methode für die Geschwindigkeit des Fahrzeuges

            Args:
            speed: int
                Geschwindigkeit des Fahrzeuges (0 - 100)
        """
        self.__speed = speed
        if self.__speed == 0: # Wenn speed null, dann fährt das Auto nicht, also direction = 0
            self.__direction == 0
        elif self.__speed >0 and speed <101 and self.__direction == 0:
            print("Fehlende Fahrtrichtung. Speed auf null gesetzt!")
            self.__speed = 0
        else:
            self.drive(self.__speed, self.__direction)

    @property
    def direction(self) -> int: # Getter Methode für die Fahrtrichtung
        return self.__direction
    
    def drive(self, geschwindigkeit: int, fahrtrichtung: int):
        """
            Die Methode gibt den Fahrbefehl für das Fahrzeug.
            
            Args:
            geschwindigkeit: int
                Ein ganzzahliger Wert zwischen 0 (stop) und 100 (Max-Speed)
            fahrtrichtung: int
                1: vorwärts, 0: stop, -1: rückwärts
        """
        if fahrtrichtung == 1:
            self.__direction = 1
            self.__speed = geschwindigkeit
            self.antriebsraeder.speed = self.__speed
            self.antriebsraeder.forward()
        elif fahrtrichtung == -1:
            self.__direction = -1
            self.__speed = geschwindigkeit
            self.antriebsraeder.speed = self.__speed
            self.antriebsraeder.backward()
        elif fahrtrichtung == 0:
            self.stop()
        else:
            self.__direction == 0
        
       





