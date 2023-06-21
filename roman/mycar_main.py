from mycar import *
import time

# Hauptprogramms zu mycar.py

# Auto initialisieren:
mycar = BaseCar()


# Fahrparcours #1:
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



