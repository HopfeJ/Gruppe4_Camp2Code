from basecar import BaseCar
from basisklassen_cam import Camera
import numpy as np
import cv2 as cv
import time

class CamCar(BaseCar):

    def __init__(self):
        super().__init__()
        self.cam = Camera()

    def make_picture(self):
        img = self.cam.get_frame()
        self.cam.release()
        return img
    
    def save_picture(self, img):
        try:
            cv.imwrite('parcour.png', img)
        except:
            print("Bild konnte nicht gespeichert werden!")

    def load_picture(self, pic_file):
        img = cv.imread(pic_file)
        return img
    
    def show_picture(self, img):
        cv.imshow('image', img)
        cv.waitKey(0)

if __name__ == "__main__":
    my_car = CamCar()
    img = my_car.make_picture()
    my_car.save_picture(img)
    img = my_car.load_picture('parcour.png')
    my_car.show_picture(img)
    
   
    

