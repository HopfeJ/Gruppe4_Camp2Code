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
        lines_right_lane_boundary_y1 = np.array([])
        lines_left_lane_boundary_y1 = np.array([])
        lines_left_lane_boundary_y2 = np.array([])
        lines_right_lane_boundary_y2 = np.array([])

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

            if y1 > 0: # linke Fahrbahnbegrenzung
                lines_left_lane_boundary_y1 = np.append(lines_left_lane_boundary_y1, [y1])
                lines_left_lane_boundary_y2 = np.append(lines_left_lane_boundary_y2, [y2])
            if y1 < 0: # rechte Fahrbahnbegrenzung
                lines_right_lane_boundary_y1 = np.append(lines_right_lane_boundary_y1, [y1])
                lines_right_lane_boundary_y2 = np.append(lines_right_lane_boundary_y2, [y2])

            # print(x1,x2,y1,y2)
            img=cv.line(img,(x1,y1),(x2,y2),(200,100,100),1) # adds a line to an image
            cv.putText(img, 
                text = 'erkannte Geraden',
                org=(180,50), # Position
                fontFace= cv.FONT_HERSHEY_SIMPLEX,
                fontScale = 0.8, # Font size
                color = (255,247,0), # Color in rgb
                thickness = 2)
        if len(lines_left_lane_boundary_y1) > 0:
            img=cv.line(img,(x1,int(lines_left_lane_boundary_y1.mean())),(x2,int(lines_left_lane_boundary_y2.mean())),(100,200,100),3) # adds a line to an image
            lines_left_lane_boundary_y1_mean = lines_left_lane_boundary_y1.mean()
        else:
            lines_left_lane_boundary_y1_mean = 0    

        if len(lines_right_lane_boundary_y1) > 0:
            img=cv.line(img,(x1,int(lines_right_lane_boundary_y1.mean())),(x2,int(lines_right_lane_boundary_y2.mean())),(100,200,100),3) # adds a line to an image
            lines_right_lane_boundary_y1_mean = lines_right_lane_boundary_y1.mean()
        else:
            lines_right_lane_boundary_y1_mean = 0

        return (img, lines_left_lane_boundary_y1_mean, lines_right_lane_boundary_y1_mean)
    
    def steering_direction(self, lines_left_lane_boundary_y1_mean, lines_right_lane_boundary_y1_mean):
        if lines_left_lane_boundary_y1_mean > 200:
            return 135
        elif lines_right_lane_boundary_y1_mean > -400 and lines_right_lane_boundary_y1_mean != 0:
            return 45
        else:
            return 90