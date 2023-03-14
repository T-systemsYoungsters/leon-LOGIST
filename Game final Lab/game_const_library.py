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
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

#music

#health
HEALTH = []
for i in range(11):
    health = pygame.image.load(os.path.join("resources", f"VIDA_{i}.png"))
    HEALTH.append(health)
   
#backgrounds
BACKGROUND_LIST = []
BACKGROUND_IMAGE_MENU = pygame.image.load(os.path.join("resources", "Background-1.png"))
# BACKGROUND_IMAGE_1 = pygame.image.load(os.path.join("resources", "Background-2.png"))
# BACKGROUND_IMAGE_2 = pygame.image.load(os.path.join("resources", "Background-3.png"))
# BACKGROUND_IMAGE_3 = pygame.image.load(os.path.join("resources", "Background-4.png"))
# BACKGROUND_IMAGE_4 = pygame.image.load(os.path.join("resources", "Background-5.jpg"))
# BACKGROUND_IMAGE_5 = pygame.image.load(os.path.join("resources", "Background-6.jpg")) 
# BACKGROUND_IMAGE_6 = pygame.image.load(os.path.join("resources", "Background-7.jpg"))
# BACKGROUND_IMAGE_7 = pygame.image.load(os.path.join("resources", "Background-8.jpg"))
# BACKGROUND_IMAGE_8 = pygame.image.load(os.path.join("resources", "Background-9.jpg"))
# BACKGROUND_IMAGE_9 = pygame.image.load(os.path.join("resources", "Background-10.jpg"))
# BACKGROUND_IMAGE_10 = pygame.image.load(os.path.join("resources", "Background-11.png"))

#bullet
BULLET = pygame.image.load(os.path.join("resources", "bullet_top.png"))
#ships
#player-ships
PLAYER_SHIP_LIST = []
PLAYER_SHIP_1 = pygame.image.load(os.path.join("resources","blueships1.png" ))

#friendly_ships

#enemy-ships
ENEMY_SHIP_LIST = []
for i in range(3):
    ship = pygame.image.load(os.path.join("resources", f"EnemyShip_{i}.png"))
    ENEMY_SHIP_LIST.append(ship)
#effects_ships

#icons

#objects
#good_objects
#bad_objects
gem = pygame.image.load(os.path.join("resources", "gem-1.png"))
asteroid_one = pygame.image.load(os.path.join("resources","asteroid.png"))
