import os
from os import mkdir, path, getcwd
from PIL import Image
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
    for filename in glob.glob('./images/{}/*.png'.format(folder_name)):
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
    return magnitude


folder_list = get_folder_list_names()
images = select_choices(folder_list, [])
default_quantity = get_magnitude(images)

# Create new folder if not exists
def new_folder(name):
    folder_path = path.join(getcwd(), name)
    if not path.isdir(folder_path):
        mkdir(folder_path)
    return folder_path

# Function to generate all combined images
def generate(single_image_list, i):
    width, height = single_image_list[0].size
    canva = Image.new(mode="RGBA", size=(
        width, height), color=(255, 255, 255, 0))
    for image in single_image_list:
        canva.paste(image, (0, 0), mask=image)
    new_folder('generated')
    canva.save('./generated/{}.png'.format(i))
    print(i)
    canva = Image.new(mode="RGBA", size=(width, height), color=(255, 255, 255, 0))

# Random images, every array nested is a entire image composed of one random element of a selected folder (IN ORDER)
def random_images(image_list, quantity=default_quantity):
    assert quantity <= default_quantity
    image_group = []
    single_image = []
    i = 1
    while i <= quantity:
        for images in image_list:
            image = random.choice(images)
            single_image.append(image)

        if single_image not in image_group:
            image_group.append(single_image)
            generate(single_image, i)
            print(i)
            i += 1
        single_image = []
    return image_group


random_images(images)


raw_input = input
raw_input()
