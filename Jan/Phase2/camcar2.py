from basecar import BaseCar
from basisklassen_cam import Camera
import numpy as np
import cv2 as cv
import matplotlib.pylab as plt
import time
from datetime import datetime


class CamCar(BaseCar):

   

    def draw_lines_links(self):
        try:    
            cam = Camera()
            lower = np.array([95, 0, 0])
            upper = np.array([125, 255, 255])
            rho = 1
            angle = np.pi / 180 
            min_threshold = 190  

            img = cam.get_frame() 
            img_cut = img[80:380,50:640].copy()
            img_cut_HSV = cv.cvtColor(img_cut,cv.COLOR_BGR2HSV) 
            image_mask = cv.inRange(img_cut_HSV, lower, upper)
            parameter_mask = cv.HoughLines(image_mask, rho, angle, min_threshold)
            parameter_mask[:2]
            linke_seite = np.array([])
            for line in parameter_mask:
                rho,theta = line[0]
                a = -np.cos(theta)/np.sin(theta) # Anstieg der Gerade
                b = rho/np.sin(theta)            # Absolutglied/Intercept/Schnittpunkt mit der y-Achse
                x1 = 0
                y1 = int(b)
                x2 = 1000
                y2 = int(a*1000+b)
                if y1 > 0:
                    linke_seite = np.append(linke_seite,[y1])

             
            links = round(linke_seite.mean(),0)
            #print('Links',links)
            cam.release()
            return links 
        except:
            pass

    def draw_lines_rechts(self):
        try:    
            cam = Camera()
            lower = np.array([95, 0, 0])
            upper = np.array([125, 255, 255])
            rho = 1
            angle = np.pi / 180 
            min_threshold = 190  

            img = cam.get_frame() 
            img_cut = img[80:380,50:640].copy()
            img_cut_HSV = cv.cvtColor(img_cut,cv.COLOR_BGR2HSV) 
            image_mask = cv.inRange(img_cut_HSV, lower, upper)
            parameter_mask = cv.HoughLines(image_mask, rho, angle, min_threshold)
            parameter_mask[:2]
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

              
            rechts = round(rechte_seite.mean(),0)
            print('rechts',rechts)
            cam.release()
            return   rechts       
        except:
            pass
   
   
    
   
  
    
    
if __name__ == "__main__":
    test = CamCar()
    start = datetime.now()
    while (datetime.now()-start).seconds<= 90:
        test.drive(30,1)
        try:
            if test.draw_lines_rechts() > 860 :
                test.steering_angle = 58
                test.drive(25,1)
                print('voller einschlag')
            if test.draw_lines_rechts() > 660 :
                test.steering_angle = 70
                print('voller einschlag')
            if test.draw_lines_rechts() < 540 :
                test.steering_angle = 85
            #    print('leichter einschlag')
            #if test.draw_lines_rechts() < 200 :
            #    test.steering_angle = 80
            #    print('einschlag recht')   
            #if test.draw_lines_rechts() > 610 :
            #    test.drive(35,1)
            #    test.steering_angle = 80
           
            if test.draw_lines_rechts() < 660 :
            #    #test.drive(20,1)
                test.steering_angle = 90
                print('gerade')
            #if test.draw_lines_links() > 530:
            #    test.steering_angle = 110 
            if test.draw_lines_links() > 230:
                test.steering_angle = 95  
        except:
            pass
    test.stop()   
   