import pygame
import random
import math

pygame.init()

WHITE = (255,255,255)
GRASS = (0,100,0)
WATER = (0,0,128)
WAVE  = (65, 105, 225)
SKY   = (0,0,255)
STAR  = (255,215,0)
MOON  = (240, 230, 140)
MOON_1= (189, 183, 107)
HOUSE = (10,10,10)
STRASSE = (64,64,64)
LIGHT_BLUE =(0,191,255)
LIGHT_RED =(255,0,0)
LIGHT_GREEN=(0,255,0)
LIGHT_YELLOW = (255,255,0)

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Picasso?")

pi = 3.141592653

light_count = 0

font = pygame.font.Font(None,25)
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

schnuppe_x = 0
schnuppe_y= 0

ufo_x = random.randrange(1, 690)
ufo_y = 2

#change sternschnuppe
schnuppe_change_x = 3
schnuppe_change_y = 0.5

#change sat
ufo_change_x = 2
ufo_change_y = 0.75

angle =0

PI = 3.141592653

while not done:
    
    #all event processing should go below this comment
    
    for event in pygame.event.get():     #User did something

        if event.type == pygame.QUIT:        #If user clicked close
            done = True                     #flag that we are done so exit the loop

    #all game logic should go below this comment
    if light_count < 40:
        light = LIGHT_BLUE
    elif light_count < 80:
        light = LIGHT_RED
    else:
        light_count = 0
    
    if ufo_x > 699 or ufo_x<1:
        ufo_change_x *=-1
    if ufo_y > 299 or ufo_y < 1:
        ufo_change_y*=-1

    if light_count < 20:
        color_ufo_1 = LIGHT_RED
        color_ufo_2 = LIGHT_GREEN
    elif light_count < 40:
        color_ufo_1 = LIGHT_GREEN
        color_ufo_2 = LIGHT_BLUE
    elif light_count < 60:
        color_ufo_1 = LIGHT_BLUE
        color_ufo_2 = LIGHT_YELLOW
    elif light_count < 80:
        color_ufo_1 = LIGHT_YELLOW
        color_ufo_2 = LIGHT_RED
    
    #x und y von dem Licht, welches um den Mond kreist
    
    light_moon_x = 45*math.sin(angle) +600
    light_moon_y = 45*math.cos(angle) +50

    angle += 0.03

    if angle > 2* PI:
        angle = angle -2*PI

    light_count +=1         

    #all code to draw should go below this comment
    #Himmel = ganzer Hintergrund
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
    for item in star_list:
        x=item[0]
        y=item[1]
        
        line =item[2]
        pygame.draw.line(screen, STAR, [x+10,y+5],[x+10,y+15],line)
        pygame.draw.line(screen, STAR, [x+5,y+15],[x+15,y+5],line)
        pygame.draw.line(screen, STAR, [x+5,y+10],[x+15,y+10],line)
        pygame.draw.line(screen, STAR, [x+5,y+5],[x+15,y+15],line)
    
    #Sternschnuppe
    pygame.draw.line(screen, STAR, [schnuppe_x+5,schnuppe_y],[schnuppe_x+5,schnuppe_y+10],1)
    pygame.draw.line(screen, STAR, [schnuppe_x,schnuppe_y+10],[schnuppe_x+10,schnuppe_y],1)
    pygame.draw.line(screen, STAR, [schnuppe_x,schnuppe_y+5],[schnuppe_x+10,schnuppe_y+5],1)
    pygame.draw.line(screen, STAR, [schnuppe_x,schnuppe_y],[schnuppe_x+10,schnuppe_y+10],1)
    pygame.draw.polygon(screen,STAR, [[schnuppe_x,schnuppe_y],[schnuppe_x-5,schnuppe_y-1],[schnuppe_x-4,schnuppe_y-3]],1)

    schnuppe_x += schnuppe_change_x
    schnuppe_y += schnuppe_change_y

    #ufo
    pygame.draw.circle(screen, color_ufo_1, [ufo_x, ufo_y], 2)
    pygame.draw.circle(screen, color_ufo_1, [ufo_x+1, ufo_y+1], 2)

    #Licht um den Mond
    pygame.draw.circle(screen, color_ufo_1, [light_moon_x, light_moon_y], 2)

    ufo_x += ufo_change_x
    ufo_y += ufo_change_y
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
   
    pygame.draw.rect(screen, STAR, [360, 265, 15,25])
    pygame.draw.rect(screen, STAR, [440, 300, 15,25])
    pygame.draw.rect(screen, STAR, [540, 350, 15,25])
    pygame.draw.rect(screen, STAR, [580, 265, 15,25])
    
    #Strasse
    pygame.draw.rect(screen, STRASSE,[0, 440,700,100] )
    for i in range(0, 800, 50):
        pygame.draw.line(screen, WHITE, [-5+i, 490], [15+i,490],3)

    #AUTO
    pygame.draw.rect(screen, HOUSE, [130, 430, 200,35])
    pygame.draw.circle(screen, HOUSE, [160, 470], 20)
    pygame.draw.circle(screen, HOUSE, [300, 470], 20)
    pygame.draw.polygon(screen,HOUSE, [[160,440],[180,390],[315,390],[325,440]])
    pygame.draw.circle(screen, light, [200, 385], 10)
    pygame.draw.circle(screen, light, [290, 385], 10)
    text= font.render("Police", True, WHITE)

    screen.blit(text, [205, 435])
    pygame.display.flip()   # zeigt das gezeichnete auf dem Bildschirm an

    #limit tp frames per second     
    clock.tick(60)

pygame.quit()


