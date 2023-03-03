import pygame
from game_const_library import *
import os
pygame.init()
# cd --> change directory (chapter 11 Lab)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
bump = pygame.mixer.Sound("bump.wav")

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