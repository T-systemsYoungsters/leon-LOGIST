import pygame
import random
import badblock_library
import goodblock_library
from game_const_library import *
import player_library
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
#good_block = pygame.mixer.Sound("good_block.wav")
#bad_block = pygame.mixer.Sound("bad_block.wav")


class Game():
    block_list = None
    bad_block_list = None
    good_block_list = None
    all_sprites_list = None
    player = None
    game_over = False

    score = 0

    def __init__(self):
        self.score = 0
        self.game_over = False
        # This is a list of 'sprites.' Each block in the program is
    # added to this list. The list is managed by a class called 'Group.'
        self.bad_block_list = pygame.sprite.Group()
        self.good_block_list = pygame.sprite.Group()
        # This is a list of every sprite.
        # All blocks and the player block as well.
        self.all_sprites_list = pygame.sprite.Group()

        # bad blocks
        for i in range(30):
            # This represents a block
            block = badblock_library.BadBlock(asteroid_one)

            # Set a random location for the block
            block.rect.x = random.randrange(screen_width)
            block.rect.y = random.randrange(screen_height)

            # Add the block to the list of objects
            self.bad_block_list.add(block)
            self.all_sprites_list.add(block)

        # good blocks
        for i in range(50):
            # This represents a block
            block = goodblock_library.GoodBLock(gem)

            # Set a random location for the block
            block.rect.x = random.randrange(screen_width-20)
            block.rect.y = random.randrange(screen_height-15)

            # Add the block to the list of objects
            self.good_block_list.add(block)
            self.all_sprites_list.add(block)

        # Create a BLUE player block
        self.player = player_library.Player(PLAYER_SHIP_1)
        self.all_sprites_list.add(self.player)

    def process_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if self.game_over and event.type == pygame.MOUSEBUTTONDOWN:
                self.__init__()
            #background music
            # elif event.type == pygame.constants.USEREVENT:
            #     pygame.mixer.music.load("a_block_in_space.wav")
            #     #pygame.mixer.music.play()    
            # Set the speed based on the key pressed
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.changespeed(-3, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.changespeed(3, 0)
                elif event.key == pygame.K_UP:
                    self.player.changespeed(0, -3)
                elif event.key == pygame.K_DOWN:
                    self.player.changespeed(0, 3)
    
            # Reset speed when key goes up
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.changespeed(3, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.changespeed(-3, 0)
                elif event.key == pygame.K_UP:
                    self.player.changespeed(0, 3)
                elif event.key == pygame.K_DOWN:
                    self.player.changespeed(0, -3)
        return False

    def run_logic(self):

        if not self.game_over:
            self.all_sprites_list.update()
            # See if the player block has collided with anything.
            blocks_hit_list = pygame.sprite.spritecollide(
                self.player, self.good_block_list, True)
            # Check the list of collisions.
            for block in blocks_hit_list:
                self.score += 1
                #good_block.play()

            blocks_hit_list = pygame.sprite.spritecollide(
                self.player, self.bad_block_list, False)
            for block in blocks_hit_list:
                self.score -= 1
                #bad_block.play()
                badblock_library.BadBlock.reset_pos(block)

            if len(self.good_block_list) == 0 or self.score < -10:
                self.game_over = True

    def display_frame(self, screen):

        screen.blit(BACKGROUND_IMAGE_MENU, [0,0])

        if self.game_over:

            game_over_font = pygame.font.SysFont("serif", 25)
            game_over_text = game_over_font.render(
                "Game Over, click to restart", True, WHITE)
            x = (screen_width // 2) - (game_over_text.get_width() // 2)
            y = (screen_height // 2) - (game_over_text.get_height() // 2)
            screen.blit(game_over_text, [x,y])

        if not self.game_over:
            self.all_sprites_list.draw(screen)
            font = pygame.font.Font("C:/Windows/Fonts/RAVIE.TTF", 25)
            text_score = font.render("Score: " +str(self.score), True, WHITE)
            screen.blit(text_score, [5,5])
        pygame.display.flip()
    
    
