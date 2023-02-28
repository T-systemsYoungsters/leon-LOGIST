

import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
STRASSE = (64,64,64)
LIGHT_BLUE =(0,191,255)
GREY = (224,224,224)

pi = 3.141592653

plane_x_coord = 600
plane_y_coord = 300

plane_x_speed = 0
plane_y_speed = 0 





def draw_streifen(i):
    pygame.draw.line(screen, WHITE, [638,0+i],[638, 20 + i], 4 )


def draw_plane(x,y):
    #body
    pygame.draw.ellipse(screen, LIGHT_BLUE,[x,y, 80, 200])
    pygame.draw.ellipse(screen, BLACK,[x,y, 80, 200],2)
    pygame.draw.arc(screen, WHITE, [x+30, y+15, 20,20], 2*pi,pi, 4)

    #wing left
    pygame.draw.polygon(screen, LIGHT_BLUE,[[x+3,y+60],[x-70, y+135],[x-65,y+140],[x+2,y+125]] )
    pygame.draw.polygon(screen, BLACK,[[x+3,y+60],[x-70, y+135],[x-65,y+140],[x+2,y+125]], 2)

    #wing right
    pygame.draw.polygon(screen, LIGHT_BLUE,[[x+80-3,y+60],[x+80+70, y+135],[x+80+65,y+140],[x-2+80,y+125]] )
    pygame.draw.polygon(screen, BLACK,[[x+80-3,y+60],[x+80+70, y+135],[x+80+65,y+140],[x-2+80,y+125]],2 )

    #windows
    for i in range(0, 80, 10):
        pygame.draw.rect(screen, WHITE, [x+10, y+50 +i,5,5])
        pygame.draw.rect(screen, WHITE, [x+65, y+50 +i,5,5])


pygame.init()
 
# Set the width and height of the screen [width, height]
size = (1280, 720)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Planerun")

done = False
clock = pygame.time.Clock()

pygame.mouse.set_visible(0)

background_image = pygame.image.load("sky.jpg").convert()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # --- Game logic should go here
        
    

    pos = pygame.mouse.get_pos()
    plane_x_coord = pos[0]
    plane_y_coord = pos[1]

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.bit(background_image, [0,0])
   
    
    draw_plane(plane_x_coord, plane_y_coord)
    pygame.display.flip()
    
    
    clock.tick(60)
 

pygame.quit()