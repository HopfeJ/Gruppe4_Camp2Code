from basecar import BaseCar
from basisklassen_cam import Camera
import numpy as np
import cv2 as cv
import matplotlib.pylab as plt
import time
import statistics as st




class CamCar(BaseCar):

    def test(self):
        car = Camera()
        while True:
            img = car.get_frame()
            cv.imshow('image', img)
            if cv.waitKey(5000) & 0xFF == ord('q'):
                break
        car.release()
        cv.destroyAllWindows()
        car.stop()

        
    def test1(self):
        car = Camera()
        img = car.get_frame()
        cv.imshow('image', img)
        cv.waitKey(0) 



    def fahren_wie_auf_schienen(self):

        def draw_line_segments(line_segments,img):
            img2 = img.copy()
            img2 = cv.cvtColor(img2, cv.COLOR_GRAY2RGB)
            for line in line_segments:
                x1,y1,x2,y2 = line[0]
                cv.line(img2,(x1,y1),(x2,y2),(0,0,255),3)
                #cv.line(img2,(y1,y2),(255,0,0),3)
            cv.putText(img2, 
                    text = 'gezeichnete linien',
                    org=(180,190), # Position
                    fontFace= cv.FONT_HERSHEY_SIMPLEX,
                    fontScale = .8, # Font size
                    color = (255,247,0), # Color in rgb
                    thickness = 2)
            print(y1,y2)
            return img2
        
        cam = Camera()
        lower = np.array([95, 0, 0])
        upper = np.array([125, 255, 255])
        rho = 1              # distance precision in pixel, i.e. 1 pixel
        angle = np.pi / 180  # angular precision in radian, i.e. 1 degree
        min_threshold = 180   # in etwas Anzal der Punkt auf der Geraden. Je geringer Min_threshold, desto mehr Geraden werden erkannt.
        minLineLength = 15    # Minimale Linienlänge
        maxLineGap = 4       # Maximale Anzahl von Lücken in der Linie



        




        while True:
            img = cam.get_frame() 
            img_cut = img[80:380,50:640].copy()
            img_cut_HSV = cv.cvtColor(img_cut,cv.COLOR_BGR2HSV) 

            image_mask = cv.inRange(img_cut_HSV, lower, upper)

            image_edges = cv.Canny(image_mask,200,400)
        

            line_segments = cv.HoughLinesP(image_mask, rho, angle, min_threshold, np.array([]), minLineLength=minLineLength, maxLineGap=maxLineGap)
            line_segments[:2]


          

            imageresult1 = draw_line_segments(line_segments,image_mask)
            
                
            cv.imshow("Display window (press q to quit)", imageresult1)
            # Ende bei Drücken der Taste q
            if cv.waitKey(1) == ord('q'):
                break
              
            time.sleep(0.1)
        
        cam.release()
        cv.destroyAllWindows()
       








if __name__ == "__main__":
    test = CamCar()
    test.fahren_wie_auf_schienen()
    #test.steering_angle =90
    #time.sleep(3)
    #test.steering_angle = 45
    #time.sleep(3)
    #test.steering_angle =90