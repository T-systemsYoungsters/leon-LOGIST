import pygame
import os
path = os.getcwd()
os.chdir(os.path.dirname(os.path.abspath(__file__)))
pygame.init()
screen = pygame.display.set_mode([1130, 647])
pygame.display.set_caption("My Game")
time=pygame.time.Clock()
done = False
def cloud(screen,x,y):
    pygame.draw.circle(screen, (226,0,116), (0+x, 0+y), 25)
    pygame.draw.circle(screen, (226,0,116), (20+x, 0+y), 25)
    pygame.draw.circle(screen, (226,0,116), (40+x, 0+y), 25)
    pygame.draw.circle(screen, (226,0,116), (60+x, 0+y), 25)
    pygame.draw.circle(screen, (226,0,116), (80+x, 0+y), 25)
    pygame.draw.circle(screen, (226,0,116), (10+x, 10+y), 25)
    pygame.draw.circle(screen, (226,0,116), (40+x, 20+y), 25)
    pygame.draw.circle(screen, (226,0,116), (70+x, 10+y), 25)
    pygame.draw.circle(screen, (226,0,116), (10+x, -10+y), 25)
    pygame.draw.circle(screen, (226,0,116), (40+x, -20+y), 25)
    pygame.draw.circle(screen, (226,0,116), (70+x, -10+y), 25)
background_image = pygame.image.load("background.jpg").convert()
pygame.mouse.set_visible(0)
click_sound = pygame.mixer.Sound("laser5.ogg")
while done==False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()
    screen.blit(background_image, [0, 0])
    mouse=pygame.mouse.get_pos()
    x=mouse[0]
    y=mouse[1]
    cloud(screen, x, y)
    pygame.display.flip()
time.tick(20)
pygame.quit()