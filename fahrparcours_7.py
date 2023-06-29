import time
from sensor_car import SensorCar


def fahrparcours_7(my_car):
    my_car.create_data_table()
    my_car.drive(40,1) # Volle Fahrt voraus
    my_car.steering_angle = 90 # Räder gerade stellen
    while True:
        fertig = my_car.drive_with_line_follower(7)
        if fertig:
            break
        if my_car.distance < 15 and my_car.distance > 0:
            print(f'Ergebnis Stop (Abstand Hindernis) {my_car.distance}')
            my_car.stop()
            my_car.save_data(my_car.speed, my_car.direction, my_car.steering_angle, my_car.distance, 3, my_car.sensordaten)
            break
        
if __name__ == "__main__":
    my_car = SensorCar()
    fahrparcours_7(my_car)  