# Some experimental Children of Camera
# The class allow transformation of the image

# Some ugly code alowing to import basisklassen_cam.py from the current file position
import os
import pathlib
import sys
path_to_this_file = os.path.realpath(__file__)
path_to_modules = pathlib.Path(path_to_this_file).resolve().parents[1].joinpath('Software')
sys.path.append(str(path_to_modules))
print("_Choosen path to basisklassen_cam.py",path_to_modules)
from basisklassen_cam import Camera
import cv2


class MyCam(Camera):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.selected_transformer = 'Original'
        self.transformers = {
            'Original': self.get_original,
            'Canny': self.get_canny,
            'Black/White': self.get_bw,
            'Switch Red Blue' : self.get_srb
        }
        self.add_transformer
        self.frames = {}

    def select_transformer(self, name):
        if name in self.transformers.keys():
            self.selected_transformer = name
        else:
            raise Exception('Selected transformer does not exist!')

    def get_available_transformer(self):
        return list(self.transformers.keys())
    
    def add_transformer(self,name, transformer):
        self.transformers.update({name: transformer})

    def get_frame(self):
        frame = super().get_frame()
        # self.make_frame()
        return self.transformers[self.selected_transformer](frame)

    def make_frame(self):
        self.frames = {name: transformer(self.frame) for name, transformer in self.transformers.items()}

    @staticmethod
    def get_original(frame):
        return frame

    @staticmethod
    def get_canny(frame):
        return cv2.Canny(frame, 100, 150)

    @staticmethod
    def get_bw(frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    @staticmethod
    def get_srb(frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


class MyCam2(Camera):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.transformers = {'Original': self.__original}
        self.select_transformer('Original')

    def get_available_transformer(self):
        return list(self.transformers.keys())

    @staticmethod
    def __original(frame):
        return frame

    def register_transformer(self, identifier : str):
        def register(func):
            self.transformers[identifier] = func
            return func
        return register

    def get_frame(self):
        frame = super().get_frame()
        return self.transformers[self.selected_transformer](frame)

    def select_transformer(self, name):
        if name in self.transformers.keys():
            self.selected_transformer = name
        else:
            raise Exception('Selected transformer does not exist!')


if __name__ == "__main__":

    x = MyCam2(flip=False, colorspace='rgb')
    print('Transformers:', x.transformers)

    @x.register_transformator('black_white')
    def black_white(frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    @x.register_transformator('canny')
    def canny(frame):
        return cv2.Canny(frame, 100, 150)

    print('Transformers:', x.transformers)

    import matplotlib.pylab as plt
    x.select_transformer('canny')
    frame = x.get_frame()
    x.release()
    print(frame.shape)
    plt.imshow(frame)