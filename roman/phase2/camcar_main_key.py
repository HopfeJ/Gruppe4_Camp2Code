import numpy as np
import cv2 as cv
import matplotlib.pylab as plt
from camcar_new import *
import time


car = CamCar()

#car.drive(25, 1)
car.steering_angle = 90

# Video-Schleife
while True:
    taste = input('Leertaste für weiter, t für Abbruch: ')
    if taste == ' ':
        img = car.get_prep_image()
        line_segments = car.calc_line_segments(img)
        print(line_segments)
        
        if line_segments is not None:
            linien = car.calc_fahrbahnlinien(img, line_segments)
            leitlinie = car.calc_leitlinie(img, linien)
            imageresult = car.draw_line_segments(linien, leitlinie, img)
            lenkwinkel = car.calc_steering_angle(img, linien)
            car.steering_angle = lenkwinkel
            print('gesetzter Lenkwinkel: ', car.steering_angle)
            cv.namedWindow("MeinFenster", cv2.WINDOW_NORMAL)
            cv.resizeWindow("MeinFenster", 800, 600)
            cv.imshow("MeinFenster", imageresult)
            # Ende bei Drücken der Taste q
            if cv.waitKey(1) == ord('q'):
                break
            time.sleep(0.3)
        
        else:
            car.stop()
            car.close()
            print('Stop - Keine Linien mehr erkannt.')
            break
    else:
        print('Abbruch')
        break

car.stop()
car.close()
cv.destroyAllWindows()