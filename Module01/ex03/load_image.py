from PIL import Image
from array import array
import numpy as np


def ft_load(path: str):
    try:
        img = Image.open(path)
        img = np.array(img)
        print("The shape of image is :", img.shape)
        print(img)
        return (img)
    except FileNotFoundError as msg_err:
        print(msg_err)
    except Image.UnidentifiedImageError as msg_err:
        print(msg_err)
    exit(1)
    