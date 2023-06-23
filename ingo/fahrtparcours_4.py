from sonic_car import SonicCar
import os
import time

os.chdir("/home/pi/Gruppe4_Camp2Code/ingo")

my_car = SonicCar()

my_car.drive(40,1)
my_car.save_data(my_car.speed, my_car.direction, my_car.steering_angle, my_car.distance)

while True:
    distance = my_car.distance
    print(distance)
    if distance < 15 and distance >0:
        my_car.stop()
        my_car.steering_angle = 135
        my_car.save_data(my_car.speed, my_car.direction, my_car.steering_angle, my_car.distance)
        my_car.drive(40,-1)
        my_car.save_data(my_car.speed, my_car.direction, my_car.steering_angle, my_car.distance)
        time.sleep(2)
        my_car.steering_angle = 90
        my_car.save_data(my_car.speed, my_car.direction, my_car.steering_angle, my_car.distance)
        my_car.drive(40,1)
        my_car.save_data(my_car.speed, my_car.direction, my_car.steering_angle, my_car.distance)
