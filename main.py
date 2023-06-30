import base_car
import sonic_car
import sensor_car
import fahrparcours_1
import fahrparcours_2
import fahrparcours_3
import fahrparcours_4
import fahrparcours_5
import fahrparcours_6
import fahrparcours_7

"""
Dieses Programm ermöglicht die Auswahl und Ausführung verschiedener Fahrparcours für das SunFounder-Auto.

Das Programm importiert die Module base_car, sonic_car, sensor_car sowie die verschiedenen Fahrparcours-Module
(fahrparcours_1, fahrparcours_2, fahrparcours_3 usw.).

Es werden drei Fahrzeugobjekte erstellt: 
    moehre (von der Klasse BaseCar), 
    moehre_mit_abstandsmesser (von der Klasse SonicCar) und 
    luxusschlitten (von der Klasse SensorCar).

Der Benutzer wird durch ein Menü aufgefordert, eine Option auszuwählen. 
Je nach Auswahl wird der entsprechende Fahrparcours für das entsprechende Fahrzeug gestartet.

Optionen:
    1 - Fahrparcours 1 starten
    2 - Fahrparcours 2 starten
    3 - Fahrparcours 3 starten
    4 - Fahrparcours 4 starten
    5 - Fahrparcours 5 starten
    6 - Fahrparcours 6 starten
    7 - Fahrparcours 7 starten
    x - Programm beenden

Das Programm läuft in einer Endlosschleife, bis der Benutzer die Option "x" wählt, um das Programm zu beenden.
Bei einer falschen Eingabe wird eine entsprechende Meldung ausgegeben.

"""


moehre = base_car.BaseCar()
moehre_mit_abstandsmesser = sonic_car.SonicCar()
luxusschlitten = sensor_car.SensorCar()


print("-----------------------------------------")
print(" 1 - Fahrparcours 1 starten ")
print(" 2 - Fahrparcours 2 starten ")
print(" 3 - Fahrparcours 3 starten ")
print(" 4 - Fahrparcours 4 starten ")
print(" 5 - Fahrparcours 5 starten ")
print(" 6 - Fahrparcours 6 starten ")
print(" 7 - Fahrparcours 7 starten ")
print(" x - Programm beenden")
print("-----------------------------------------")
while True:
    eingabe = input("Bitte wählen sie eine Option: ")
    if eingabe == "1":
        fahrparcours_1.fahrparcours_1(moehre)
    elif eingabe == "2":
        fahrparcours_2.fahrparcours_2(moehre)
    elif eingabe == "3":
        fahrparcours_3.fahrparcours_3(moehre_mit_abstandsmesser)
    elif eingabe == "4":
        fahrparcours_4.fahrparcours_4(moehre_mit_abstandsmesser)
    elif eingabe == "5":
        fahrparcours_5.fahrparcours_5(luxusschlitten)
    elif eingabe == "6":
        fahrparcours_6.fahrparcours_6(luxusschlitten)
    elif eingabe == "7":
        fahrparcours_7.fahrparcours_7(luxusschlitten)
    elif eingabe == "x" or "X":
        break
    else:
        print("Falsche Eingabe !")



