import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import glob
import inquirer
import random

images = []

# Get folder list name:


def get_folder_list_names():
    return os.listdir('./images')


# Get Images from folder:
def get_images(folder_name):
    image_list = []
    for filename in glob.glob('./images/{}/*.png'.format(folder_name)):  # assuming gif
        im = Image.open(filename)
        image_list.append(im)

    return image_list  # Array with all images in a folder


# Get ALL images in nested arrays:
def get_images_collection(path_group):
    images_group = []
    for path in path_group:
        images_group.append(get_images(path))
    return images_group


# Get image order of components function:
def select_choices(options, order):
    images = []
    choices = options
    # Trigger inquirer.
    questions = [
        inquirer.List('size',
                      message="What's the first layer group?",
                      choices=choices,
                      ),
    ]
    # Saving sigle answer.
    answer = inquirer.prompt(questions)['size']
    order.append(answer)
    choices.remove(answer)  # Removing answer to tigger function again.
    if len(choices) > 0:
        return select_choices(choices, order)
    else:
        images = get_images_collection(order)
        return images

# Function to get magnitude, in other words, ALL POSSIBLE IMAGES COMBINATIONS.
def get_magnitude(image_list):
    magnitude = 1
    for image_group in image_list:
        magnitude *= len(image_group)
    print(magnitude)


# Random images, every array nested is a entire image composed of one random element of a selected folder (IN ORDER)
def random_images(image_list):
    image_group = []
    for images in image_list:
        image = random.choice(images)
        image_group.append(image)
    return image_group


folder_list = get_folder_list_names()
images = select_choices(folder_list, [])
get_magnitude(images)


nft = random_images(images)


raw_input = input

raw_input()
