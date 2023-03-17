import block_library
from game_const_library import *
import random

class EnemyShips(block_library.Block):
    count = 0
    health = 3
    def __init__(self, x,y, object):
        block_library.Block.__init__(self, object)
        self.health = 3
        self.x = x
        self.y = y

    def update(self):

        self.rect.x += self.x
        self.rect.y += self.y

        if self.health <= 0:
            self.kill()
    