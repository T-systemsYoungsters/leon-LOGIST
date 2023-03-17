import pygame
from game_const_library import *
import math
class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, object, start_x,start_y,dest_x,dest_y):
        pygame.sprite.Sprite.__init__(self)

        self.image = object 
        # self.image = pygame.Surface[4,10]
        # self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y

        self.floating_point_x = start_x
        self.floating_point_y = start_y

        # Calculation the angle in radians between the start points
        # and end points. This is the angle the bullet will travel.
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff);

        velocity = 5 #speed of bullet
        self.change_x = math.cos(angle) * velocity
        self.change_y = math.sin(angle) * velocity
    def update(self):
        
        # The floating point x and y hold our more accurate location.
        self.floating_point_y += self.change_y
        self.floating_point_x += self.change_x
 
        # The rect.x and rect.y are converted to integers.
        self.rect.y = int(self.floating_point_y)
        self.rect.x = int(self.floating_point_x)
 
        # If the bullet flies of the screen, get rid of it.
        if self.rect.x < 0 or self.rect.x > SCREEN_WIDTH or self.rect.y < 0 or self.rect.y > SCREEN_HEIGHT:
            self.kill()
