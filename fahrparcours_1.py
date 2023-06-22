import BaseCar
import time

my_car = BaseCar.BaseCar()

def fahrparcours_1(my_car):
    my_car.drive(50,1)
    time.sleep(3)
    my_car.stop()
    time.sleep(1)
    my_car.drive(30,-1)
    time.sleep(3)
    my_car.stop()

if __name__ == "__main__":
    fahrparcours_1(my_car)