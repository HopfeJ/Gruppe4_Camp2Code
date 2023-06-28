import base_car
import time



def fahrparcours_2(my_car):
    my_car.drive(50,1) # Vorwärts
    time.sleep(1)
    my_car.steering_angle = 135 # Rechts
    time.sleep(8)
    my_car.stop()
    time.sleep(1)
    my_car.steering_angle = 135 # Rechts
    my_car.drive(50,-1) # Rückwärts
    time.sleep(8)
    my_car.steering_angle = 90 # Gerade
    time.sleep(1)
    my_car.stop()

    my_car.drive(50,1) # Vorwärts
    time.sleep(1)
    my_car.steering_angle = 45 # Links
    time.sleep(8)
    my_car.stop()
    time.sleep(1)
    my_car.steering_angle = 45 # Links
    my_car.drive(50,-1) # Rückwärts
    time.sleep(8)
    my_car.steering_angle = 90 # Gerade
    time.sleep(1)
    my_car.stop()
    
if __name__ == "__main__":
    my_car = base_car.BaseCar()
    fahrparcours_2(my_car)