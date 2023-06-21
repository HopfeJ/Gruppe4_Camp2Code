import basisklassen

class BaseCar():

    def __init__(self):
        self.bw = basisklassen.BackWheels()
        self.__direction = 0

    @property
    def direction(self):
        return self.__direction
    
    def stop(self):
        self.bw.stop()

    def drive(self, geschwindigkeit: int, fahrtrichtung: int):
        """
            Args:

            geschwindigkeit: Ein ganzzahliger Wert zwischen 0 (stop) und 100 (Max-Speed)
            fahrtrichtung: 1: vorwärts, 0: stop, -1: rückwärts
        """
        self.bw.speed = geschwindigkeit
        if fahrtrichtung == 1:
            self.__direction = 1
            self.bw.forward()
        elif fahrtrichtung == -1:
            self.bw.backward()
            self.__direction == -1
        else:
            self.stop()





