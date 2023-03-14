import block_library
import random

class BadBlock(block_library.Block):
    def reset_pos(self):
        self.rect.y = random.randrange(-30, -19)
        self.rect.x = random.randrange(1280-20)
    def update(self):
        self.rect.y +=1
        if self.rect.y > 740:
            self.reset_pos()