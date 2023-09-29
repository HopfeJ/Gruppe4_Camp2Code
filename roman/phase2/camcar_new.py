from basecar import BaseCar
from basisklassen_cam import *

import numpy as np
import cv2 as cv
import matplotlib.pylab as plt
import time
import csv
import math
from datetime import datetime
import tensorflow as tf


class CamCar(BaseCar):
    
    def __init__(self, config: str = "config.json"):
        super().__init__(config)
        self.cam = Camera()
    
    def take_picture(self):
        img = self.cam.get_frame()                          # Foto aufnehmen
        return img

    def resize_image(self, img, x1, x2, y1, y2):
        # Größe Bildausschnitt: # 100,370,0,640
        # eingangsgröße Bild: 640, 480
        img_cut = img[x1:x2,y1:y2].copy()                
        # neue größe nach zuschneiden: 270, 640
        # fürs training des nn die hälfte nehmen: 135, 320
        #dim = img_cut.shape
        #dim = (320,240) # Bildgröße muss dem des Autos entsprechen!
        interpolation = cv2.INTER_AREA
        img_cut = cv2.resize(img_cut, (320, 135), interpolation)
        return img_cut

    def get_prep_image(self, img):
        # Werte f+r Blau-Anteil im HSV-Farbraum (360 Grad / 2)
        lower = np.array(self.data['lower'])
        upper = np.array(self.data['upper'])
        img_cut_HSV = cv.cvtColor(img,cv.COLOR_BGR2HSV) # in HSV-Raum umwandeln
        image_mask = cv.inRange(img_cut_HSV, lower, upper)  # blau-Anteil maskieren
        image_edges = cv.Canny(image_mask,200,400)          # Kanten der Blau-Maske ermitteln
        return image_edges

    def calc_line_segments(self, image_edges):
        rho = 1              # distance precision in pixel, i.e. 1 pixel
        angle = np.pi / 180  # angular precision in radian, i.e. 1 degree
        min_threshold = 20   # in etwas Anzal der Punkt auf der Geraden. Je geringer Min_threshold, desto mehr Geraden werden erkannt.
        minLineLength = 8    # Minimale Linienlänge
        maxLineGap = 4       # Maximale Anzahl von Lücken in der Linie
        line_segments = cv.HoughLinesP(image_edges, rho, angle, min_threshold, np.array([]), minLineLength=minLineLength, maxLineGap=maxLineGap)
        return line_segments

    def calc_linie(self, image_edges, line): # Helper-Function für calc_fahrbahnlinien
        höhe, breite = image_edges.shape
        slope, intercept = line
        y1 = höhe  # unterer Rand des Bildes
        y2 = int(y1 * 0.6)  # erstelle Linie von 75% von oben bis nach unten: 0.25

        # errechne Koordinaten aus Steigung und SChnittpunk
        x1 = max(-breite, min(2 * breite, int((y1 - intercept) / slope)))
        x2 = max(-breite, min(2 * breite, int((y2 - intercept) / slope)))
        return [[x1, y1, x2, y2]]

    def calc_fahrbahnlinien(self, image_edges, line_segments):
        
        fahrbahnlinien = []
        if line_segments is None:
            print('calc_fahrbahnlinien(): Es wurden keine Linien in line_segments gefunden.')
            return fahrbahnlinien

        höhe, breite = image_edges.shape # Höhe und Breite des Bildes auslesen
        links_werte = []
        rechts_werte = []

        grenzbereich = 1/3
        linker_grenzbereich = breite * (1 - grenzbereich)  # line segment für linke Linie muss auf dem linken 2/3 des Bildes sein
        rechter_grenzbereich = breite * grenzbereich # line segment für rechte Linie muss auf dem rechten 2/3 des Bildes sein

        for line_segment in line_segments:
            for x1, y1, x2, y2 in line_segment:
                if x1 == x2:
                    #print('Vertikale Linie überspringen, da Steigung unendlich.')
                    continue
                # Was tun, wenn x2 < x1, sich also die Linien kreuzen?
                werte = np.polyfit((x1, x2), (y1, y2), 1) # Zu gegebenen Koordinaten des line segments die Steigung und Schnittpunkt finden #(x1, x2), (y1, y2)
                slope = werte[0]      # Steigung
                intercept = werte[1]  # Schnittpunkt
                #print('werte für Steigung und schnittpkt:', werte)
                if slope < 0:       # Wenn Steiung negativ: Links
                    if x1 < linker_grenzbereich and x2 < linker_grenzbereich:
                        links_werte.append((slope, intercept))
                else:               # Steigung positiv: Rechts
                    if x1 > rechter_grenzbereich and x2 > rechter_grenzbereich:
                        rechts_werte.append((slope, intercept))
        # was tun, wenn links/rechts avg = nan, also keine Linie gefunden? -> maximaler Lenkeinschlag in Gegenrichtung?
        
        #print('links_werte: ', links_werte)
        links_werte_avg = np.average(links_werte, axis=0)
        #print(type(links_werte_avg))
        #print('left avg: ', links_werte_avg)
        if np.isnan(links_werte_avg).any():
            #print('links_werte_avg nan')
            default_links = [[1, höhe, -500, int(höhe * 0.6)]] # 0.5
            fahrbahnlinien.append(default_links)
        else:
            fahrbahnlinien.append(self.calc_linie(image_edges, links_werte_avg))
            
        #print('rechts_werte: ', rechts_werte)
        rechts_werte_avg = np.average(rechts_werte, axis=0)
        if np.isnan(rechts_werte_avg).any():
            #print('rechts_werte_avg nan')
            default_rechts = [[breite, höhe, breite+500, int(höhe * 0.6)]] # 0.5
            fahrbahnlinien.append(default_rechts)
        else:
            fahrbahnlinien.append(self.calc_linie(image_edges, rechts_werte_avg))

        #print('calc_fahrbahnlinien(): ', fahrbahnlinien)
        return fahrbahnlinien
    
    def calc_leitlinie(self, img, fahrbahnlinien):
        # Leitlinie erzeugen
        leitlinie = []
        höhe, breite = img.shape

        if fahrbahnlinien[0][0]:
            links = fahrbahnlinien[0][0]

            links_x2= links[2]
            y2 = links[3]
            #print('leitlinie links_x2, links_y2: ', links_x2, y2)

        if fahrbahnlinien[1][0]:
            rechts = fahrbahnlinien[1][0]

            rechts_x2 = rechts[2]
            y2 = rechts[3]
            #print('leitlinie rechts_x2, rechts_y2: ', rechts_x2, y2)

        mid = int(breite / 2)
        x2_leitlinie = int((links_x2 + rechts_x2) / 2)
        leitlinie = [[mid, höhe, x2_leitlinie, y2]] # 50 = y2 von links oder rechts
        #print(leitlinie)
        return leitlinie
    
    def calc_steering_angle_from_cam(self, frame, fahrbahnlinien):

        if len(fahrbahnlinien) == 0:
            print('Keine Linien gefunden -> nicht lenken.')
            return -90

        höhe, breite = frame.shape
        if len(fahrbahnlinien) == 1:
            print('Nur eine Linie gefunden. %s' % fahrbahnlinien[0])
            x1, _, x2, _ = fahrbahnlinien[0][0]
            x_versatz = x2 - x1
        else:
            links = fahrbahnlinien[0][0]
            rechts = fahrbahnlinien[1][0]
            links_x2= links[2]
            rechts_x2 = rechts[2]
            mid = int(breite / 2)
            x_versatz = (links_x2 + rechts_x2) / 2 - mid

        # Lenkwinkel als Winkel zwischen Senkrechten auf X-Achse und Endpunkt der Leitlinie
        y_versatz = int(höhe / 2) # halbe Bildhöhe

        winkel_radian = math.atan(x_versatz / y_versatz)  
        winkel_grad = int(winkel_radian * 180.0 / math.pi)
        steering_angle = winkel_grad + 90  # + 90 als geradeaus

        #print('new steering angle: %s' % steering_angle)
        return steering_angle
    
   

    def draw_line_segments(self, line_segments, leitlinie, img):
        img2 = img.copy()
        img2 = cv.cvtColor(img2, cv.COLOR_GRAY2RGB)
        for line in line_segments:
            x1,y1,x2,y2 = line[0]
            #print(f'x1: {x1}, y1: {y1}, x2: {x2}, y2: {y2}')
            cv.line(img2,(x1,y1),(x2,y2),(200,100,100),3)
        if leitlinie is not None:
            cv.line(img2,(leitlinie[0][0], leitlinie[0][1]), (leitlinie[0][2], leitlinie[0][3]),(0,0,255),3) # Leitlinie einzeichnen
        return img2

    def save_with_date(self, img, angle):
        img_name = f"Bild {datetime.now().replace(microsecond=0)}_Angle_{angle}.png"              
        img_pfad = f"bilder_nn/{img_name}"
        cv.imwrite(img_pfad, img)

    def close(self):
        self.cam.release()
        print('Camera from car released')
    
class DeepCar(CamCar):

    def __init__(self, config: str = "config.json"):
        super().__init__(config)
        self.model = self.load_model()

    def load_model(self):
        # Laden eines Modells
        # Laden eines Modells
        # path_to_model_file = './Model_v3.h5'
        # model_loaded = tf.keras.models.load_model(path_to_model_file)   
        # return model_loaded
        pass
    
    def get_steering_angle_from_nn(self, resized_image):
        xe = np.array( [resized_image] )
        xe.shape
        angle = xe
        return angle

    
    