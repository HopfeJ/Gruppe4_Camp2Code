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

    def make_points(self, image_edges, line):
        height, width = image_edges.shape
        slope, intercept = line
        y1 = height  # unterer Rand des Bildes
        y2 = int(y1 * 0.25)  # make points from middle of the frame down Standard: 1/2, besser 1/3

        # bound the coordinates within the frame
        x1 = max(-width, min(2 * width, int((y1 - intercept) / slope)))
        x2 = max(-width, min(2 * width, int((y2 - intercept) / slope)))
        return [[x1, y1, x2, y2]]

    def average_slope_intercept(self, image_edges, line_segments):
        """
        This function combines line segments into one or two lane lines
        If all line slopes are < 0: then we only have detected left lane
        If all line slopes are > 0: then we only have detected right lane
        """
        lane_lines = []
        if line_segments is None:
            print('average_slope_intercept(): Es wurden keine Linien line_segments gefunden.')
            return lane_lines

        height, width = image_edges.shape # Höhe und Breite des Bildes auslesen
        left_fit = []
        right_fit = []

        boundary = 1/3
        left_region_boundary = width * (1 - boundary)  # line segment für linke Linie muss auf dem linken 2/3 des Bildes sein
        right_region_boundary = width * boundary # line segment für rechte Linie muss auf dem rechten 2/3 des Bildes sein

        for line_segment in line_segments:
            for x1, y1, x2, y2 in line_segment:
                if x1 == x2:
                    print('Vertikale Linie überspringen, da Steigung unendlich.')
                    continue
                fit = np.polyfit((x1, x2), (y1, y2), 1) # Zu gegebenen Koordinaten des line segments die Steigung und Schnittpunkt finden
                slope = fit[0]      # Steigung
                intercept = fit[1]  # Schnittpunkt
                if slope < 0:       # Wenn Steiung negativ: Links
                    if x1 < left_region_boundary and x2 < left_region_boundary:
                        left_fit.append((slope, intercept))
                else:               # Steigung positiv: Rechts
                    if x1 > right_region_boundary and x2 > right_region_boundary:
                        right_fit.append((slope, intercept))

        left_fit_average = np.average(left_fit, axis=0)
        print('left avg: ', left_fit_average)
        if len(left_fit) > 0:
            lane_lines.append(self.make_points(image_edges, left_fit_average))

        right_fit_average = np.average(right_fit, axis=0)
        print('right avg: ', right_fit_average)
        if len(right_fit) > 0:
            lane_lines.append(self.make_points(image_edges, right_fit_average))
        return lane_lines
    
    def calc_fahrlinie(self, img, lane_lines):
        # Fahrlinie
        fahrlinie = []
        height, width = img.shape

        print(lane_lines)
        if lane_lines[0][0]:
            links = lane_lines[0][0]
            left_x2= links[2]
            y2 = links[3]

        if lane_lines[1][0]:
            rechts = lane_lines[1][0]
            right_x2 = rechts[2]
            y2 = rechts[3]

        camera_mid_offset_percent = 0.00 # 0.0 means car pointing to center, -0.03: car is centered to left, +0.03 means car pointing to right
        mid = int(width / 2 * (1 + camera_mid_offset_percent))
        x2_fahrlinie = int((left_x2 + right_x2) / 2)
        fahrlinie = [[mid, height, x2_fahrlinie, y2]] # 50 = y2 von links oder rechts
        print(fahrlinie)
        return fahrlinie
    
    def compute_steering_angle(self, frame, lane_lines):
        """ Find the steering angle based on lane line coordinate
            We assume that camera is calibrated to point to dead center
        """
        if len(lane_lines) == 0:
            print('No lane lines detected, do nothing')
            return -90

        height, width = frame.shape
        if len(lane_lines) == 1:
            print('Only detected one lane line, just follow it. %s' % lane_lines[0])
            x1, _, x2, _ = lane_lines[0][0]
            x_offset = x2 - x1
        else:
            links = lane_lines[0][0]
            rechts = lane_lines[1][0]
            left_x2= links[2]
            right_x2 = rechts[2]
            camera_mid_offset_percent = 0.00 # 0.0 means car pointing to center, -0.03: car is centered to left, +0.03 means car pointing to right
            mid = int(width / 2 * (1 + camera_mid_offset_percent))
            x_offset = (left_x2 + right_x2) / 2 - mid

        # find the steering angle, which is angle between navigation direction to end of center line
        y_offset = int(height / 2)

        angle_to_mid_radian = math.atan(x_offset / y_offset)  # angle (in radian) to center vertical line
        angle_to_mid_deg = int(angle_to_mid_radian * 180.0 / math.pi)  # angle (in degrees) to center vertical line
        steering_angle = angle_to_mid_deg + 90  # this is the steering angle needed by picar front wheel

        print('new steering angle: %s' % steering_angle)
        return steering_angle

    def draw_line_segments(self, line_segments, fahrlinie, img):
        img2 = img.copy()
        img2 = cv.cvtColor(img2, cv.COLOR_GRAY2RGB)
        for line in line_segments:
            x1,y1,x2,y2 = line[0]
            print(f'x1: {x1}, y1: {y1}, x2: {x2}, y2: {y2}')
            cv.line(img2,(x1,y1),(x2,y2),(200,100,100),3)
        if fahrlinie is not None:
            cv.line(img2,(fahrlinie[0][0], fahrlinie[0][1]), (fahrlinie[0][2], fahrlinie[0][3]),(0,0,255),3) # Fahrlinie einzeichnen
        return img2

    def close(self):
        self.cam.release()
        print('Camera from car released')
    

    
    