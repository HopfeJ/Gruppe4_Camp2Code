import time
from sensor_car import SensorCar


def fahrparcours_5(my_car):
    my_car.create_data_table()
    my_car.drive(40,1) # Volle Fahrt voraus
    my_car.steering_angle = 90 # Räder gerade stellen
    while True:
        fertig = my_car.drive_with_line_follower(5)
        if fertig:
            break

if __name__ == "__main__":
    my_car = SensorCar()
    fahrparcours_5(my_car)  
    

