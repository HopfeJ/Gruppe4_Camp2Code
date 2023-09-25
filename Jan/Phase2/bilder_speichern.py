from basisklassen_cam import Camera
import cv2 as cv
import os
from datetime import datetime


class Speichern():

    def __init__(self):
        super().__init__()
        self.cam = Camera()


    def save_image(self):
        #  Bild aufnehmen
    
        image = self.cam.get_frame()       
        

        # Dateinamen für das Bild
        img_name = "Bild {}.jpg".format(len(os.listdir("bilder_nn")) + 1)
        img_pfad = os.path.join("bilder_nn", img_name)

        # Speichert das Bild im Ordner
        cv.imwrite(img_pfad, image)
        #print("Bild gespeichert unter:", img_path)




    def save_with_date(self):
        image = self.cam.get_frame()
        img_name = f"Bild {datetime.now().replace(microsecond=0)}.png"              
        img_pfad = f"bilder_nn/{img_name}"
        cv.imwrite(img_pfad,image)


test = Speichern()
test.save_with_date()