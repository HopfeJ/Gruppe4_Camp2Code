import BaseCar
import time
#import SonicCar

my_car = BaseCar.BaseCar
#my_car = SonicCar.SonicCar()

# my_car.speed = 50
# print(my_car.speed)
# time.sleep(3)
# my_car.drive(40, 1)
# print(my_car.speed)
# time.sleep(3)
# my_car.drive(100, 1)
# print(my_car.speed)
# time.sleep(3.5)
# my_car.stop()
# my_car.steering_angle = 110
for i in range(100):
    my_car.steering_angle = 90
    time.sleep(1)

#print(my_car.abstand)