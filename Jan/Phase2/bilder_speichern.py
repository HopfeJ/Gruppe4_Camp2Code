from basisklassen_cam import Camera
import cv2
import os


def save_image():
    #  Bild aufnehmen
    cam = Camera()
    image = cam.get_frame()       
    cam.release()

    # Dateinamen für das Bild
    img_name = "straße_{}.jpg".format(len(os.listdir("bilder_nn")) + 1)
    img_pfad = os.path.join("bilder_nn", img_name)

    # Speichere das Bild im angegebenen Ordner
    cv2.imwrite(img_pfad, image)
    #print("Bild gespeichert unter:", img_path)




save_image()
