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
    # level1
    block_list = None
    bad_block_list = None
    good_block_list = None
    bullet_list = None
    #enemy_list = None
    all_sprites_list = None
    #enemy = 0
    # level2
    block_list_1 = None
    bad_block_list_1 = None
    good_block_list_1 = None
    #enemy_list_1 = None
    all_sprites_list_1 = None
    #enemy_1 = 0

    block_list_2 = None
    bad_block_list_2 = None
    good_block_list_2 = None
    #enemy_list_2 = None
    all_sprites_list_2 = None
    #enemy_2 = 0
    
    ammo_list_5 = None
    ammo_list_10 = None
    key_flag = 0
    flag = 0
    player = None
    player_ship = None
    bullet_image = None
    game_state = 0  # (0:Startscreen, 1:Play Level1, 8:Game Won,9:Game Over)
    health_bar = 10
    score = 0
    #tick = 0

    mouse_pos = []

    def __init__(self):
        self.health_bar = 10
        self.score = 0
        #self.game_over = False
        self.game_state = 0
        self.flag = 0
        #self.tick = 0
        self.key_flag = 0

        self.bad_block_list = pygame.sprite.Group()
        self.good_block_list = pygame.sprite.Group()
        #self.enemy_list = pygame.sprite.Group()
        self.bullet_list = pygame.sprite.Group()
        # This is a list of every sprite.
        # All blocks and the player block as well.
        self.ammo_list_5 = pygame.sprite.Group()
        self.ammo_list_10 = pygame.sprite.Group()

        self.all_sprites_list = pygame.sprite.Group()

        # bad blocks
        for i in range(20):
            # This represents a block
            block = badblock_library.BadBlock(0, 1, asteroid_one)

            # Set a random location for the block
            block.rect.x = random.randrange(SCREEN_WIDTH)
            block.rect.y = random.randrange(-200, 340)

            # Add the block to the list of objects
            self.bad_block_list.add(block)
            self.all_sprites_list.add(block)

        # good blocks
        for i in range(30):
            # This represents a block
            block = goodblock_library.GoodBLock(gem)

            # Set a random location for the block
            block.rect.x = random.randrange(SCREEN_WIDTH-20)
            block.rect.y = random.randrange(SCREEN_HEIGHT-15)

            # Add the block to the list of objects
            self.good_block_list.add(block)
            self.all_sprites_list.add(block)

        # Level 2
        self.bad_block_list_1 = pygame.sprite.Group()
        self.good_block_list_1 = pygame.sprite.Group()
        #self.enemy_list_1 = pygame.sprite.Group()

        # This is a list of every sprite.
        # All blocks and the player block as well.
        self.all_sprites_list_1 = pygame.sprite.Group()

        # bad blocks
        for i in range(25):
            # This represents a block
            block = badblock_library.BadBlock(1, 0, asteroid_one)

            # Set a random location for the block
            block.rect.x = random.randrange(-600, 200)
            block.rect.y = random.randrange(SCREEN_HEIGHT)

            # Add the block to the list of objects
            self.bad_block_list_1.add(block)
            self.all_sprites_list_1.add(block)

        # good blocks
        for i in range(45):
            # This represents a block
            block = goodblock_library.GoodBLock(gem)

            # Set a random location for the block
            block.rect.x = random.randrange(SCREEN_WIDTH-20)
            block.rect.y = random.randrange(SCREEN_HEIGHT-15)

            # Add the block to the list of objects
            self.good_block_list_1.add(block)
            self.all_sprites_list_1.add(block)

        self.bad_block_list_2 = pygame.sprite.Group()
        self.good_block_list_2 = pygame.sprite.Group()
        #self.enemy_list_1 = pygame.sprite.Group()

        # This is a list of every sprite.
        # All blocks and the player block as well.
        self.all_sprites_list_2 = pygame.sprite.Group()

        # bad blocks
        for i in range(30):
            # This represents a block
            block = badblock_library.BadBlock(-2, 2, asteroid_one)

            # Set a random location for the block
            block.rect.x = random.randrange(SCREEN_WIDTH//2, SCREEN_WIDTH)
            block.rect.y = random.randrange(-100, 350)

            # Add the block to the list of objects
            self.bad_block_list_2.add(block)
            self.all_sprites_list_2.add(block)

        # good blocks
        for i in range(60):
            # This represents a block
            block = goodblock_library.GoodBLock(gem)

            # Set a random location for the block
            block.rect.x = random.randrange(SCREEN_WIDTH-20)
            block.rect.y = random.randrange(SCREEN_HEIGHT-15)

            # Add the block to the list of objects
            self.good_block_list_2.add(block)
            self.all_sprites_list_2.add(block)

        # Create a  player block
        self.player_ship = PLAYER_SHIP_LIST[0]
        self.player = player_library.Player(self.player_ship, 40)
        self.all_sprites_list.add(self.player)
        self.all_sprites_list_1.add(self.player)
        self.all_sprites_list_2.add(self.player)

        self.bullet_image = BULLET_LIST[0]

    def process_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if self.game_state == 9 and event.type == pygame.MOUSEBUTTONDOWN:
                self.__init__()
                self.health_bar = 10
                

            elif self.game_state == 0 and event.type == pygame.MOUSEBUTTONDOWN and self.mouse_x < SCREEN_WIDTH/2+100 and self.mouse_x > SCREEN_WIDTH/2-100 and self.mouse_y > SCREEN_HEIGHT/2-50 and self.mouse_y < SCREEN_HEIGHT/2:
                self.game_state = 1

            elif self.game_state == 0 and event.type == pygame.MOUSEBUTTONDOWN and self.mouse_x < SCREEN_WIDTH/2+100 and self.mouse_x > SCREEN_WIDTH/2-100 and self.mouse_y > SCREEN_HEIGHT/2+10 and self.mouse_y < SCREEN_HEIGHT/2+200:
                self.game_state = 0.1
            elif self.game_state == 0.1:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.game_state = 0
                elif event.type == pygame.MOUSEBUTTONDOWN and self.mouse_x < 328 and self.mouse_x > 232 and self.mouse_y > SCREEN_HEIGHT/2-128 and self.mouse_y < SCREEN_HEIGHT/2-32:
                    self.player_ship = PLAYER_SHIP_LIST[0]
                    self.bullet_image = BULLET_LIST[0]
                    SELECT.play()
                elif event.type == pygame.MOUSEBUTTONDOWN and self.mouse_x < 456 and self.mouse_x > 360 and self.mouse_y > SCREEN_HEIGHT/2-128 and self.mouse_y < SCREEN_HEIGHT/2-32:
                    self.player_ship = PLAYER_SHIP_LIST[1]
                    self.bullet_image = BULLET_LIST[1]
                    SELECT.play()
                elif event.type == pygame.MOUSEBUTTONDOWN and self.mouse_x < 584 and self.mouse_x > 488 and self.mouse_y > SCREEN_HEIGHT/2-128 and self.mouse_y < SCREEN_HEIGHT/2-32:
                    self.player_ship = PLAYER_SHIP_LIST[2]
                    self.bullet_image = BULLET_LIST[2]
                    SELECT.play()
                elif event.type == pygame.MOUSEBUTTONDOWN and self.mouse_x < 712 and self.mouse_x > 616 and self.mouse_y > SCREEN_HEIGHT/2-128 and self.mouse_y < SCREEN_HEIGHT/2-32:
                    self.player_ship = PLAYER_SHIP_LIST[3]
                    self.bullet_image = BULLET_LIST[3]
                    SELECT.play()
                elif event.type == pygame.MOUSEBUTTONDOWN and self.mouse_x < 840 and self.mouse_x > 744 and self.mouse_y > SCREEN_HEIGHT/2-128 and self.mouse_y < SCREEN_HEIGHT/2-32:
                    bullet_image = BULLET_LIST[4]
                    SELECT.play()
                elif event.type == pygame.MOUSEBUTTONDOWN and self.mouse_x < 968 and self.mouse_x > 872 and self.mouse_y > SCREEN_HEIGHT/2-128 and self.mouse_y < SCREEN_HEIGHT/2-32:
                    self.player_ship = PLAYER_SHIP_LIST[5]
                    self.bullet_image = BULLET_LIST[5]
                    SELECT.play()
                self.player.image = self.player_ship
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.game_state == 8:
                self.game_state = 2  # level2
                self.health_bar = 10
                self.flag = 0
                self.player.ammo = 30
                self.player.rect.x = SCREEN_WIDTH // 2
                self.player.rect.y = SCREEN_HEIGHT // 2
                self.player.image = pygame.transform.rotate(self.player_ship, 90)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.game_state == 7:
                self.game_state = 3  # level3
                self.health_bar = 10
                self.flag = 0
                self.player.ammo = 20
                self.player.rect.x = SCREEN_WIDTH // 2
                self.player.rect.y = SCREEN_HEIGHT // 2
                self.player.image = self.player_ship

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and self.game_state == 8:
                self.game_state = 0  # main menu

            elif event.type == pygame.MOUSEBUTTONDOWN and (self.game_state == 1 or self.game_state == 2 or self.game_state == 3):
                if self.player.ammo != 0:
                    self.mouse_pos = pygame.mouse.get_pos()
                    self.mouse_x = self.mouse_pos[0]
                    self.mouse_y = self.mouse_pos[1]
                    bullet = bullet_library.Bullet(
                        self.bullet_image, self.player.rect.x, self.player.rect.y, self.mouse_x, self.mouse_y)
                    LASER[0].play()
                    self.player.ammo -= 1
                    if self.game_state == 1:
                        self.all_sprites_list.add(bullet)
                    elif self.game_state == 2:
                        self.all_sprites_list_1.add(bullet) 
                    elif self.game_state == 3:
                        self.all_sprites_list_2.add(bullet)         
                    self.bullet_list.add(bullet)
                else: EMPTY.play()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.player.changespeed(0, -3)
                    self.player.image = self.player_ship

                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.player.changespeed(3, 0)
                    self.player.image = pygame.transform.rotate(self.player_ship, 270)
                    

                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:

                    self.player.changespeed(0, 3)
                    self.player.image = pygame.transform.rotate(self.player_ship, 180)

                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.player.changespeed(-3, 0)
                    self.player.image = pygame.transform.rotate(self.player_ship, 90)
                    

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
        if self.game_state == 0 or self.game_state == 0.1:
            self.mouse_pos = pygame.mouse.get_pos()
            self.mouse_x = self.mouse_pos[0]
            self.mouse_y = self.mouse_pos[1]
        

        if self.game_state == 1:
            self.all_sprites_list.update()

            for bullet in self.bullet_list:
                bullet_block_hit_list = pygame.sprite.spritecollide(
                    bullet, self.bad_block_list, False)
                #pygame.sprite.spritecollide(sprite, group, dokill)
                for block in bullet_block_hit_list:
                    if random.randrange(15) == 1:
                        good_block = goodblock_library.GoodBLock(gem)
                        # Set a  location for the block
                        good_block.rect.x = bullet.rect.x
                        good_block.rect.y = bullet.rect.y
                        # Add the block to the list of objects
                        self.good_block_list.add(good_block)
                        self.all_sprites_list.add(good_block)
                    if random.randrange(10) == 1:
                        if random.randrange(4)==1:
                            
                            good_block = goodblock_library.GoodBLock(ammo_10)
                            good_block.rect.x = bullet.rect.x
                            good_block.rect.y = bullet.rect.y
                            self.ammo_list_10.add(good_block)
                            self.all_sprites_list.add(good_block)
                        else: 
                            good_block = goodblock_library.GoodBLock(ammo_5)
                            good_block.rect.x = bullet.rect.x
                            good_block.rect.y = bullet.rect.y
                            self.ammo_list_5.add(good_block)
                            self.all_sprites_list.add(good_block)
                    self.bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)
                    badblock_library.BadBlock.reset_pos(block)

                if bullet.rect.y < -10:
                    self.bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)           

            good_blocks_hit_list = pygame.sprite.spritecollide(
                self.player, self.ammo_list_10, True)
            # Check the list of collisions.
            for block in good_blocks_hit_list:
                self.player.ammo += 10
                GOOD.play()
                self.ammo_list_10.remove(block)
                self.all_sprites_list.remove(block)
            
            good_blocks_hit_list = pygame.sprite.spritecollide(
                self.player, self.ammo_list_5, True)
            # Check the list of collisions.
            for block in good_blocks_hit_list:
                self.player.ammo += 5
                GOOD.play()
                self.ammo_list_5.remove(block)
                self.all_sprites_list.remove(block)

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

            if len(self.good_block_list) == 0:
                self.flag = 2
        if self.game_state == 2:
            self.all_sprites_list_1.update()
            # See if the player block has collided with anything.

            for bullet in self.bullet_list:
                bullet_block_hit_list = pygame.sprite.spritecollide(
                    bullet, self.bad_block_list_1, False)
                #pygame.sprite.spritecollide(sprite, group, dokill)
                for block in bullet_block_hit_list:
                    if random.randrange(10) == 1:
                        good_block = goodblock_library.GoodBLock(gem)
                        # Set a  location for the block
                        good_block.rect.x = bullet.rect.x
                        good_block.rect.y = bullet.rect.y
                        # Add the block to the list of objects
                        self.good_block_list_1.add(good_block)
                        self.all_sprites_list_1.add(good_block)
                    if random.randrange(15) == 1:
                        if random.randrange(8)==1:
                            good_block = goodblock_library.GoodBLock(ammo_10)
                            good_block.rect.x = bullet.rect.x
                            good_block.rect.y = bullet.rect.y
                            self.ammo_list_10.add(good_block)
                            self.all_sprites_list_1.add(good_block)
                        else: 
                            good_block = goodblock_library.GoodBLock(ammo_5)
                            good_block.rect.x = bullet.rect.x
                            good_block.rect.y = bullet.rect.y
                            self.ammo_list_5.add(good_block)
                            self.all_sprites_list_1.add(good_block)
                    self.bullet_list.remove(bullet)
                    self.all_sprites_list_1.remove(bullet)
                    badblock_library.BadBlock.reset_pos(block)

                if bullet.rect.y < -10:
                    self.bullet_list.remove(bullet)
                    self.all_sprites_list_1.remove(bullet)
            
            good_blocks_hit_list = pygame.sprite.spritecollide(
                self.player, self.ammo_list_10, True)
            # Check the list of collisions.
            for block in good_blocks_hit_list:
                self.player.ammo += 10
                GOOD.play()
                self.ammo_list_10.remove(block)
                self.all_sprites_list_1.remove(block)
            
            good_blocks_hit_list = pygame.sprite.spritecollide(
                self.player, self.ammo_list_5, True)
            # Check the list of collisions.
            for block in good_blocks_hit_list:
                self.player.ammo += 5
                GOOD.play()
                self.ammo_list_5.remove(block)
                self.all_sprites_list_1.remove(block)

            good_blocks_hit_list = pygame.sprite.spritecollide(
                self.player, self.good_block_list_1, True)
            # Check the list of collisions.
            for block in good_blocks_hit_list:
                self.score += 1
                GOOD.play()
                self.good_block_list_1.remove(block)

            blocks_hit_list1 = pygame.sprite.spritecollide(
                self.player, self.bad_block_list_1, False)
            for block1 in blocks_hit_list1:
                badblock_library.BadBlock.reset_pos(block1)
                self.health_bar -= 1
                BAD.play()

                if self.health_bar <= 0:
                    self.flag = 1

            

            if len(self.good_block_list_1) == 0:
                self.flag = 2
        
        if self.game_state == 3:
            self.all_sprites_list_2.update()
            # See if the player block has collided with anything.

            for bullet in self.bullet_list:
                bullet_block_hit_list = pygame.sprite.spritecollide(
                    bullet, self.bad_block_list_2, False)
                #pygame.sprite.spritecollide(sprite, group, dokill)
                for block in bullet_block_hit_list:
                    if random.randrange(5) == 1:
                        good_block = goodblock_library.GoodBLock(gem)
                        # Set a  location for the block
                        good_block.rect.x = bullet.rect.x
                        good_block.rect.y = bullet.rect.y
                        # Add the block to the list of objects
                        self.good_block_list_2.add(good_block)
                        self.all_sprites_list_2.add(good_block)
                    if random.randrange(30) == 1:
                        if random.randrange(16)==1:
                            good_block = goodblock_library.GoodBLock(ammo_10)
                            good_block.rect.x = bullet.rect.x
                            good_block.rect.y = bullet.rect.y
                            self.ammo_list_10.add(good_block)
                            self.all_sprites_list_2.add(good_block)
                        else: 
                            good_block = goodblock_library.GoodBLock(ammo_5)
                            good_block.rect.x = bullet.rect.x
                            good_block.rect.y = bullet.rect.y
                            self.ammo_list_5.add(good_block)
                            self.all_sprites_list_2.add(good_block)
                    self.bullet_list.remove(bullet)
                    self.all_sprites_list_2.remove(bullet)
                    badblock_library.BadBlock.reset_pos(block)

                

                if bullet.rect.y < -10:
                    self.bullet_list.remove(bullet)
                    self.all_sprites_list_2.remove(bullet)

            # Check the list of collisions.
            good_blocks_hit_list = pygame.sprite.spritecollide(
                self.player, self.ammo_list_10, True)
            for block in good_blocks_hit_list:
                self.player.ammo += 10
                GOOD.play()
                self.ammo_list_10.remove(block)
                self.all_sprites_list_2.remove(block)
            
            good_blocks_hit_list = pygame.sprite.spritecollide(
                self.player, self.ammo_list_5, True)
            # Check the list of collisions.
            for block in good_blocks_hit_list:
                self.player.ammo += 5
                GOOD.play()
                self.ammo_list_5.remove(block)
                self.all_sprites_list_2.remove(block)

            good_blocks_hit_list = pygame.sprite.spritecollide(
                self.player, self.good_block_list_2, True)
            # Check the list of collisions.
            for block in good_blocks_hit_list:
                self.score += 1
                GOOD.play()
                self.good_block_list_2.remove(block)

            blocks_hit_list2 = pygame.sprite.spritecollide(
                self.player, self.bad_block_list_2, False)
            for block1 in blocks_hit_list2:
                badblock_library.BadBlock.reset_pos(block1)
                self.health_bar -= 1
                BAD.play()

                if self.health_bar <= 0:
                    self.flag = 1

            if len(self.good_block_list_2) == 0:
                self.flag = 2

    def display_frame(self, screen):

        if self.game_state == 0:#main menu

            screen.blit(BACKGROUND_LIST[0], [0, 0])
            pygame.draw.rect(screen, BUTTONS_COLOR, [
                             SCREEN_WIDTH/2-100, SCREEN_HEIGHT/2-50, 200, 50])
            pygame.draw.rect(
                screen, BLACK, [SCREEN_WIDTH/2-100, SCREEN_HEIGHT/2-50, 200, 50], 4)
            pygame.draw.rect(screen, BUTTONS_COLOR, [
                             SCREEN_WIDTH/2-100, SCREEN_HEIGHT/2+10, 200, 50])
            pygame.draw.rect(
                screen, BLACK, [SCREEN_WIDTH/2-100, SCREEN_HEIGHT/2+10, 200, 50], 4)
            
            game_titel_text = game_titel_font.render(
                "Spacegame", True, WHITE)
            game_menu_play = game_menu_font.render(
                "PLAY", True, WHITE)
            game_menu_ships = game_menu_font.render(
                "SHIPS", True, WHITE)
            x = (SCREEN_WIDTH // 2) - (game_titel_text.get_width() // 2)
            y = (SCREEN_HEIGHT // 2) - (game_titel_text.get_height() // 2)
            screen.blit(game_titel_text, [x, y-150])
            x = (SCREEN_WIDTH // 2) - (game_menu_play.get_width() // 2)
            y = (SCREEN_HEIGHT // 2) - (game_menu_play.get_height() // 2)
            screen.blit(game_menu_play, [x, y-25])
            x = (SCREEN_WIDTH // 2) - (game_menu_ships.get_width() // 2)
            y = (SCREEN_HEIGHT // 2) - (game_menu_ships.get_height() // 2)
            screen.blit(game_menu_ships, [x, y+35])

        elif self.game_state == 0.1:#menu ship select
            screen.blit(BACKGROUND_LIST[0], [0, 0])
            pygame.draw.rect(screen,(47, 79, 79), [160, SCREEN_HEIGHT//2- 160, 896, 256]) # 96, 64
            #pygame.draw.rect(screen,BLACK, [256+128*i, SCREEN_HEIGHT//2- 128, ship.get_width(), ship.get_height()], 4)
            
            for i in range(6):
                ship = PLAYER_SHIP_LIST[i]
                pygame.draw.rect(screen, BLACK, [232+128*i,SCREEN_HEIGHT//2-128, 96, 96], 4)
                screen.blit(ship, [256+128*i, SCREEN_HEIGHT//2- 128])
            ships_instructions = game_titel_font.render(
                "Press ESC to get back to the main menu", True, WHITE)
            x = (SCREEN_WIDTH // 2) - (ships_instructions.get_width() // 2)
            y = (SCREEN_HEIGHT // 2) - (ships_instructions.get_height() // 2)
            screen.blit(ships_instructions, [x, y+300])

        elif self.game_state == 1:#level1
            screen.blit(BACKGROUND_LIST[1], [0, 0])

            self.all_sprites_list.draw(screen)
            text_score = font.render("Score: " + str(self.score), True, WHITE)
            screen.blit(text_score, [5, 5])
            text_ammo = font.render("AMMO: "+ str(self.player.ammo), True , WHITE)
            screen.blit(text_ammo, [SCREEN_WIDTH-text_ammo.get_width()-40, SCREEN_HEIGHT - 40])

            if self.flag == 1:
                screen.blit(HEALTH[0], [
                    self.player.rect.x, self.player.rect.y - 4])
                self.game_state = 9

            else:
                if self.flag == 2:
                    self.game_state = 8
                screen.blit(HEALTH[self.health_bar], [
                    self.player.rect.x, self.player.rect.y - 4])

        elif self.game_state == 2:#level2
            screen.blit(BACKGROUND_LIST[2], [0, 0])

            self.all_sprites_list_1.draw(screen)
            
            text_score = font.render("Score: " + str(self.score), True, WHITE)
            screen.blit(text_score, [5, 5])
            text_ammo = font.render("AMMO: "+ str(self.player.ammo), True , WHITE)
            screen.blit(text_ammo, [SCREEN_WIDTH-text_ammo.get_width()-40, SCREEN_HEIGHT - 40])
            if self.flag == 1:
                screen.blit(HEALTH[0], [
                    self.player.rect.x, self.player.rect.y - 4])
                self.game_state = 9

            else:
                if self.flag == 2:
                    self.game_state = 7
                screen.blit(HEALTH[self.health_bar], [
                    self.player.rect.x, self.player.rect.y - 4])

        elif self.game_state == 3:#level3
            screen.blit(BACKGROUND_LIST[3], [0, 0])

            self.all_sprites_list_2.draw(screen)
            
            text_score = font.render("Score: " + str(self.score), True, WHITE)
            screen.blit(text_score, [5, 5])
            text_ammo = font.render("AMMO: "+ str(self.player.ammo), True , WHITE)
            screen.blit(text_ammo, [SCREEN_WIDTH-text_ammo.get_width()-40, SCREEN_HEIGHT - 40])
            if self.flag == 1:
                screen.blit(HEALTH[0], [
                    self.player.rect.x, self.player.rect.y - 4])
                self.game_state = 9

            else:
                if self.flag == 2:
                    self.game_state = 10
                screen.blit(HEALTH[self.health_bar], [
                    self.player.rect.x, self.player.rect.y - 4])

        elif self.game_state == 8 or self.game_state == 7:
            time.sleep(1)
            game_instruction_text = game_titel_font.render(
                "Press ESC to get back to Menu", True, (47, 79, 79))
            game_instruction_text_1 = game_titel_font.render(
                "(Coming Soon:)Press SPACE to go to the next Level", True, (47, 79, 79))
            game_won_text = game_titel_font.render(
                "You Won!", True, (47, 79, 79))
            x = (SCREEN_WIDTH // 2) - (game_won_text.get_width() // 2)
            y = (SCREEN_HEIGHT // 2) - (game_won_text.get_height() // 2)
            screen.blit(game_won_text, [x, y])
            screen.blit(game_instruction_text, [(SCREEN_WIDTH//2)-(game_instruction_text.get_width(
            )//2), (SCREEN_HEIGHT//2)-(game_instruction_text.get_height()//2)+60])
            screen.blit(game_instruction_text_1, [(SCREEN_WIDTH//2)-(game_instruction_text_1.get_width(
            )//2), 120+(SCREEN_HEIGHT//2)-(game_instruction_text.get_height()//2)])

        elif self.game_state == 9:
            time.sleep(1)
            screen.blit(BACKGROUND_LIST[9], [0, 0])
            game_over_text = game_titel_font.render(
                "Game Over \n leftclick to get back to the menu", True, WHITE)
            x = (SCREEN_WIDTH // 2) - (game_over_text.get_width() // 2)
            y = (SCREEN_HEIGHT // 2) - (game_over_text.get_height() // 2)
            screen.blit(game_over_text, [x, y])

        elif self.game_state == 10:
            time.sleep(1)
            screen.blit(BACKGROUND_LIST[9], [0, 0])
            game_won_text = game_titel_font.render(
                "You won! leftclick to get back to the menu", True, WHITE)
            x = (SCREEN_WIDTH // 2) - (game_won_text.get_width() // 2)
            y = (SCREEN_HEIGHT // 2) - (game_won_text.get_height() // 2)
            screen.blit(game_won_text, [x, y])
        pygame.display.flip()
