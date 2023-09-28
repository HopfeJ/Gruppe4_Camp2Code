import numpy as np
import cv2 as cv
import matplotlib.pylab as plt
from camcar_new import *
import time
import os


car = DeepCar()

img_path = "C:/Users/EISENBRO/Desktop/python/code/roman/phase2/bilder_nn/"
img_files = os.listdir(img_path)

#img = car.take_picture()
img = cv2.imread(cv2.imread(img_path + img_files[0]))
resized_img = car.resize_image(img, 100,370,0,640)
plt.imshow(resized_img)
