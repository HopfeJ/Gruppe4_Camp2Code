from mycar import *

# Hauptprogramms zu mycar.py

# Auto initialisieren:
mycar = BaseCar()


# Fahrparcours #1:
mycar.speed = 50 # das bringt nix
mycar.drive(30, 1)
print(mycar.direction)
print(mycar.speed) # speed über getter abfragen
time.sleep(3)
mycar.stop()



