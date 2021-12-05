import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import glob

# Get Images from folder:

def get_images(folder_name):
    image_list = []

    for filename in glob.glob('./images/{}/*.png'.format(folder_name)): #assuming gif
        im=Image.open(filename)
        image_list.append(im)

    return image_list

image_list = get_images('background')

print(image_list[0].filename)

raw_input = input

raw_input()