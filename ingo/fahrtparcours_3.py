import base_car
import sonic_car
import os
import time

os.chdir("/home/pi/Gruppe4_Camp2Code/ingo")


my_car = sonic_car.SonicCar()

def fahrparcours_3(my_car):
    my_car.drive(40,1)
    my_car.save_data(my_car.speed, my_car.direction, my_car.steering_angle, my_car.distance)

    while True:
        distance = my_car.distance
        print(distance)
        time.sleep(0.2)
        if distance < 15 and distance >0:
            break

    my_car.stop()
    my_car.save_data(my_car.speed, my_car.direction, my_car.steering_angle, my_car.distance)

if __name__ == "__main__":
    fahrparcours_3(my_car)