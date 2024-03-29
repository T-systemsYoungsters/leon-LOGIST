import block_library
from game_const_library import *
import random

class BadBlock(block_library.Block):
    def __init__(self, x,y, object):
        block_library.Block.__init__(self, object)
        self.x = x
        self.y = y
    def reset_pos(self):
        if self.x < 0 and self.y > 0:
            self.rect.x = random.randrange(50, 2*SCREEN_WIDTH)
            self.rect.y = random.randrange(-100, 0)
        elif self.x != 0:
            self.rect.x = random.randrange(-30, -19)
            self.rect.y = random.randrange(720-20)
        elif self.y != 0:
            self.rect.y = random.randrange(-50, 0)
            self.rect.x = random.randrange(1280-20)
    def update(self):
        self.rect.x += self.x
        self.rect.y += self.y
        if self.x < 0 and self.y > 0:
            if self.rect.y > 740 or self.rect.x < -50:
                self.reset_pos()
        elif self.x != 0:
            if  self.rect.x > 1400 or self.rect.x < - 300:
                self.reset_pos()
        elif self.y != 0:
            if self.rect.y > 800 or self.rect.y < -200:
                self.reset_pos()
        
        