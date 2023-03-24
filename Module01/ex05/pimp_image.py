from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt
import matplotlib as mpl
from array import array
import numpy as np
from load_image import ft_load
from PIL import ImageFilter

def ft_blue(path: str):

    img = ft_load(path)
    img[:, :, 0:2] = 0
    print(img)
    plt.imshow(img)
    plt.show()

def ft_green(path: str):

    img = ft_load(path)
    img[:, :, 0] = 0
    img[:, :, 2] = 0
    print(img)
    plt.imshow(img)
    plt.show()

def ft_red(path: str):

    img = ft_load(path)
    img[:, :, 1] = 0
    img[:, :, 2] = 0
    print(img)
    plt.imshow(img)
    plt.show()

def ft_grey(path: str):

    img = ft_load(path)
    img = img[:,:,1]
    mpl.style.use("grayscale")
    plt.imshow(img)
    print(img)
    plt.show()

def ft_invert(path: str):

    img = ft_load(path)
    plt.imshow(img[::-1])
    print(img)
    plt.show()

if __name__ == '__main__':

    ft_blue("landscape.jpg")
    ft_green("landscape.jpg")
    ft_red("landscape.jpg")
    ft_grey("landscape.jpg")
    ft_invert("landscape.jpg")
