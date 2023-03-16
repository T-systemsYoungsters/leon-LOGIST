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
BUTTONS_COLOR = (119, 136, 153)

# Set the height and width of the screen
info = pygame.display.Info()

SCREEN_WIDTH = 1280#info.current_w
SCREEN_HEIGHT = 720#info.current_h


#font
game_menu_font = pygame.font.SysFont("serif", 25)
game_titel_font = pygame.font.SysFont("serif", 35)
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

#spacestations
SPACESTATION_128 = []
SPACESTATION_128.append(pygame.image.load(os.path.join("resources", "Spacestation_1_128.png")))
# for i in range (1,6):
#     SPACESTATION.append(pygame.image.load(os.path.join("resources", f"Spacestation_{i}_128.png")))
# SPACESTATION_256 = []
# for i in range(1,6):
#     SPACESTATION_256.append(pygame.image.load(os.path.join("resources", f"Spacestation_{i}_256.png")))
#bullet
BULLET = pygame.image.load(os.path.join("resources", "bullet_top.png"))
#ships
#player-ships
PLAYER_SHIP_LIST = []
PLAYER_SHIP_1 = pygame.image.load(os.path.join("resources","blueships1.png" ))

#friendly_ships

#enemy-ships
ENEMY_SHIP_LIST = []
for i in range(17):
    ship = pygame.image.load(os.path.join("resources", f"EnemyShip_{i}.png"))
    ENEMY_SHIP_LIST.append(ship)
#effects_ships

#icons

#objects
#good_objects
#bad_objects
gem = pygame.image.load(os.path.join("resources", "gem-1.png"))
asteroid_one = pygame.image.load(os.path.join("resources","asteroid.png"))
