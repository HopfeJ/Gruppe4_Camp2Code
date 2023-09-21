from basecar import BaseCar
from basisklassen_cam import Camera
import numpy as np
import cv2 as cv
import matplotlib.pylab as plt
import time





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

        def draw_lines_links(parameter_mask,img):
            img2 = img.copy()
            img2 = cv.cvtColor(img2, cv.COLOR_GRAY2RGB)
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
                 
            time.sleep(0.2)  
            links = round(linke_seite.mean(),0)
           
            return links 
            
        def draw_lines_rechts(parameter_mask,img):
            img2 = img.copy()
            img2 = cv.cvtColor(img2, cv.COLOR_GRAY2RGB)
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
                    
            time.sleep(0.2)  
            rechts = round(rechte_seite.mean(),0)
            return   rechts       
        
        cam = Camera()
        lower = np.array([95, 0, 0])
        upper = np.array([125, 255, 255])
        rho = 1
        angle = np.pi / 180 
        min_threshold = 250  

        
        img = cam.get_frame() 
        img_cut = img[80:380,50:600].copy()
        img_cut_HSV = cv.cvtColor(img_cut,cv.COLOR_BGR2HSV) 
        image_mask = cv.inRange(img_cut_HSV, lower, upper)
        parameter_mask = cv.HoughLines(image_mask, rho, angle, min_threshold)
        parameter_mask[:2]
        links =  draw_lines_links(parameter_mask, image_mask) 
        rechts = draw_lines_rechts(parameter_mask,image_mask)
        cam.release()
        print(links,rechts)
        return links ,rechts
       
       








if __name__ == "__main__":
    test = CamCar()
    
    while True:
        #test.drive(30,1)
       
        if test.fahren_wie_auf_schienen() < (420,0):
            test.steering_angle = 110
       # if test.fahren_wie_auf_schienen() < 240 :
       #     test.steering_angle = 70
       # if test.fahren_wie_auf_schienen() < 420 :
       #     test.steering_angle = 90

   