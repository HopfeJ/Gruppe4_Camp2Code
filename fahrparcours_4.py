from sonic_car import SonicCar
import time

def fahrparcours_4(my_car):
    my_car.create_data_table()
    zaehler = 0
    while zaehler < 1:
        my_car.drive(50,1)
        my_car.save_data(my_car.speed, my_car.direction, my_car.steering_angle, my_car.distance, 4)
        my_car.distance_schleife(3)
        my_car.drive(80,1)
        my_car.save_data(my_car.speed, my_car.direction, my_car.steering_angle, my_car.distance, 4)
        my_car.distance_schleife(3)
        my_car.drive(50,1)
        my_car.steering_angle = 60
        my_car.save_data(my_car.speed, my_car.direction, my_car.steering_angle, my_car.distance, 4)
        my_car.distance_schleife(2)
        my_car.drive(60,1)
        my_car.steering_angle = 90
        my_car.save_data(my_car.speed, my_car.direction, my_car.steering_angle, my_car.distance, 4)
        my_car.distance_schleife(8)
        zaehler +=1

    if zaehler == 1:
        my_car.stop()  
        my_car.save_data(my_car.speed, my_car.direction, my_car.steering_angle, my_car.distance, 4)


if __name__ == "__main__":
    my_car = SonicCar()
    fahrparcours_4(my_car)      