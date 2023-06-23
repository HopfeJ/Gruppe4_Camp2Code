from sonic_car import SonicCar
import time


my_car = SonicCar()

my_car.drive(50,1)
my_car.save_data(my_car.speed, my_car.direction, my_car.steering_angle, my_car.distance)
while True:
    print(my_car.distance)
    time.sleep(0.2)
    if my_car.distance < 10:
        print(f'Fehlerhaftes ergebnis {my_car.distance}')
        my_car.stop()
        my_car.save_data(my_car.speed, my_car.direction, my_car.steering_angle, my_car.distance)
        break


