from basecar import BaseCar
from basisklassen_cam import Camera
import numpy as np
import cv2 as cv
import matplotlib.pylab as plt
import time
from datetime import datetime


class CamCar(BaseCar):

    def __init__(self):
        super().__init__()
        self.cam = Camera() 
        

    def bild_fertig(self):
        img = self.cam.get_frame() 
        img_cut = img[80:380,50:640].copy()
        img_cut_HSV = cv.cvtColor(img_cut,cv.COLOR_BGR2HSV)
        return img_cut_HSV  
    
    def stop_Cam(self):
        self.cam.release()
        


    def draw_lines(self):
            
        try:    
            lower = np.array([95, 0, 0])
            upper = np.array([125, 255, 255])
            rho = 1
            angle = np.pi / 180 
            min_threshold = 190  

            img_cut_HSV = self.bild_fertig()
            image_mask = cv.inRange(img_cut_HSV, lower, upper)
            parameter_mask = cv.HoughLines(image_mask, rho, angle, min_threshold)
            parameter_mask[:2]
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
                if y1 < 0:
                    rechte_seite = np.append(rechte_seite,[y1+1000] )
                if y1 > 0:
                    linke_seite = np.append(linke_seite,[y1])

            links = round(linke_seite.mean(),0) 
            rechts = round(rechte_seite.mean(),0)
            print('rechts',links,rechts)
            if rechts > 860:
                return int(60)

            elif rechts > 680 :
                return int(75)
            
            elif rechts > 650 :
               return int(85)
            
            elif rechts < 400 :
                return int(110)
            
            elif rechts < 500 :
                return int(100)
            
            elif rechts < 550 :
                return int(95)

            elif rechts < 650 :
                return int(90)
     
        except:
            pass

  
if __name__ == "__main__":
    test = CamCar()
    start = datetime.now()
    
    while (datetime.now()-start).seconds<= 35:
        test.drive(35,1)
        
        try:
            test.steering_angle = test.draw_lines()
            print(test.draw_lines())
        except:
            continue
        
        time.sleep(0.1)
       
    test.stop() 
    test.stop_Cam()  
   