

import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
STRASSE = (64,64,64)
LIGHT_BLUE =(0,191,255)

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

    #wings left
    pygame.draw.polygon(screen, LIGHT_BLUE,[[x+3,y+60],[x-70, y+135],[x-65,y+140],[x+2,y+125]] )
    pygame.draw.polygon(screen, BLACK,[[x+3,y+60],[x-70, y+135],[x-65,y+140],[x+2,y+125]], 2)

    # pygame.draw.polygon(screen, LIGHT_BLUE,[[x+35-13,y+220-40],[x+10-13, y+230-40],[x+15-13,y+232-40],[x+32-10,y+228-40]] )
    # pygame.draw.polygon(screen, BLACK,[[x+35-13,y+220-40],[x+10-13, y+230-40],[x+15-13,y+232-40],[x+32-10,y+228-40]] ,2)
    #wings right
    pygame.draw.polygon(screen, LIGHT_BLUE,[[x+80-3,y+60],[x+80+70, y+135],[x+80+65,y+140],[x-2+80,y+125]] )
    pygame.draw.polygon(screen, BLACK,[[x+80-3,y+60],[x+80+70, y+135],[x+80+65,y+140],[x-2+80,y+125]],2 )

    #pygame.draw.polygon(screen, LIGHT_BLUE,[[x-30,20],[x-15, 30],[x-20,32],[x-32,28]] )

    #pygame.draw.polygon(screen, LIGHT_BLUE,[[600,400],[550, 450],[555,455],[600,425]], 2)

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (1280, 720)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Planerun")

done = False
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                plane_x_speed = -3
            if event.key == pygame.K_RIGHT:
                plane_x_speed = 3
            if event.key == pygame.K_UP:
                plane_y_speed = -2
            if event.key == pygame.K_DOWN:
                plane_y_speed = 2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                plane_x_speed = 0
            if event.key == pygame.K_RIGHT:
                plane_x_speed = 0
            if event.key == pygame.K_UP:
                plane_y_speed = 0
            if event.key == pygame.K_DOWN:
                plane_y_speed = 0

    # --- Game logic should go here
    plane_x_coord += plane_x_speed
    plane_y_coord += plane_y_speed   
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(STRASSE)
 
    for i in range(0, 720, 30):
        draw_streifen(i)
    
    draw_plane(plane_x_coord, plane_y_coord)

    pygame.display.flip()
    
    
    clock.tick(60)
 

pygame.quit()