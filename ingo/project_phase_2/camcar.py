from basecar import BaseCar
from basisklassen_cam import Camera
from steering_controller_classic import SteeringController
import numpy as np
import cv2 as cv

class CamCar(BaseCar):

    def __init__(self, steering_controller):
        super().__init__()
        self.cam = Camera()
        self.steering_controller = steering_controller

    def make_picture(self) -> np.array:
        img = self.cam.get_frame()
        self.cam.release()
        return img
    
    def save_picture(self, img):
        try:
            cv.imwrite('parcour.png', img)
        except:
            print("Bild konnte nicht gespeichert werden!")

    def load_picture(self, pic_file) -> np.array:
        img = cv.imread(pic_file)
        return img
    
    def show_picture(self, img):
        cv.imshow('image', img)
        cv.waitKey(0)

    def prepare_picture(self, img) -> np.array:
        img_cut = img[170:380,50:600].copy()
        return img_cut
    
    def run(self):
        img = self.make_picture()
        prepared_img = self.prepare_picture(img)
        transformed_img = self.steering_controller.classic_hough_transformation(prepared_img)
        self.show_picture(transformed_img)
            

if __name__ == "__main__":
    my_car = CamCar(SteeringController(np.array([90, 0, 0]), np.array([150, 255, 255])))
    my_car.run()
    
   
    

