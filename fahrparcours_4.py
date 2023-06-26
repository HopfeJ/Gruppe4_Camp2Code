from sonic_car import SonicCar
import time


my_car = SonicCar()


def fahrparcours_4(my_car):
    zaehler = 5
    while zaehler < 5:
        my_car.drive(50,1)
        my_car.save_data(my_car.speed, my_car.direction, my_car.steering_angle, my_car.distance)
        my_car.distance_schleife(3)
        my_car.drive(80,1)
        my_car.save_data(my_car.speed, my_car.direction, my_car.steering_angle, my_car.distance)
        my_car.distance_schleife(3)
        my_car.drive(50,1)
        my_car.steering_angle = 60
        my_car.save_data(my_car.speed, my_car.direction, my_car.steering_angle, my_car.distance)
        my_car.distance_schleife(2)
        my_car.drive(60,1)
        my_car.steering_angle = 90
        my_car.save_data(my_car.speed, my_car.direction, my_car.steering_angle, my_car.distance)
        my_car.distance_schleife(8)
        zaehler +=1

    if zaehler == 5:
        my_car.stop()  



if __name__ == "__main__":
    fahrparcours_4(my_car)      