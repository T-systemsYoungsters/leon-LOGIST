import pygame
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()
# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)

# Set the height and width of the screen
screen_width = 1280
screen_height = 720

background_image_menu = pygame.image.load(os.path.join("resc", "")).convert()