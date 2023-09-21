import numpy as np
import cv2 as cv

class SteeringController():
    
    def __init__(self, lower, upper) -> None:
        self.lower = lower
        self.upper = upper

    def classic_hough_transformation(self, img): # Klassische Hough-Transformation
        img_cut_HSV = cv.cvtColor(img,cv.COLOR_BGR2HSV)
        image_mask = cv.inRange(img_cut_HSV, self.lower, self.upper)
        rho = 1  # distance precision in pixel, i.e. 1 pixel
        angle = np.pi / 180  # angular precision in radian, i.e. 1 degree
        min_threshold = 210  # minimal of votes, Je geringer Min_threshold, dest mehr Geraden werden erkannt. 
        parameter_mask = cv.HoughLines(image_mask, rho, angle, min_threshold)
        imageresult =  self.draw_lines(parameter_mask, image_mask)
        return imageresult

    def draw_lines(self,parameter_mask, image_mask): # Diese Funktion zeichnet die Geraden in das Bild ein
        img = image_mask.copy()
        img = cv.cvtColor(img, cv.COLOR_GRAY2RGB)
        for line in parameter_mask:
        
            rho,theta = line[0]
            try:
                a = -np.cos(theta)/np.sin(theta) # Anstieg der Gerade
                b = rho/np.sin(theta)            # Absolutglied/Intercept/Schnittpunkt mit der y-Achse
                x1 = 0
                y1 = int(b)
                x2 = 1000
                y2 = int(a*1000+b)
            except:
                #print(f'Fehler{a,b}')
                pass

            # print(x1,x2,y1,y2)
            img=cv.line(img,(x1,y1),(x2,y2),(200,100,100),1) # adds a line to an image
            cv.putText(img, 
                text = 'erkannte Geraden',
                org=(180,50), # Position
                fontFace= cv.FONT_HERSHEY_SIMPLEX,
                fontScale = 0.8, # Font size
                color = (255,247,0), # Color in rgb
                thickness = 2)
        return img