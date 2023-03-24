from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt
import matplotlib as mpl
from array import array
import numpy as np
from load_image import ft_load

def ft_zoom(init_y: int, init_x: int, zoom: int, path: str):

    try:
        if isinstance(init_y, int) != True or isinstance(init_y, int) != True:
            raise AssertionError ("Bad type")
        img = ft_load(path)
        y,x,rgb = img.shape
        if (init_x < 0 or init_y < 0):
            print("Bad value")
            exit(1)
        if ((init_y + zoom) > y or (zoom + init_x) > x):
            print("Bad value")
            exit(1)
        img = img[(init_y): (init_y + zoom), (init_x): (zoom + init_x)]
        img = img[:,:,1]
        mpl.style.use("grayscale")
        plt.imshow(img)
        print("New shape after slicing:", img.shape)
        print(img)
        plt.show()
    except AssertionError as msg_err:
    	print(msg_err)

if __name__ == '__main__':

    ft_zoom(150, 450, 400, "animal.jpeg")