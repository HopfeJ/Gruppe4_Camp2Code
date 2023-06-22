import basisklassen
import time

class BaseCar (object):
    
    def __init__(self, ) -> None:
        self.bw = basisklassen.BackWheels()
        self.fw = basisklassen.FrontWheels()
        
        
    def stop(self):
        self.bw.stop()
        
        
    def drive(self,geschwindigkeit: int, fahrrichtung: int):
        if fahrrichtung == 1:
            self.bw.forward()
            
        elif fahrrichtung == -1 :
            self.bw.backward()
            
        elif fahrrichtung == 0 :
            self.bw.stop()
                    
        self.bw.speed = geschwindigkeit
        
    def direction(self,fahrrichtung: int):
        if fahrrichtung == 1:
            self.bw.forward()
            
        elif fahrrichtung == -1 :
            self.bw.backward()
            
        elif fahrrichtung == 0 :
            self.bw.stop()
            
    def speed(self,geschwindigkeit):
        self.bw.speed = geschwindigkeit
        
    def angle(self,richtung: int):
        self.fw.turn(richtung)
        
   
            
class SonicCar(BaseCar):
    
    def __init__(self) -> None:
        self.ultra =basisklassen.Ultrasonic()
        
    
    
    
              
        
car= BaseCar()                      
brot = BaseCar()
modus = {
        1: 'Fahrparcour 1:',
        2: 'Fahrparcour 2:',
        3: 'Fahrparcour 3:',
        9: 'Programm beenden:',
    }


print('Hier kann der Fahrparcour ausgewählt werden:\n')

for m in modus:
    print(f'{m}: {modus[m]}')
    


while True:
    modi = int(input('Gib einen Modus an: \n'))
    
    if modi == 1:
        print('ja ja jetzt gehts los mit dem Fahrparcour 1')
        car.drive(60,1)
        time.sleep(3)
        car.stop()
        time.sleep(1)
        car.drive(60,-1)
        time.sleep(3)
        car.stop()

    if modi == 2:
        print('ja ja jetzt gehts los mit dem Fahrparcour 2')
        car.drive(60,1)
        car.angle(45)
        time.sleep(3)
        car.angle(90)
        car.stop()
        time.sleep(1)
        car.angle(45)
        car.drive(60,-1)
        time.sleep(3)
        car.stop()    
    if modi == 3 :
        print('ja ja jetzt gehts los mit dem Fahrparcour 3')
        brot.drive(60,1)
        time.sleep(5)
        brot.stop()   
        
    elif modi == 9:
        print('Programm wird beendet:')
        break
    
    else:
        print('Getroffene Auswahl nicht möglich.')