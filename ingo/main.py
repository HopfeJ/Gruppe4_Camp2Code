import base_car as base_car
import time

my_car = base_car.BaseCar()

my_car.speed = 50
print(my_car.speed)
my_car.drive(40, 1)
print(my_car.speed)
time.sleep(1)
my_car.drive(100,0)
print(my_car.speed)
time.sleep(1)
my_car.speed = 100
print(my_car.speed)

time.sleep(3.5)
my_car.stop()