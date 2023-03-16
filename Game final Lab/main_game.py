import pygame
import os
from game_const_library import *
import game_library
# cd --> change directory (chapter 11 Lab)
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def main():
    # Initialize Pygame
    pygame.init()
 
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    game = game_library.Game()

# -------- Main Program Loop -----------
    while not done:

        done = game.process_events()

        game.run_logic()

        game.display_frame(screen)
    
        # Limit to 60 frames per secondw
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()