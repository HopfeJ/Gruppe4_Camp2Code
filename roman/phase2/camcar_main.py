import numpy as np
import cv2 as cv
import matplotlib.pylab as plt
from camcar_new import *
import time


car = CamCar()

car.drive(30, 1)
car.steering_angle = 90

# Video-Schleife
while True:
    img = car.get_prep_image()
    line_segments = car.calc_line_segments(img)
    print(line_segments)
    
    if line_segments is not None:
        linien = car.teile_linien(img, line_segments)
        print('Avg Steigung und Schnittpunkt:')
        print(linien)
        leitlinie = car.calc_leitlinie(img, linien)
        imageresult = car.draw_line_segments(linien, leitlinie, img)
        lenkwinkel = car.calc_steering_angle(img, linien)
        car.steering_angle = lenkwinkel
        cv.imshow("Display window (press q to quit)", imageresult)
        # Ende bei Drücken der Taste q
        if cv.waitKey(1) == ord('q'):
            break
        time.sleep(0.3)
    
    else:
        car.stop()
        car.close()
        print('Stop - Keine Linien mehr erkannt.')
        break

car.stop()
car.close()
cv.destroyAllWindows()