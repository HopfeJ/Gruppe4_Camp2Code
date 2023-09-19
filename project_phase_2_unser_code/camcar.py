from basecar import BaseCar
from basisklassen_cam import Camera
import numpy as np
import cv2
import time

class CamCar(BaseCar):

    def __init__(self):
        super().__init__()
    

if __name__ == "__main__":
    # cam = Camera()
    # while True:
    #     img = cam.get_frame()
    #     cv2.imshow('image', img)
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break
    # cam.release()
    # print(' - camera released')
    # cv2.destroyAllWindows()
    myCar = CamCar()
    myCar.drive(40,1)
    time.sleep(3)
    myCar.stop()

