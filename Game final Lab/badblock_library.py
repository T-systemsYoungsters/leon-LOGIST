import block_library
import random

class BadBlock(block_library.Block):
    def __init__(self, x,y, object):
        block_library.Block.__init__(self, object)
        self.x = x
        self.y = y
    def reset_pos(self):
        self.rect.y = random.randrange(-30, -19)
        self.rect.x = random.randrange(1280-20)
    def update(self):
        self.rect.y += self.x
        self.rect.y += self.y
        if self.rect.y > 740:
            self.reset_pos()