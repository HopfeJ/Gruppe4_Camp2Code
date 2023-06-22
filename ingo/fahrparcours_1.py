import base_car
import time

my_car = base_car.BaseCar()

def fahrparcours_1(my_car):
    my_car.drive(50,1)
    time.sleep(3)
    my_car.stop()
    time.sleep(1)
    my_car.drive(50,-1)
    time.sleep(3)
    my_car.stop()

if __name__ == "__main__":
    fahrparcours_1(my_car)