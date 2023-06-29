import base_car
import time

def fahrparcours_1(my_car):
    my_car.drive(50,1)
    time.sleep(3)
    my_car.stop()
    time.sleep(1)
    my_car.drive(30,-1)
    time.sleep(3)
    my_car.stop()

if __name__ == "__main__":
    my_car = base_car.BaseCar()
    fahrparcours_1(my_car)