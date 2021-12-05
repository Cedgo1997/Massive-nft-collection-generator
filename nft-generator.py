import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import glob
import inquirer

# Get folder list name:
def get_folder_list_names():
    return os.listdir('./images')

def get_images_collection(path_group):
    images_group = []
    for path in path_group:
        images_group.append(get_images(path))
    return images_group

# Get NFT image order of components function:
def select_choices(options, order):
    choices = options
    # Trigger inquirer.
    questions = [
    inquirer.List('size',
                    message="What's the first layer group?",
                    choices= choices,
                ),
    ]
    # Saving sigle answer.
    answer = inquirer.prompt(questions)['size']
    order.append(answer)
    choices.remove(answer) # Removing answer to tigger function again.
    if len(choices) > 0:
        select_choices(choices, order)
    else:
        print(order)

options = get_folder_list_names()
select_choices(options, [])


# Get Images from folder:
def get_images(folder_name):
    image_list = []

    for filename in glob.glob('./images/{}/*.png'.format(folder_name)): #assuming gif
        im=Image.open(filename)
        image_list.append(im)

    return image_list # Array with all images in a folder

image_list = get_images('background')

#print(image_list[0].filename)

raw_input = input

raw_input()