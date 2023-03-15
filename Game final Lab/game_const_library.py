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

#music and sounds
BACKGROUND_MUSIC = []
BACKGROUND_MUSIC.append(pygame.mixer.music.load(os.path.join("music", "a_block_in_space.ogg")))
BACKGROUND_MUSIC.append(pygame.mixer.music.load(os.path.join("music", "through space.ogg")))

BAD = pygame.mixer.Sound(os.path.join("music", "bad_block.ogg"))
GOOD = pygame.mixer.Sound(os.path.join("music", "good_block.ogg"))
BUMP = pygame.mixer.Sound(os.path.join("music", "bump.ogg"))

LASER = []
LASER.append(pygame.mixer.Sound(os.path.join("music", "laserSmall_001.ogg")))
LASER.append(pygame.mixer.Sound(os.path.join("music", "laserLarge_001.ogg")))

    # pygame.mixer.music.set_volume(0.3)
    # pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    # pygame.mixer.music.play() 
#health
HEALTH = []
for i in range(11):
    health = pygame.image.load(os.path.join("resources", f"VIDA_{i}.png"))
    HEALTH.append(health)
   
#backgrounds
BACKGROUND_LIST = []
for i in range(1,5):
    background = pygame.image.load(os.path.join("resources", f"Background-{i} (1).png"))
    BACKGROUND_LIST.append(background)
for i in range(5,11):
    background = pygame.image.load(os.path.join("resources", f"Background-{i} (1).jpg"))
    BACKGROUND_LIST.append(background)



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
