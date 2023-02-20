#Chapter 6: Back to Looping: Lab 6: Loopy Lab

#6.1

# num = 10

# for row in range(1,10):
#     for column in range(row):
#         print(num, end =" ")
#         num +=1
#     print()


#6.2
# n = int(input("Enter number of rows"))


# #first row
# for i in range(n*2):
#     print("o", end = "") 
# print()

# #between
# for i in range(n-2):
#     print("o", end="")
#     for j in range(n*2-2):
#         print(" ", end="")
#     print("o", end="")   
#     print()

# #last row
# for i in range(n*2):
#     print("o", end = "")


#3 
#skip

# n = int(input("Enter the size of the box"))

# #first row
# # for i in range(1, n*2, 2):
# #     print(i,"", end="")
# #     for j in range(i+2, n*2,2):
# #         print(j,"", end="")
# #     for k in range(2*n-1, 0, -2):
# #         print(k,"", end = "")
# #     print()
    
# # for i in range(2*n-1, 0, -2):
# #     print(i)
# #     for j in range(i, n*2,2):
# #         print(j, end="")
# #     print()

#4
#->pygame_base_template.py
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
    for i in range(0,500,15):
        for j in range(0, 700, 15):
            pygame.draw.rect(screen, GREEN, [j+5,i+5,10,10])

    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()