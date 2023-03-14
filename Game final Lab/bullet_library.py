import pygame
from game_const_library import *
class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, object):
        pygame.sprite.Sprite.__init__(self)

        self.image = object 
        # self.image = pygame.Surface[4,10]
        # self.image.fill(RED)
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.y -= 1