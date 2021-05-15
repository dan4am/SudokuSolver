import pygame
import os
import time
######################
# Define some colors #
######################

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (220, 220, 220)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
_image_library = {}
jump_sprites = []
walk_sprites = []


def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image

def fill_sprites():
    for i in range (1,10):
        walk_sprites.append(get_image("Sprites/"+str(i)+".png"))
    # for j in range (1,9):
    #     jump_sprites.append(get_image("Sprites/JUMPING"+str(j)+"j.png"))


