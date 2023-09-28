import numpy as np
import cv2 as cv
import matplotlib.pylab as plt
from camcar_new import *
import time


car = CamCar()

car.drive(30, 1) # fährt bis 40
car.steering_angle = 90

# Video-Schleife
counter = 0
while True:
    img = car.take_picture()
    resized_img = car.resize_image(img, 100,370,0,640)
    prep_img = car.get_prep_image(resized_img)
    line_segments = car.calc_line_segments(prep_img)
    #print(line_segments)
    
    if line_segments is not None:
        linien = car.calc_fahrbahnlinien(prep_img, line_segments)
        leitlinie = car.calc_leitlinie(prep_img, linien)
        imageresult = car.draw_line_segments(linien, leitlinie, prep_img)
        aktueller_lenkwinkel = car.steering_angle
        errechneter_lenkwinkel = car.calc_steering_angle_from_cam(prep_img, linien)
        print('aktueller Lenkwinkel:', aktueller_lenkwinkel, type(aktueller_lenkwinkel))
        print('errechneter Lenkwinkel: ', errechneter_lenkwinkel, type(aktueller_lenkwinkel))

        car.steering_angle = errechneter_lenkwinkel
        print('gesetzter Lenkwinkel: ', car.steering_angle)
        cv.namedWindow("MeinFenster", cv2.WINDOW_NORMAL)
        cv.resizeWindow("MeinFenster", 800, 600)
        cv.imshow("MeinFenster", imageresult)
        # Ende bei Drücken der Taste q
        if cv.waitKey(1) == ord('q'):
            break
        time.sleep(0.05)
        if counter > 3: # nur alle 10 Durchläufe Bild speichern
            car.save_with_date(img, errechneter_lenkwinkel)
            counter = 0

        counter +=1 
    
    else:
        car.stop()
        car.close()
        print('Stop - Keine Linien mehr erkannt.')
        break

car.stop()
car.close()
cv.destroyAllWindows()