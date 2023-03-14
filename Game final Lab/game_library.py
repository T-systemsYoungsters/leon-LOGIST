import pygame
import random
import badblock_library
import goodblock_library
import bullet_library
from game_const_library import *
import player_library
import enemy_ships_library
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
#good_block = pygame.mixer.Sound("good_block.wav")
#bad_block = pygame.mixer.Sound("bad_block.wav")


class Game():
    block_list = None
    bad_block_list = None
    good_block_list = None
    bullet_list = None
    enemy_list = None
    all_sprites_list = None
    player = None
    enemy = 0
    game_over = False
    health_bar = 10
    score = 0

    def __init__(self):
        health_bar = 10
        self.score = 0
        self.game_over = False
        # This is a list of 'sprites.' Each block in the program is
    # added to this list. The list is managed by a class called 'Group.'
        self.bad_block_list = pygame.sprite.Group()
        self.good_block_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.bullet_list = pygame.sprite.Group()
        # This is a list of every sprite.
        # All blocks and the player block as well.
        self.all_sprites_list = pygame.sprite.Group()

        # bad blocks
        for i in range(20):
            # This represents a block
            block = badblock_library.BadBlock(asteroid_one)

            # Set a random location for the block
            block.rect.x = random.randrange(SCREEN_WIDTH)
            block.rect.y = random.randrange(SCREEN_HEIGHT)

            # Add the block to the list of objects
            self.bad_block_list.add(block)
            self.all_sprites_list.add(block)

        # good blocks
        for i in range(50):
            # This represents a block
            block = goodblock_library.GoodBLock(gem)

            # Set a random location for the block
            block.rect.x = random.randrange(SCREEN_WIDTH-20)
            block.rect.y = random.randrange(SCREEN_HEIGHT-15)

            # Add the block to the list of objects
            self.good_block_list.add(block)
            self.all_sprites_list.add(block)

        for i in range(3):
            enemy = enemy_ships_library.EnemyShips(ENEMY_SHIP_LIST[i])
            enemy.rect.x = random.randrange(SCREEN_WIDTH)
            enemy.rect.y = random.randrange(SCREEN_HEIGHT)
            self.all_sprites_list.add(enemy)

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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                    bullet = bullet_library.Bullet(BULLET)
                    bullet.rect.x = self.player.rect.x
                    bullet.rect.y = self.player.rect.y
                    
                    self.all_sprites_list.add(bullet)
                    self.bullet_list.add(bullet)   

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.player.changespeed(3, 0)
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.player.changespeed(0, -3)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.player.changespeed(0, 3)
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.player.changespeed(-3, 0)

            # Reset speed when key goes up
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.player.changespeed(3, 0)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.player.changespeed(-3, 0)
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.player.changespeed(0, 3)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.player.changespeed(0, -3)
        return False

    def run_logic(self):

        if not self.game_over:
            self.all_sprites_list.update()
            # See if the player block has collided with anything.
            blocks_hit_list = pygame.sprite.spritecollide(
                self.player, self.good_block_list, True)

            for bullet in self.bullet_list:
                bullet_block_hit_list = pygame.sprite.spritecollide(bullet, self.bad_block_list, True)
                for block in bullet_block_hit_list:
                    self.bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)
                if bullet.rect.y < -10:
                    self.bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)


            # Check the list of collisions.
            for block in blocks_hit_list:
                self.score += 1
                #good_block.play()

            blocks_hit_list = pygame.sprite.spritecollide(
                self.player, self.bad_block_list, False)
            for block in blocks_hit_list:
                self.score -= 1
                self.player.health -= 5
                self.health_bar -= 1
                if self.player.health <= 0:
                    self.game_over = True
                #bad_block.play()
                badblock_library.BadBlock.reset_pos(block)

            if len(self.good_block_list) == 0 or self.score <= -10:
                self.game_over = True
            
            

            

    def display_frame(self, screen):

        screen.blit(BACKGROUND_IMAGE_MENU, [0,0])

        if self.game_over:

            game_over_font = pygame.font.SysFont("serif", 25)
            game_over_text = game_over_font.render(
                "Game Over, click to restart", True, WHITE)
            x = (SCREEN_WIDTH // 2) - (game_over_text.get_width() // 2)
            y = (SCREEN_HEIGHT // 2) - (game_over_text.get_height() // 2)
            screen.blit(game_over_text, [x,y])

        if not self.game_over:
            self.all_sprites_list.draw(screen)
            font = pygame.font.Font("C:/Windows/Fonts/RAVIE.TTF", 25)
            text_health = font.render("Health: " +str(self.player.health), True, WHITE)
            text_score = font.render("Score: " +str(self.score), True, WHITE)
            screen.blit(text_score, [5,5])
            
            screen.blit(HEALTH[self.health_bar], [self.player.rect.x, self.player.rect.y - 4])
        pygame.display.flip()
    
    
