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



