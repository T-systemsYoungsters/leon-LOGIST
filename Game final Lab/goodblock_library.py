import block_library
import random

class GoodBLock(block_library.Block):
    def update(self):
        if self.rect.x > 685:
            self.rect.x -= random.randrange(4)
        elif self.rect.x < 0:
            self.rect.x += random.randrange(4)
        elif self.rect.y > 385:
            self.rect.y -= random.randrange(4)
        elif self.rect.y < 0:
            self.rect.y += random.randrange(4)
        else:
            self.rect.x += random.randrange(-3,4)
            self.rect.y += random.randrange(-3,4)