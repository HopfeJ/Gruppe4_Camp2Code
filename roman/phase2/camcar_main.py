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
        lane_lines = car.average_slope_intercept(img, line_segments)
        print('average_slope_intercept:')
        print(lane_lines)
        fahrlinie = car.calc_fahrlinie(img, lane_lines)
        imageresult = car.draw_line_segments(lane_lines, fahrlinie, img)
        lenkwinkel = car.compute_steering_angle(img, lane_lines)
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