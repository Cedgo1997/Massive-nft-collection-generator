import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import glob

# Get Images from folder:
image_list = []
for filename in glob.glob('./images/*.png'): #assuming gif
    im=Image.open(filename)
    image_list.append(im)


print(image_list[0].filename)

raw_input = input

raw_input()