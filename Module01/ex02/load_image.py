from PIL import Image
from array import array
import numpy as np


def ft_load(path: str) -> array:
    try:
        img = Image.open(path)
        img = np.array(img)
        print("The shape of image is :", img.shape)
        return (img)
    except FileNotFoundError as msg_err:
        print(msg_err)
    except Image.UnidentifiedImageError as msg_err:
        print(msg_err)
    exit(1)
# if __name__ == '__main__':

#     print(ft_load("landscape.jpg"))
