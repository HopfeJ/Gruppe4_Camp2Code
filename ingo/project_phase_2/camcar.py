from basecar import BaseCar
from basisklassen_cam import Camera
from steering_controller_classic import SteeringController
import numpy as np
import cv2 as cv
from time import sleep

class CamCar(BaseCar):

    def __init__(self, steering_controller):
        super().__init__()
        self.steering_controller = steering_controller
        self.stop_it = False

    def make_picture(self) -> np.array:
        cam = Camera()
        img = cam.get_frame()
        cam.release()
        return img
    
    def save_picture(self, img: np.array):
        try:
            cv.imwrite('parcour.png', img)
        except:
            print("Bild konnte nicht gespeichert werden!")

    def load_picture(self, pic_file) -> np.array:
        img = cv.imread(pic_file)
        return img
    
    def show_picture(self, img):
        cv.imshow('image', img)
        if cv.waitKey(1) == ord('q'):
            self.stop_it = True

    def prepare_picture(self, img) -> np.array:
        img_cut = img[170:380,50:600].copy() # Erste Koordinaten y-Achse von oben nach unten, Zweite Koordinaten X-Achse von links nach rechts
        return img_cut
    
    def run(self):
        while True:
            if self.stop_it:
                break
            img = self.make_picture()
            prepared_img = self.prepare_picture(img)
            transformed_img, lines_left_lane_boundary_y1_mean, lines_right_lane_boundary_y1_mean = self.steering_controller.classic_hough_transformation(prepared_img)
            self.show_picture(transformed_img)
            steering_order = self.steering_controller.steering_direction(lines_left_lane_boundary_y1_mean, lines_right_lane_boundary_y1_mean)
            self.drive(30, 1)
            self.steering_angle = steering_order
            sleep(0.5)
            self.steering_angle = 90
            print(steering_order, lines_left_lane_boundary_y1_mean, lines_right_lane_boundary_y1_mean)
        self.stop()

if __name__ == "__main__":
    my_car = CamCar(SteeringController(np.array([90, 0, 0]), np.array([150, 255, 255])))
    my_car.run()

    
   
    

