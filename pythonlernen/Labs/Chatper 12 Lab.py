import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class Rectangle():
    def __init__(self):
        self.x = random.randrange(701)
        self.y = random.randrange(501)
        self.height = random.randrange(20, 71)
        self.width = random.randrange(20, 71)
        self.change_x = random.randrange(-3, 4)
        self.change_y = 0
        self.color = (random.randrange(256), random.randrange(
            256), random.randrange(256))

    def draw(self):
        pygame.draw.rect(screen, self.color, [
                         self.x, self.y, self.width, self.height])

    def move(self):
        self.x += self.change_x
        self.y += self.change_y


class Ellipse(Rectangle):
    def draw(self):
        pygame.draw.ellipse(screen, self.color, [
                            self.x, self.y, self.width, self.height])


pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

my_list = []
for i in range(100):
    my_object = Rectangle()
    my_list.append(my_object)
for i in range(100):
    my_object = Ellipse()
    my_list.append(my_object)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    my_object.move()

    # --- Drawing should go here
    screen.fill(BLACK)

    for i in range(len(my_list)):
        my_list[i].draw()
        my_list[i].move()
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
