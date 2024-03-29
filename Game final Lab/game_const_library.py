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
ALICE_BLUE = (240, 248, 255)
MARINE_BLUE = (0,0,128)

# Set the height and width of the screen
info = pygame.display.Info()

SCREEN_WIDTH = 1280#info.current_w
SCREEN_HEIGHT = 720#info.current_h


#font
font = pygame.font.Font("C:/Windows/Fonts/RAVIE.TTF", 25)
game_menu_font = pygame.font.SysFont("serif", 25)
game_titel_font = pygame.font.SysFont("serif", 35)

#music and sounds
BACKGROUND_MUSIC = []
BACKGROUND_MUSIC.append(pygame.mixer.music.load(os.path.join("music", "a_block_in_space.ogg")))
BACKGROUND_MUSIC.append(pygame.mixer.music.load(os.path.join("music", "through space.ogg")))

BAD = pygame.mixer.Sound(os.path.join("music", "bad_block.ogg"))
GOOD = pygame.mixer.Sound(os.path.join("music", "good_block.ogg"))
BUMP = pygame.mixer.Sound(os.path.join("music", "bump.ogg"))
EMPTY = pygame.mixer.Sound(os.path.join("music", "empty_mag.ogg"))
SELECT = pygame.mixer.Sound(os.path.join("music", "select01.ogg"))

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
BULLET_LIST = []
for i in range(12,19):
    BULLET = pygame.image.load(os.path.join("resources", f"{i}.png"))
    BULLET_LIST.append(BULLET)

#player-ships
PLAYER_SHIP_LIST = []
MENU_SHIPS = []

for i in range(1,7):
    ship = pygame.image.load(os.path.join("resources", f"ship1 ({i}).png"))
    PLAYER_SHIP_LIST.append(ship)
    ship = pygame.image.load(os.path.join("resources",f"menu_ship_{i}.png"))
    MENU_SHIPS.append(ship)
    

#objects
gem = pygame.image.load(os.path.join("resources", "gem-1.png"))
ammo_5 = pygame.image.load(os.path.join("resources", "5.png"))
ammo_10 = pygame.image.load(os.path.join("resources", "6.png"))
ASTEROID_LIST = []
for i in range(12):
    asteroid = pygame.image.load(os.path.join("resources",f"asteroid{i}.png"))
    ASTEROID_LIST.append(asteroid)
