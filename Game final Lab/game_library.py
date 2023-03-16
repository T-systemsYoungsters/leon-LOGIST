import pygame
import random
import badblock_library
import goodblock_library
import bullet_library
from game_const_library import *
import player_library
import enemy_ships_library
import os
import time

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
    flag = 0
    #game_over = False
    game_state = 0  # (0:Startscreen, 1:Play Level1, 8:Game Won,9:Game Over)
    health_bar = 10
    score = 0
    mouse_pos = []

    def __init__(self):
        self.health_bar = 10
        self.score = 0
        #self.game_over = False
        self.game_state = 0
        self.flag = 0

        # BACKGROUND_MUSIC[0]
        # pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
        # pygame.mixer.music.play()
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
            if self.game_state == 9 and event.type == pygame.MOUSEBUTTONDOWN:
                self.__init__()
                self.health_bar = 10
            elif self.game_state == 0 and event.type == pygame.MOUSEBUTTONDOWN and self.mouse_x<SCREEN_WIDTH/2+100 and self.mouse_x > SCREEN_WIDTH/2-100 and self.mouse_y > SCREEN_HEIGHT/2-50 and self.mouse_y < SCREEN_HEIGHT/2:
                self.game_state = 1
           
            #elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.game_state == 8:
            #    self.game_state = new level
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and self.game_state == 8:
                self.game_state = 0 #main menu

            elif event.type == pygame.MOUSEBUTTONDOWN:
                bullet = bullet_library.Bullet(BULLET)
                bullet.rect.x = self.player.rect.x
                bullet.rect.y = self.player.rect.y
                LASER[0].play()
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
        if self.game_state == 0:
            self.mouse_pos = pygame.mouse.get_pos()
            self.mouse_x = self.mouse_pos[0]
            self.mouse_y = self.mouse_pos[1]
        if self.game_state == 1:
            self.all_sprites_list.update()
            # See if the player block has collided with anything.

            for bullet in self.bullet_list:
                bullet_block_hit_list = pygame.sprite.spritecollide(
                    bullet, self.bad_block_list, False)
                #pygame.sprite.spritecollide(sprite, group, dokill)
                for block in bullet_block_hit_list:
                    self.bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)
                    badblock_library.BadBlock.reset_pos(block)
                if bullet.rect.y < -10:
                    self.bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)

            good_blocks_hit_list = pygame.sprite.spritecollide(
                self.player, self.good_block_list, True)
            # Check the list of collisions.
            for block in good_blocks_hit_list:
                self.score += 1
                GOOD.play()
                self.good_block_list.remove(block)

            blocks_hit_list = pygame.sprite.spritecollide(
                self.player, self.bad_block_list, False)
            for block in blocks_hit_list:
                self.health_bar -= 1
                BAD.play()

                if self.health_bar <= 0:
                    self.flag = 1

                badblock_library.BadBlock.reset_pos(block)

            if self.score == 50:
                self.flag = 2
                

    def display_frame(self, screen):

        if self.game_state == 0:

            screen.blit(BACKGROUND_LIST[0], [0, 0])
            pygame.draw.rect(screen, BUTTONS_COLOR, [SCREEN_WIDTH/2-100,SCREEN_HEIGHT/2-50,200,50])
            pygame.draw.rect(screen, BLACK, [SCREEN_WIDTH/2-100,SCREEN_HEIGHT/2-50,200,50],4)
            pygame.draw.rect(screen, BUTTONS_COLOR, [SCREEN_WIDTH/2-100,SCREEN_HEIGHT/2+10,200,50])
            pygame.draw.rect(screen, BLACK, [SCREEN_WIDTH/2-100,SCREEN_HEIGHT/2+10,200,50],4)
            pygame.draw.rect(screen, BUTTONS_COLOR, [SCREEN_WIDTH/2-100,SCREEN_HEIGHT/2+70,200,50])
            pygame.draw.rect(screen, BLACK, [SCREEN_WIDTH/2-100,SCREEN_HEIGHT/2+70,200,50],4)
            game_titel_text = game_titel_font.render(
                "Spacegame", True, WHITE)
            game_menu_play = game_menu_font.render(
                "PLAY", True, WHITE)
            game_menu_level = game_menu_font.render(
                "LEVEL - COMING SOON", True, WHITE)
            game_menu_ships = game_menu_font.render(
                "SHIPS - COMING SOON", True, WHITE)
            x = (SCREEN_WIDTH // 2) - (game_titel_text.get_width() // 2)
            y = (SCREEN_HEIGHT // 2) - (game_titel_text.get_height() // 2)
            screen.blit(game_titel_text, [x, y-150])
            x = (SCREEN_WIDTH // 2) - (game_menu_play.get_width() // 2)
            y = (SCREEN_HEIGHT // 2) - (game_menu_play.get_height() // 2)
            screen.blit(game_menu_play, [x, y-25])
            x = (SCREEN_WIDTH // 2) - (game_menu_level.get_width() // 2)
            y = (SCREEN_HEIGHT // 2) - (game_menu_level.get_height() // 2)
            screen.blit(game_menu_level, [x, y+35])
            x = (SCREEN_WIDTH // 2) - (game_menu_ships.get_width() // 2)
            y = (SCREEN_HEIGHT // 2) - (game_menu_ships.get_height() // 2)
            screen.blit(game_menu_ships, [x, y+95])

        elif self.game_state == 1:
            screen.blit(BACKGROUND_LIST[1], [0, 0])
            
            self.all_sprites_list.draw(screen)
            font = pygame.font.Font("C:/Windows/Fonts/RAVIE.TTF", 25)
            text_score = font.render("Score: " + str(self.score), True, WHITE)
            screen.blit(text_score, [5, 5])
            if self.flag == 1:
                screen.blit(HEALTH[0], [
                        self.player.rect.x, self.player.rect.y - 4])
                self.game_state = 9
            
            else:
                if self.flag == 2:
                    self.game_state = 8
                screen.blit(HEALTH[self.health_bar], [
                        self.player.rect.x, self.player.rect.y - 4])
            
        elif self.game_state == 8:
            time.sleep(1)
            game_instruction_text = game_titel_font.render("Press ESC to get back to Menu", True, (47,79,79))
            game_instruction_text_1 = game_titel_font.render("(Coming Soon:)Press SPACE to go to the next Level", True, (47,79,79))
            game_won_text = game_titel_font.render("You Won!", True, (47,79,79))
            x = (SCREEN_WIDTH // 2) - (game_won_text.get_width() // 2)
            y = (SCREEN_HEIGHT // 2) - (game_won_text.get_height() // 2)
            screen.blit(game_won_text, [x,y])
            screen.blit(game_instruction_text, [(SCREEN_WIDTH//2)-(game_instruction_text.get_width()//2),(SCREEN_HEIGHT//2)-(game_instruction_text.get_height()//2)+60])
            screen.blit(game_instruction_text_1, [(SCREEN_WIDTH//2)-(game_instruction_text_1.get_width()//2),120+(SCREEN_HEIGHT//2)-(game_instruction_text.get_height()//2)])

        elif self.game_state == 9:
            time.sleep(1)
            screen.blit(BACKGROUND_LIST[9], [0, 0])
            game_over_text = game_titel_font.render(
                "Game Over \n leftclick to get back to the menu", True, WHITE)
            x = (SCREEN_WIDTH // 2) - (game_over_text.get_width() // 2)
            y = (SCREEN_HEIGHT // 2) - (game_over_text.get_height() // 2)
            screen.blit(game_over_text, [x, y])

        
                
        pygame.display.flip()