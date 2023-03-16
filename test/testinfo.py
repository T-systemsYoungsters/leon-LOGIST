import pygame

pygame.display.init()

info = pygame.display.Info()

SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h
print(SCREEN_HEIGHT, SCREEN_WIDTH)