from basecar import BaseCar
from basisklassen_cam import Camera
import cv2 as cv
import numpy as np

class CamCar(BaseCar):
    
    def __init__(self):
        super().__init__()
        self.cam = Camera()

    def make_picture(self):
        img = self.cam.get_frame()
        return img

    def prepare_picture(self, img):
        img_cut = img[80:380, 30:610] # Y-Achse, X-Achse
        img_cut_hsv = cv.cvtColor(img_cut, cv.COLOR_BGR2HSV)
        return img_cut_hsv
    
    def calculate_angle_from_picture(self, img):
        # Farbfilter anwenden
        lower = np.array([95, 0, 0])
        upper = np.array([125, 255, 255])
        image_mask = cv.inRange(img, lower, upper)
        self.show_picture(image_mask)

    def show_picture(self, img):
        window = "Picture Viewer (press q to quit)"
        cv.imshow(window, img)
        key = cv.waitKey(0)
        if key == ord("q"):
            cv.destroyWindow(window) 

    def run(self):
        # Bild machen
        img = self.make_picture()
        # Bild schneiden und colorieren
        prepared_image = self.prepare_picture(img)
        # Bild übergeben und Steuerwinkel zurückgeben
        self.calculate_angle_from_picture(prepared_image)
        # Winkel setzen und Auto fahren lassen


if __name__ == "__main__":
    my_car = CamCar()
    my_car.run()
