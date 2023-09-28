from basecar import BaseCar


car = BaseCar()
turn_offset = input('Offset: ')
while True:
    angle = input('Neuer Angle, Leertaste Abbruch: ')
    if angle != ' ':
        new = int(angle) + int(turn_offset)
        print('Aktueller Angle: ', car.steering_angle)
        print(f'Neuer Angle {int(new)} wird gesetzt...')
        car.steering_angle = int(new)
        print('Neuer Angle gesetzt.')
        print('Abfrage gesetzter Angle: ', car.steering_angle)
    else:
        print('Abbruch.')
        break
        

