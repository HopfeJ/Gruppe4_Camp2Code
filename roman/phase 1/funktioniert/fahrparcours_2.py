import base_car
import time

my_car = base_car.BaseCar()

def fahrparcours_2(my_car):
    my_car.drive(50,1)
    time.sleep(1)
    my_car.steering_angle = 135
    time.sleep(8)
    my_car.stop()
    time.sleep(1) #kurzer stopp (visualisierung)
    my_car.drive(50,-1)
    my_car.steering_angle = 135
    time.sleep(8)
    my_car.steering_angle = 90
    time.sleep(1)
    my_car.stop()

    my_car.drive(50,1)
    time.sleep(1)
    my_car.steering_angle = 45
    time.sleep(8)
    my_car.stop()
    time.sleep(1) #kurzer stopp (visualisierung)
    my_car.drive(50,-1)
    my_car.steering_angle = 45
    time.sleep(8)
    my_car.steering_angle = 90
    time.sleep(1)
    my_car.stop()

if __name__ == "__main__":
    fahrparcours_2(my_car)



