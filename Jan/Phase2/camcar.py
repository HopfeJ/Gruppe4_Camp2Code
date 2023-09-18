from basecar import BaseCar
from basisklassen_cam import Camera
import time
import cv2




class CamCar(BaseCar):

    def test(self):
        car = Camera()
        while True:
            img = car.get_frame()
            cv2.imshow('image', img)
            if cv2.waitKey(5000) & 0xFF == ord('q'):
                break
        car.release()
        cv2.destroyAllWindows()
        car.stop()

        
    def test1(self):
        car = Camera()
        img = car.get_frame()
        cv2.imshow('image', img)
        cv2.waitKey(0) 

if __name__ == "__main__":
    test = CamCar()
    test.test1()