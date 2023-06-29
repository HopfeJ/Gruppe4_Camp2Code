from mycar import *
from datetime import datetime
import os

os.chdir("/home/pi/Gruppe4_Camp2Code/roman")

# Hauptprogramms zu mycar.py

# Auto initialisieren:
mycar = BaseCar()
mycar2 = SonicCar()

def fahrparcours1(mycar):
    # Fahrparcours 1 ‑ Vorwärts und Rückwärts: 
    # Das Auto fährt mit langsamer Geschwindig‑
    # keit 3 Sekunden geradeaus, stoppt für 1 Sekunde 
    # und fährt 3 Sekunden rückwärts.

    mycar.drive(30,1)
    time.sleep(3)
    mycar.stop()
    time.sleep(1)
    mycar.drive(30,-1)
    time.sleep(3)
    mycar.stop()


def fahrparcours2(mycar):

    # Fahrparcours 2 ‑ Kreisfahrt mit maximalem Lenkwinkel: Das Auto fährt 1 Sekunde ge‑
    # radeaus, dann für 8 Sekunden mit maximalen Lenkwinkel im Uhrzeigersinn und stoppt.
    # Dann soll das Auto diesen Fahrplan in umgekehrter Weise abfahren und an den Ausgangs‑
    # punkt zurückkehren. Die Vorgehensweise soll für eine Fahrt im entgegengesetzten Uhrzei‑
    # gersinn wiederholt werden.

    mycar.steering_angle = 90
    print(mycar.steering_angle)
    mycar.drive(30,1)
    time.sleep(1)
    
    # Kreisfahrt
    mycar.steering_angle = 135
    print(mycar.steering_angle)
    # setzt vor Ablauf der 8 sek, selbständig wieder auf 90, aber ohne meinen offset, also leicht nach rechts versetzt
    # und auch nach ende scheinbar willkürliche lenkausschläge in beide richtungen
    time.sleep(8)
    mycar.stop()
    print(mycar.steering_angle)
    
    # Farhtrichtung umkehren
    #mycar.steering_angle = 45
    print(mycar.steering_angle)
    mycar.drive(30,-1)
    time.sleep(8)
    mycar.stop()

def fahrparcours3(mycar2):
    # Vorwärtsfahrt bis Hindernis
    # Fahrdaten sollen während Fahrt aufgezeichnet werden:
    # Geschwindigkeit, Lenkwinkel, Fahrtrichtung, Sensordaten

    # Logging in ein csv-file
    # schleife für regelmäßige abfrage sensor
    # reaktion auto in abhängigkeit sensor
    # pro schleinfendurchlauf, parameter mal speichern
    # was soll gespeichert werden: alte parameter, oder neuer parameter ...

    mycar2.drive(30, 1)
    mycar2.log_data(datetime.now(), mycar2.speed, mycar2.direction, mycar2.steering_angle, mycar2.last_distance_measured, "start_driving")
    mycar2.measure_distance() 

    
def fahrparcours4(mycar2):

    # Auto soll während laufender Fahrt Speed und Direction verändern können
    mycar2.drive(random.randint(30,100), 1)
    print("speed aktuell", mycar2.speed)
    print("direction aktuell", mycar2.direction)
    mycar2.log_data(mycar2.zeitstempel(), mycar2.speed, mycar2.direction, mycar2.steering_angle, mycar2.last_distance_measured, "start_driving")
    mycar2.measure_distance(20)

def test(mycar):
    # test
    print("Speed auf 50 für 3 sek setzen")
    print(f"Direction vor Setzen über setter: {mycar.direction}")
    mycar.speed = 50 # speed mit property-setter setzen
    print(f"Direction nach Setzen über setter: {mycar.direction}")
    print(f"Speed: {mycar.speed}") # speed über getter abfragen
    # print(f"Steering angle vor lenken: {mycar.steering_angle}")
    # mycar.steering_angle = 45
    # print(f"Steering angle nach lenken: {mycar.steering_angle}")
    time.sleep(3)

    print("drive aufrufen mit 30, 1 für 3 sek")
    mycar.drive(30, 1)
    print(f"Direction: {mycar.direction}")
    print(f"Speed: {mycar.speed}") # speed über getter abfragen
    time.sleep(3)

    print("Speed auf 70 für 3 sek setzen")
    print(f"Direction vor Setzen über setter: {mycar.direction}")
    mycar.speed = 70 # speed mit property-setter setzen
    print(f"Direction nach Setzen über setter: {mycar.direction}")
    print(f"Speed: {mycar.speed}") # speed über getter abfragen
    time.sleep(3)

    print("drive aufrufen mit 50, 0 für 3 sek")
    mycar.drive(50, 0)
    print(f"Direction: {mycar.direction}")
    print(f"Speed: {mycar.speed}") # speed über getter abfragen
    time.sleep(3)

    print("drive aufrufen mit 70, -1 für 3 sek")
    mycar.drive(70, -1)
    print(f"Direction: {mycar.direction}")
    print(f"Speed: {mycar.speed}") # speed über getter abfragen
    time.sleep(3)

    print("Speed auf 100 für 3 sek setzen")
    print(f"Direction vor Setzen über setter: {mycar.direction}")
    mycar.speed = 100 # speed mit property-setter setzen
    print(f"Direction nach Setzen über setter: {mycar.direction}")
    print(f"Speed: {mycar.speed}") # speed über getter abfragen
    time.sleep(3)

    print("stop")
    mycar.stop()
    print(f"Direction: {mycar.direction}")
    print(f"Speed: {mycar.speed}") # speed über getter abfragen

# Main:

#fahrparcours2(mycar)
#fahrparcours4(mycar2)

mycar3 = SensorCar()
mycar3.drive(30,1)
time.sleep(3)
mycar3.stop()
