import block_library
from game_const_library import *
import random

class EnemyShips(block_library.Block):
    count = 0
    ranx = 0
    rany = 1
    def update(self):
        
        if self.count > 120:
            self.count = 0
            self.ranx = random.randrange(-1,2)
            self.rany = random.randrange(-1,2)

        if self.rect.y > SCREEN_HEIGHT :
            self.rany = -1

        elif self.rect.y < 0 :
            self.rany = +1

        if self.rect.x > SCREEN_WIDTH :
            self.ranx = -1

        elif self.rect.x < 0 :
            self.ranx = +1

        self.rect.x += self.ranx
        self.rect.y += self.rany

        self.count += 1