from basecar import BaseCar
from basisklassen_cam import Camera
import cv2 as cv
import numpy as np
from time import sleep
from datetime import datetime

def draw_lines(parameter_mask,img):
    img2 = img.copy()
    img2 = cv.cvtColor(img2, cv.COLOR_GRAY2RGB)

    if parameter_mask is None:
        return img2
    
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
            continue
        #print(x1,x2,y1,y2)
        img2=cv.line(img2,(x1,y1),(x2,y2),(200,100,100),1) # adds a line to an image
        cv.putText(img2, 
            text = 'erkannte Geraden',
            org=(10,190), # Position
            fontFace= cv.FONT_HERSHEY_SIMPLEX,
            fontScale = .8, # Font size
            color = (120,255,255), # Color in hsv
            thickness = 2)
    return img2

class CamCar(BaseCar):
    
    def __init__(self):
        super().__init__()
        self.cam = Camera()
        self.stop_it = False
        self.image_hough = None
        print(self.data)

    def make_picture(self):
        img = self.cam.get_frame()
        return img

    def prepare_picture(self, img):
        img_cut = img[80:380, 30:610] # Y-Achse, X-Achse
        img_cut_hsv = cv.cvtColor(img_cut, cv.COLOR_BGR2HSV)
        return img_cut_hsv
    
    def save_with_date(self,img,angle):
        img_name = f"Bild {datetime.now().replace(microsecond=0)}_Angle_{angle}.png"              
        img_pfad = f"bilder_nn/{img_name}"
        cv.imwrite(img_pfad,img)
    
    def calculate_angle_from_picture(self, img):
        # Farbfilter anwenden
        lower = np.array(self.data['lower'])
        upper = np.array(self.data['upper'])
        image_mask = cv.inRange(img, lower, upper)
        # Geraden im Bild ermitteln
        rho = 1  # distance precision in pixel, i.e. 1 pixel
        angle = np.pi / 180  # angular precision in radian, i.e. 1 degree
        min_threshold = 220  # minimal of votes, Je geringer Min_threshold, dest mehr Geraden werden erkannt.
        found_lines = cv.HoughLines(image_mask, rho, angle, min_threshold)
        lines_left_lane_boundary_y1_mean, lines_right_lane_boundary_y1_mean = self.calculate_lines_in_lane_boundary(found_lines)
        self.image_hough = draw_lines(found_lines, image_mask)
        
        if lines_left_lane_boundary_y1_mean > 490: # 200
            print(round(lines_left_lane_boundary_y1_mean,0))
            return 135

        elif lines_left_lane_boundary_y1_mean > 350: # 200
            print(round(lines_left_lane_boundary_y1_mean,0))
            return 120
        
        elif lines_left_lane_boundary_y1_mean > 310 :
            print(round(lines_left_lane_boundary_y1_mean,0))
            return 105

        elif lines_right_lane_boundary_y1_mean > -170 and lines_right_lane_boundary_y1_mean != 0: #-400
            print(round(lines_right_lane_boundary_y1_mean,0))
            return 55

        elif lines_right_lane_boundary_y1_mean > -300 and lines_right_lane_boundary_y1_mean != 0: #-400
            print(round(lines_right_lane_boundary_y1_mean,0))
            return 75
        
        elif lines_right_lane_boundary_y1_mean > -380 and lines_right_lane_boundary_y1_mean != 0: #-400
            print(round(lines_right_lane_boundary_y1_mean,0))
            return 80

        else:
            print(round(lines_left_lane_boundary_y1_mean,0))
            return 90
        
    def calculate_lines_in_lane_boundary(self, found_lines): 
        lines_right_lane_boundary_y1 = np.array([])
        lines_left_lane_boundary_y1 = np.array([])
        lines_left_lane_boundary_y2 = np.array([])
        lines_right_lane_boundary_y2 = np.array([])
        
        if found_lines is None:
            lines_left_lane_boundary_y1_mean = 0
            lines_right_lane_boundary_y1_mean = 0
            return (lines_left_lane_boundary_y1_mean, lines_right_lane_boundary_y1_mean)
        
        for line in found_lines:
            
            rho,theta = line[0]
            try:
                a = -np.cos(theta)/np.sin(theta) # Anstieg der Gerade
                b = rho/np.sin(theta)            # Absolutglied/Intercept/Schnittpunkt mit der y-Achse
                x1 = 0
                y1 = int(b)
                x2 = 1000
                y2 = int(a*1000+b)
            except:
                continue

            if y1 > 0: # linke Fahrbahnbegrenzung
                lines_left_lane_boundary_y1 = np.append(lines_left_lane_boundary_y1, [y1])
                lines_left_lane_boundary_y2 = np.append(lines_left_lane_boundary_y2, [y2])
            if y1 < 0: # rechte Fahrbahnbegrenzung
                lines_right_lane_boundary_y1 = np.append(lines_right_lane_boundary_y1, [y1])
                lines_right_lane_boundary_y2 = np.append(lines_right_lane_boundary_y2, [y2])
                
        if len(lines_left_lane_boundary_y1) > 0:
            lines_left_lane_boundary_y1_mean = lines_left_lane_boundary_y1.mean()
        else:
            lines_left_lane_boundary_y1_mean = 0    

        if len(lines_right_lane_boundary_y1) > 0:
            lines_right_lane_boundary_y1_mean = lines_right_lane_boundary_y1.mean()
        else:
            lines_right_lane_boundary_y1_mean = 0

        return (lines_left_lane_boundary_y1_mean, lines_right_lane_boundary_y1_mean)
    
    def show_picture(self, img):
        window = "Picture Viewer (press q to quit)"
        cv.imshow(window, img)
        key = cv.waitKey(1)
        if key == ord("q"):
            self.stop_it = True

    def run(self):
        counter = 0
        while True:
            if self.stop_it: 
                break
            # Bild machen
            img = self.make_picture()
            # Bild schneiden und colorieren
            prepared_image = self.prepare_picture(img)
            # Bild übergeben und Steuerwinkel zurückgeben
            steering_angle = self.calculate_angle_from_picture(prepared_image)
            # Bild anzeigen
            self.show_picture(self.image_hough)
            # Winkel setzen und Auto fahren lassen
            self.drive(35, 1)
            self.steering_angle = steering_angle
            print(steering_angle)
            if counter > 10:
                self.save_with_date(img,steering_angle)
                counter =0
            #sleep(0.2)
            counter +=1
        self.stop()

if __name__ == "__main__":
    my_car = CamCar()
    my_car.run()
