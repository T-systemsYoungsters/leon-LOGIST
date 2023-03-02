import pygame
import random
import os

# cd --> change directory (chapter 11 Lab)
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
 
class Block(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """
 
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its size. """
 
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
 

class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """
 
    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(BLUE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
 
    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y
 
    def update(self):
        """ Find a new position for the player"""
        

        if self.rect.x > screen_width - 15:
            self.rect.x -= 1
            bump.play()
        elif self.rect.x < 0:
            self.rect.x += 1
            bump.play()
        elif self.rect.y > screen_height-15:
            self.rect.y -= 1
            bump.play()
        elif self.rect.y < 0:
            self.rect.y += 1
            bump.play()
        else:
            self.rect.x += self.change_x
            self.rect.y += self.change_y

# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
 
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
bad_block_list = pygame.sprite.Group()
good_block_list = pygame.sprite.Group() 
# This is a list of every sprite. 
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
#bad blocks 
for i in range(50):
    # This represents a block
    block = Block(RED, 20, 15)
 
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
 
    # Add the block to the list of objects
    bad_block_list.add(block)
    all_sprites_list.add(block)
 
#good blocks
for i in range(50):
    # This represents a block
    block = Block(GREEN, 20, 15)
 
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
 
    # Add the block to the list of objects
    good_block_list.add(block)
    all_sprites_list.add(block)
 

# Create a BLUE player block
player = Player(10,10)
all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
 
pygame.mixer.music.load("a_block_in_space.wav")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play() 

good_block = pygame.mixer.Sound("good_block.wav")
bad_block = pygame.mixer.Sound("bad_block.wav")
bump = pygame.mixer.Sound("bump.wav")

font = pygame.font.Font("C:/Windows/Fonts/RAVIE.TTF", 25)

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        #background music
        elif event.type == pygame.constants.USEREVENT:
            pygame.mixer.music.load("a_block_in_space.wav")
            pygame.mixer.music.play()    
        # Set the speed based on the key pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)
 
        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)

    all_sprites_list.update()
    # Clear the screen
    screen.fill(WHITE)
 
    
    
    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(player, good_block_list, True)
    # Check the list of collisions.
    for block in blocks_hit_list:
        score += 1
        good_block.play()


    blocks_hit_list = pygame.sprite.spritecollide(player, bad_block_list, True)
    for block in blocks_hit_list:
        score -= 1
        bad_block.play()
        

    # Draw all the spites
    all_sprites_list.draw(screen)

    text_score = font.render("Score: " +str(score), True, BLACK)
    screen.blit(text_score, [5,5])
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
pygame.quit()
