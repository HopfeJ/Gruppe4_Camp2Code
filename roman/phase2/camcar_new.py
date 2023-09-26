from basecar import BaseCar
from basisklassen_cam import *

import numpy as np
import cv2 as cv
import matplotlib.pylab as plt
import time
import csv
import math
from datetime import datetime


class CamCar(BaseCar):
    
    def __init__(self, config: str = "config.json"):
        super().__init__(config)
        self.cam = Camera()
    

    def get_prep_image(self):
        # Werte f+r Blau-Anteil im HSV-Farbraum (360 Grad / 2)
        lower = np.array([90, 0, 0])
        upper = np.array([125, 255, 255])

        img = self.cam.get_frame()                          # Foto aufnehmen
        img_cut = img[200:400,20:620].copy()                # Foto beschneiden
        img_cut_HSV = cv.cvtColor(img_cut,cv.COLOR_BGR2HSV) # in HSV-Raum umwandeln
        image_mask = cv.inRange(img_cut_HSV, lower, upper)  # blau-Anteil maskieren
        image_edges = cv.Canny(image_mask,200,400)          # Kanten der Blau-Maske ermitteln

        return image_edges

    def calc_line_segments(self, image_edges):
        rho = 1              # distance precision in pixel, i.e. 1 pixel
        angle = np.pi / 180  # angular precision in radian, i.e. 1 degree
        min_threshold = 10   # in etwas Anzal der Punkt auf der Geraden. Je geringer Min_threshold, desto mehr Geraden werden erkannt.
        minLineLength = 8    # Minimale Linienlänge
        maxLineGap = 4       # Maximale Anzahl von Lücken in der Linie
        line_segments = cv.HoughLinesP(image_edges, rho, angle, min_threshold, np.array([]), minLineLength=minLineLength, maxLineGap=maxLineGap)
        return line_segments

    def calc_linie(self, image_edges, line):
        höhe, breite = image_edges.shape
        slope, intercept = line
        y1 = höhe  # unterer Rand des Bildes
        y2 = int(y1 * 0.25)  # erstelle Linie von 75% von oben bis nach unten

        # errechne Koordinaten aus Steigung und SChnittpunk
        x1 = max(-breite, min(2 * breite, int((y1 - intercept) / slope)))
        x2 = max(-breite, min(2 * breite, int((y2 - intercept) / slope)))
        return [[x1, y1, x2, y2]]

    def teile_linien(self, image_edges, line_segments):
        
        linien = []
        if line_segments is None:
            print('teile_linien(): Es wurden keine Linien in line_segments gefunden.')
            return linien

        höhe, breite = image_edges.shape # Höhe und Breite des Bildes auslesen
        links_werte = []
        rechts_werte = []

        grenzbereich = 1/3
        linker_grenzbereich = breite * (1 - grenzbereich)  # line segment für linke Linie muss auf dem linken 2/3 des Bildes sein
        rechter_grenzbereich = breite * grenzbereich # line segment für rechte Linie muss auf dem rechten 2/3 des Bildes sein

        for line_segment in line_segments:
            for x1, y1, x2, y2 in line_segment:
                if x1 == x2:
                    print('Vertikale Linie überspringen, da Steigung unendlich.')
                    continue
                werte = np.polyfit((x1, x2), (y1, y2), 1) # Zu gegebenen Koordinaten des line segments die Steigung und Schnittpunkt finden
                slope = werte[0]      # Steigung
                intercept = werte[1]  # Schnittpunkt
                if slope < 0:       # Wenn Steiung negativ: Links
                    if x1 < linker_grenzbereich and x2 < linker_grenzbereich:
                        links_werte.append((slope, intercept))
                else:               # Steigung positiv: Rechts
                    if x1 > rechter_grenzbereich and x2 > rechter_grenzbereich:
                        rechts_werte.append((slope, intercept))

        links_werte_avg = np.average(links_werte, axis=0)
        print('left avg: ', links_werte_avg)
        if len(links_werte) > 0:
            linien.append(self.calc_linie(image_edges, links_werte_avg))

        rechts_werte_avg = np.average(rechts_werte, axis=0)
        print('right avg: ', rechts_werte_avg)
        if len(rechts_werte) > 0:
            linien.append(self.calc_linie(image_edges, rechts_werte_avg))
        return linien
    
    def calc_leitlinie(self, img, linien):
        # Leitlinie
        leitlinie = []
        höhe, breite = img.shape

        print(leitlinie)
        if linien[0][0]:
            links = linien[0][0]
            left_x2= links[2]
            y2 = links[3]

        if linien[1][0]:
            rechts = linien[1][0]
            right_x2 = rechts[2]
            y2 = rechts[3]

        mid = int(breite / 2)
        x2_leitlinie = int((left_x2 + right_x2) / 2)
        leitlinie = [[mid, höhe, x2_leitlinie, y2]] # 50 = y2 von links oder rechts
        print(leitlinie)
        return leitlinie
    
    def calc_steering_angle(self, frame, linien):

        if len(linien) == 0:
            print('Keine Linien gefunden -> nicht lenken.')
            return -90

        höhe, breite = frame.shape
        if len(linien) == 1:
            print('Nur eine Linie gefunden. %s' % linien[0])
            x1, _, x2, _ = linien[0][0]
            x_versatz = x2 - x1
        else:
            links = linien[0][0]
            rechts = linien[1][0]
            left_x2= links[2]
            right_x2 = rechts[2]
            mid = int(breite / 2)
            x_versatz = (left_x2 + right_x2) / 2 - mid

        # Lenkwinkel als Winkel zwischen Senkrechten auf X-Achse und Endpunkt der Leitlinie
        y_versatz = int(höhe / 2) # halbe Bildhöhe

        winkel_zur_mitte_radian = math.atan(x_versatz / y_versatz)  
        winkel_zur_mitte_grad = int(winkel_zur_mitte_radian * 180.0 / math.pi)
        steering_angle = winkel_zur_mitte_grad + 90  # 90 als geradeaus

        print('new steering angle: %s' % steering_angle)
        return steering_angle

    def draw_line_segments(self, line_segments, leitlinie, img):
        img2 = img.copy()
        img2 = cv.cvtColor(img2, cv.COLOR_GRAY2RGB)
        for line in line_segments:
            x1,y1,x2,y2 = line[0]
            print(f'x1: {x1}, y1: {y1}, x2: {x2}, y2: {y2}')
            cv.line(img2,(x1,y1),(x2,y2),(200,100,100),3)
        if leitlinie is not None:
            cv.line(img2,(leitlinie[0][0], leitlinie[0][1]), (leitlinie[0][2], leitlinie[0][3]),(0,0,255),3) # Leitlinie einzeichnen
        return img2

    def close(self):
        self.cam.release()
        print('Camera from car released')
    

    
    