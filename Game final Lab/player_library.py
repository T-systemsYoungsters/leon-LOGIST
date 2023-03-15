import pygame
from game_const_library import *
import os
pygame.init()
# cd --> change directory (chapter 11 Lab)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
#bump = pygame.mixer.Sound("bump.wav")

class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """
 
    # -- Methods
    def __init__(self, ship):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()

        #player stats:
        self.health = 50
        self.boost = 20
        # Set height, width
        self.image = ship
        self.rect = self.image.get_rect() 
        
        self.rect.x = (self.image.get_width()+SCREEN_WIDTH) // 2
        self.rect.y = (self.image.get_width()+SCREEN_HEIGHT) // 2
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
        

        if self.rect.x > SCREEN_WIDTH - 15:
            self.rect.x -= 1
            BUMP.play()
        elif self.rect.x < 0:
            self.rect.x += 1
            BUMP.play()
        elif self.rect.y > SCREEN_HEIGHT-15:
            self.rect.y -= 1
            BUMP.play()
        elif self.rect.y < 0:
            self.rect.y += 1
            BUMP.play()
        else:
            self.rect.x += self.change_x
            self.rect.y += self.change_y
        
        