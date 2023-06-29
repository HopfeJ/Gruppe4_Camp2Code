from sonic_car import SonicCar
import time

def fahrparcours_3(my_car):
    my_car.create_data_table()
    my_car.drive(50,1)
    my_car.save_data(my_car.speed, my_car.direction, my_car.steering_angle, my_car.distance, 3)
    while True:
        distance = my_car.distance
        # print(distance)
        time.sleep(0.2)
        if distance < 15 and distance > 0:
            print(f'Ergebnis Stop (Abstand Hindernis) {distance}')
            my_car.stop()
            my_car.save_data(my_car.speed, my_car.direction, my_car.steering_angle, distance, 3)
            break


if __name__ == "__main__":
    my_car = SonicCar()
    fahrparcours_3(my_car)