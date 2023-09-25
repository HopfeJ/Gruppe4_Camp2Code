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

        def draw_lines(parameter_mask,img):
            img2 = img.copy()
            img2 = cv.cvtColor(img2, cv.COLOR_GRAY2RGB)
            linke_seite = np.array([])
            rechte_seite = np.array([])
            for line in parameter_mask:
                rho,theta = line[0]
                a = -np.cos(theta)/np.sin(theta) # Anstieg der Gerade
                b = rho/np.sin(theta)            # Absolutglied/Intercept/Schnittpunkt mit der y-Achse
                x1 = 0
                y1 = int(b)
                x2 = 1000
                y2 = int(a*1000+b)
                    
                img2=cv.line(img2,(x1,y1),(x2,y2),(200,100,100),1) # adds a line to an image

                if y1 > 0:
                    linke_seite = np.append(linke_seite,[y1])
                if y1 < 0:
                    rechte_seite = np.append(rechte_seite,[y1+1000] )

            

            #print(linke_seite.mean())
            print(round(linke_seite.mean(),0),round(rechte_seite.mean(),0))  
            return img2
        
        
        
        cam = Camera()
        lower = np.array([95, 0, 0])
        upper = np.array([125, 255, 255])
        rho = 1
        angle = np.pi / 180 
        min_threshold = 250  

        while True:
            img = cam.get_frame() 
            img_cut = img[80:380,50:640].copy()
            img_cut_HSV = cv.cvtColor(img_cut,cv.COLOR_BGR2HSV) 

            image_mask = cv.inRange(img_cut_HSV, lower, upper)
            try:
                parameter_mask = cv.HoughLines(image_mask, rho, angle, min_threshold)
                parameter_mask[:2]
            except:
                pass

            imageresult =  draw_lines(parameter_mask, image_mask) 
            
                
            cv.imshow("Display window (press q to quit)", imageresult)
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