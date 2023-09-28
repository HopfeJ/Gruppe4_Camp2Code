from camcar import CamCar
import cv2 as cv
import numpy as np
from time import sleep
from datetime import datetime
import tensorflow as tf




class DeepCar(CamCar):

    def __init__(self):
        super().__init__()

    def load_model(self):                                               # Laden des models
        path_to_model_file = self.data['modell']                             # Hier wird der Pfad angegeben in dem sich das Model befindet
        self.model_loaded = tf.keras.models.load_model(path_to_model_file)
        

    def calculate_angle_from_nn(self, img):
        img_np_array = np.array([img]) 
        evaluated = self.model_loaded(img_np_array).numpy()         #Hier wird das Bild übergeben und ausgewertet
        print(round(evaluated[0][0]))
        return round(evaluated[0][0])
        

    def resize_picture(self,img):
        dim = (320,150)                         # bildgröße erster wert ist die x achse zeiter die y
        interpolation = cv.INTER_AREA
        img1 = cv.resize(img,dim,interpolation) #  Anpassung der Bildgröße   
        return img1  



    def run(self):
        self.load_model()
        while True:
            if self.stop_it: 
                break
            # Bild machen
            img = self.make_picture()
            # Bild schneiden und colorieren
            prepared_image = self.prepare_picture(img)
            # Bild übergeben und größe ändern
            resize_image = self.resize_picture(prepared_image)
            # zeigt das Bild an
            self.show_picture(resize_image)
            # das verkleinerte bild an die winkelberechnung übergeben
            # Winkel setzen und Auto fahren lassen
            self.steering_angle = self.calculate_angle_from_nn(resize_image)
            # Geschwindigkeit setzen
            self.drive(40,1)
            
        
        
        self.stop()
       

if __name__ == "__main__":
    my_car = DeepCar()
    my_car.run()
