import pygame
pygame.init()
import random

GRASS = (0,100,0)
WATER = (0,0,128)
WAVE  = (65, 105, 225)
SKY   = (0,0,255)
STAR  = (255,215,0)
MOON  = (240, 230, 140)
MOON_1= (189, 183, 107)
HOUSE = (10,10,10)

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Picasso?")

pi = 3.141592653

# ------- Main Program Loop -------

done = False

# used to manage how fast the screen updates
clock=pygame.time.Clock()


star_list =[]
for i in range(30):
    x = random.randrange(0, 700, 50)
    y = random.randrange(0,300,50)
    line =random.randrange(1,3)
    star_list.append([x,y,line])

while not done:
    
    #all event processing should go below this comment
    
    for event in pygame.event.get():     #User did something

        if event.type == pygame.QUIT:        #If user clicked close
            done = True                     #flag that we are done so exit the loop

    #all event processing should go above this comment


    #all game logic should go below this comment
            
    #all game logic should go above this comment
            

    #all code to draw should go below this comment
    #Himme = ganzer Hintergrund
    screen.fill(SKY)

    #Mond
    pygame.draw.circle(
    screen,             # Surface to draw on
    MOON,    # Color in RGB Fashion
    [600, 50],         # Center
    40,                 # Radius
    )
    #Mondkrater
    pygame.draw.circle(screen, MOON_1, [615, 25], 7)
    pygame.draw.circle(screen, MOON_1, [580, 65], 2)
    pygame.draw.circle(screen, MOON_1, [585, 30], 3)
    pygame.draw.circle(screen, MOON_1, [605, 50], 5)
    pygame.draw.circle(screen, MOON_1, [612, 70], 4)

    #Sterne
    """
    for i in range(3):
        x = random.randrange(0,550, 50)
        y = random.randrange(0,100, 20)
        line =random.randrange(1,3)
        pygame.draw.line(screen, STAR, [x+100,y+95],[x+100,y+105],line)
        pygame.draw.line(screen, STAR, [x+95,y+105],[x+105,y+95],line)
        pygame.draw.line(screen, STAR, [x+95,y+100],[x+105,y+100],line)
        pygame.draw.line(screen, STAR, [x+95,y+95],[x+105,y+105],line)
"""
    for item in star_list:
        
        
        x=item[0]
        y=item[1]
        
        line =item[2]
        pygame.draw.line(screen, STAR, [x+10,y+5],[x+10,y+15],line)
        pygame.draw.line(screen, STAR, [x+5,y+15],[x+15,y+5],line)
        pygame.draw.line(screen, STAR, [x+5,y+10],[x+15,y+10],line)
        pygame.draw.line(screen, STAR, [x+5,y+5],[x+15,y+15],line)

    #Wasser
    pygame.draw.rect(screen, WATER, [0,300, 700, 350])

    
    
    #Boden
    pygame.draw.rect(screen, GRASS, [0,400, 700,500])

    #Zaun?
    for x in range(0, 300, 20):
        pygame.draw.line(screen, HOUSE, [x+0, 400], [0+x, 380], 4)
    pygame.draw.line(screen, HOUSE, [0,382],[300,382],2)
    
    #Haus
    pygame.draw.rect(screen, HOUSE, [330, 250, 350,150])
    pygame.draw.polygon(screen, HOUSE, [[330, 250],[490,100],[679,250]])
    """
    for i in range(0,100,20):
        pygame.draw.rect(screen, STAR, [360, 265, 15,25])
    """
    pygame.draw.rect(screen, STAR, [360, 265, 15,25])
    pygame.draw.rect(screen, STAR, [440, 300, 15,25])
    pygame.draw.rect(screen, STAR, [540, 350, 15,25])
    pygame.draw.rect(screen, STAR, [580, 265, 15,25])
    
    pygame.display.flip()   # zeigt das gezeichnete auf dem Bildschirm an
    #all code to draw should go above this comment

    #limit tp frames per second
            
    clock.tick(20)

pygame.quit()


