import pygame
import os
from game_const_library import *
import game_library
# cd --> change directory (chapter 11 Lab)
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def main():
    # Initialize Pygame
    pygame.init()
 
    screen = pygame.display.set_mode([screen_width, screen_height])

    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    #pygame.mixer.music.load("a_block_in_space.wav")
    # pygame.mixer.music.set_volume(0.3)
    # pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    # pygame.mixer.music.play() 
    game = game_library.Game()

# -------- Main Program Loop -----------
    while not done:

        done = game.process_events()

        game.run_logic()

        game.display_frame(screen)
    
        # Limit to 60 frames per second
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()