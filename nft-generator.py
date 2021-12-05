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
    return magnitude


folder_list = get_folder_list_names()
images = select_choices(folder_list, [])
default_quantity = get_magnitude(images)

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
            i += 1
        single_image = []
    return image_group


nft = random_images(images)

# Create new folder if not exists
def new_folder(name):
    folder_path = path.join(getcwd(), name)
    if not path.isdir(folder_path):
        mkdir(folder_path)
    return folder_path

def generate(image_list):
    width, height = image_list[0][0].size
    i = 1
    canva = Image.new(mode="RGBA", size=(
        width, height), color=(255, 255, 255, 0))
    for images in image_list:
        for image in images:
            canva.paste(image, (0, 0), mask=image)
        new_folder('generated')
        canva.save('./generated/{}.png'.format(i))
        i += 1
        canva = Image.new(mode="RGBA", size=(
            width, height), color=(255, 255, 255, 0))
    print('Congratulations.')
    print('You have generate {} unique NFT.'.format(i-1))
    print('Press any key to close.')


generate(nft)

raw_input = input
raw_input()
