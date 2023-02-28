

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

def draw_helicopter(x,y):

    #body
    pygame.draw.circle(screen, GREY,[x+50,y+12.5],10)
    pygame.draw.circle(screen, BLACK,[x+50,y+12.5],10,2)
    pygame.draw.rect(screen, RED, [x,y,50,25])
    pygame.draw.rect(screen, BLACK, [x,y,50,25],2)
    pygame.draw.rect(screen, GREY, [x+30, y+5,15,10])
    pygame.draw.rect(screen, GREY, [x+10, y+5,15,10])
    pygame.draw.rect(screen, RED, [x-25,y+5,30,7])
    pygame.draw.rect(screen, BLACK, [x-25,y+5,30,7], 2)
    
    #rotor
    pygame.draw.line(screen,BLACK, [x+25,y],[x+25,y-7],3)
    pygame.draw.line(screen, BLACK, [x-10, y-10], [x+60,y-10],4)

    #backrotor
    pygame.draw.circle(screen,RED, [x-25,y+8],8,)
    pygame.draw.circle(screen,BLACK, [x-25,y+8],8,4)

    pygame.draw.line(screen,BLACK, [x+5,y+25],[x+5, y+35],2)
    pygame.draw.line(screen,BLACK, [x+45,y+25],[x+45, y+35],2)
    pygame.draw.line(screen,BLACK,[x-5,y+37], [x+60, y+37],3)



pygame.init()
 
# Set the width and height of the screen [width, height]
size = (1280, 720)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Planerun")

done = False
clock = pygame.time.Clock()

pygame.mouse.set_visible(0)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
        
            if event.key == pygame.K_LEFT:
                plane_x_speed = -8
            if event.key == pygame.K_UP:
                plane_y_speed = -5
            
            if event.key == pygame.K_RIGHT:
                plane_x_speed = 8
            if event.key == pygame.K_DOWN:
                plane_y_speed = 5
            
            

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
        
    if plane_x_coord > 1120 and plane_x_speed > 0:
        plane_x_speed = 0
    elif plane_x_coord < 80 and plane_x_speed < 0:
        plane_x_speed = 0
    if plane_y_coord > 515 and plane_y_speed > 0:
        plane_y_speed = 0
    elif plane_y_coord < 5 and plane_y_speed < 0:
        plane_y_speed = 0
    plane_x_coord += plane_x_speed
    plane_y_coord += plane_y_speed  

    pos = pygame.mouse.get_pos()
    helicopter_x_coord = pos[0]
    helicopter_y_coord = pos[1]

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(STRASSE)
 
    for i in range(0, 720, 30):
        draw_streifen(i)
    
    draw_plane(plane_x_coord, plane_y_coord)

    draw_helicopter(helicopter_x_coord,helicopter_y_coord)

    pygame.display.flip()
    
    
    clock.tick(60)
 

pygame.quit()