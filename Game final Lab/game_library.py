import pygame
import random
import badblock_library
import goodblock_library
import bullet_library
from game_const_library import *
import player_library
import os
import time
import json

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
    previous_score = 0
    high_score = 0
    high_score_name = None
    new_high_score = False
    menu_ship = None

    #tick = 0

    mouse_pos = []
    mouse_x = 0
    mouse_y = 0

    def __init__(self):

        try:
            with open('game_score.json', 'r') as high_score_file:
                self.high_score = json.load(high_score_file)
        except:
            print("No json file yet")

        self.score = 0
        self.health_bar = 10
        #self.game_over = False
        self.game_state = 0
        self.flag = 0
        #self.tick = 0
        self.key_flag = 0
        self.high_score_name = ""
        self.new_high_score = False
        self.bad_block_list = pygame.sprite.Group()
        self.good_block_list = pygame.sprite.Group()
        #self.enemy_list = pygame.sprite.Group()
        self.bullet_list = pygame.sprite.Group()
        # This is a list of every sprite.
        # All blocks and the player block as well.
        self.ammo_list_5 = pygame.sprite.Group()
        self.ammo_list_10 = pygame.sprite.Group()

        self.all_sprites_list = pygame.sprite.Group()
        self.mouse_pos = []
        self.mouse_x = 0
        self.mouse_y = 0

        self.menu_ship = MENU_SHIPS[0]

        # bad blocks
        for i in range(20):
            # This represents a block
            block = badblock_library.BadBlock(
                0, 1, ASTEROID_LIST[random.randrange(0, 4, 1)])

            # Set a random location for the block
            block.rect.x = random.randrange(SCREEN_WIDTH)
            block.rect.y = random.randrange(-200, 340)

            # Add the block to the list of objects
            self.bad_block_list.add(block)
            self.all_sprites_list.add(block)

        # good blocks
        for i in range(45):
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
            block = badblock_library.BadBlock(
                2, 0, ASTEROID_LIST[random.randrange(4, 8, 1)])

            # Set a random location for the block
            block.rect.x = random.randrange(-1000, 200)
            block.rect.y = random.randrange(SCREEN_HEIGHT)

            # Add the block to the list of objects
            self.bad_block_list_1.add(block)
            self.all_sprites_list_1.add(block)

        # good blocks
        for i in range(35):
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
            block = badblock_library.BadBlock(-2, 2,
                                              ASTEROID_LIST[random.randrange(8, 12, 1)])

            # Set a random location for the block
            block.rect.x = random.randrange(SCREEN_WIDTH+SCREEN_WIDTH)
            block.rect.y = random.randrange(-350, 350)

            # Add the block to the list of objects
            self.bad_block_list_2.add(block)
            self.all_sprites_list_2.add(block)

        # good blocks
        for i in range(30):
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
                self.previous_score = self.score
                if self.score > self.high_score["Score"]:
                    self.high_score["Score"] = self.score
                    self.high_score["Name"] = self.high_score_name
                with open('game_score.json', 'w') as score_file:
                    json.dump(self.high_score, score_file)
                self.__init__()
                self.health_bar = 10
            elif self.game_state == 10 and event.type == pygame.MOUSEBUTTONDOWN:
                self.previous_score = self.score
                if self.score > self.high_score["Score"]:
                    self.high_score["Score"] = self.score
                    self.high_score["Name"] = self.high_score_name
                with open('game_score.json', 'w') as score_file:
                    json.dump(self.high_score, score_file)
                self.__init__()
                self.health_bar = 10
            elif self.game_state == 0 and event.type == pygame.MOUSEBUTTONDOWN and self.mouse_x < (SCREEN_WIDTH//2)+100 and self.mouse_x > (SCREEN_WIDTH//2)-100 and self.mouse_y > (SCREEN_HEIGHT//2)-50 and self.mouse_y < (SCREEN_HEIGHT//2):
                self.game_state = 1

            elif self.game_state == 0 and event.type == pygame.MOUSEBUTTONDOWN and self.mouse_x < (SCREEN_WIDTH//2)+100 and self.mouse_x > (SCREEN_WIDTH//2)-100 and self.mouse_y > (SCREEN_HEIGHT//2)+10 and self.mouse_y < (SCREEN_HEIGHT//2)+60:
                self.game_state = 0.1

            elif self.game_state == 0.1 or self.game_state == 0.2:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.game_state = 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.mouse_x < SCREEN_WIDTH//2 + 100 and self.mouse_x > SCREEN_WIDTH//2+60 and self.mouse_y < SCREEN_HEIGHT//2 + 220 and self.mouse_y > SCREEN_HEIGHT//2+180:
                        self.menu_ship = MENU_SHIPS[5]
                        self.player_ship = PLAYER_SHIP_LIST[5]
                        self.bullet_image = BULLET_LIST[5]
                        SELECT.play()
                    elif self.mouse_x < SCREEN_WIDTH//2 + 60 and self.mouse_x > SCREEN_WIDTH//2+20 and self.mouse_y < SCREEN_HEIGHT//2 + 220 and self.mouse_y > SCREEN_HEIGHT//2+180:
                        self.menu_ship = MENU_SHIPS[4]
                        self.player_ship = PLAYER_SHIP_LIST[4]
                        self.bullet_image = BULLET_LIST[4]
                        SELECT.play()
                    elif self.mouse_x < SCREEN_WIDTH//2 + 20 and self.mouse_x > SCREEN_WIDTH//2-20 and self.mouse_y < SCREEN_HEIGHT//2 + 220 and self.mouse_y > SCREEN_HEIGHT//2+180:
                        self.menu_ship = MENU_SHIPS[3]
                        self.player_ship = PLAYER_SHIP_LIST[3]
                        self.bullet_image = BULLET_LIST[3]
                        SELECT.play()
                    elif self.mouse_x < SCREEN_WIDTH//2 + -20 and self.mouse_x > SCREEN_WIDTH//2-60 and self.mouse_y < SCREEN_HEIGHT//2 + 220 and self.mouse_y > SCREEN_HEIGHT//2+180:
                        self.menu_ship = MENU_SHIPS[2]
                        self.player_ship = PLAYER_SHIP_LIST[2]
                        self.bullet_image = BULLET_LIST[2]
                        SELECT.play()
                    elif self.mouse_x < SCREEN_WIDTH//2 + -60 and self.mouse_x > SCREEN_WIDTH//2-100 and self.mouse_y < SCREEN_HEIGHT//2 + 220 and self.mouse_y > SCREEN_HEIGHT//2+180:
                        self.menu_ship = MENU_SHIPS[1]
                        self.player_ship = PLAYER_SHIP_LIST[1]
                        self.bullet_image = BULLET_LIST[1]
                        SELECT.play()
                    elif self.mouse_x < SCREEN_WIDTH//2 + -100 and self.mouse_x > SCREEN_WIDTH//2-140 and self.mouse_y < SCREEN_HEIGHT//2 + 220 and self.mouse_y > SCREEN_HEIGHT//2+180:
                        self.menu_ship = MENU_SHIPS[0]
                        self.player_ship = PLAYER_SHIP_LIST[0]
                        self.bullet_image = BULLET_LIST[0]
                        SELECT.play()
                    #[SCREEN_WIDTH//2 - 140, SCREEN_HEIGHT//2+180, 240, 40]
                    self.player.image = self.player_ship
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.game_state == 8:

                self.game_state = 2  # level2
                self.health_bar = 10
                self.flag = 0
                self.player.ammo = 30
                self.player.rect.x = SCREEN_WIDTH // 2
                self.player.rect.y = SCREEN_HEIGHT // 2
                self.player.image = pygame.transform.rotate(
                    self.player_ship, 90)
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

            elif (self.new_high_score and event.type == pygame.KEYDOWN) and (self.game_state == 9 or self.game_state == 10):
                if event.key == pygame.K_BACKSPACE:
                    self.high_score_name = self.high_score_name[0:-1]

                elif len(self.high_score_name) < 15:
                    self.high_score_name += event.unicode

            # SCREEN_WIDTH/2-100, SCREEN_HEIGHT/2+70, 200, 50
            elif self.game_state == 0 and event.type == pygame.MOUSEBUTTONDOWN and self.mouse_x < (SCREEN_WIDTH//2) + 100 and self.mouse_x > (SCREEN_WIDTH//2)-100 and self.mouse_y < (SCREEN_HEIGHT//2)+120 and self.mouse_y > (SCREEN_HEIGHT//2)+70:
                self.game_state = 0.2

            elif event.type == pygame.MOUSEBUTTONDOWN and (self.game_state == 1 or self.game_state == 2 or self.game_state == 3):
                if self.player.ammo != 0:
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
                else:
                    EMPTY.play()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.player.changespeed(0, -3)
                    self.player.image = self.player_ship

                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.player.changespeed(3, 0)
                    self.player.image = pygame.transform.rotate(
                        self.player_ship, 270)

                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:

                    self.player.changespeed(0, 3)
                    self.player.image = pygame.transform.rotate(
                        self.player_ship, 180)

                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.player.changespeed(-3, 0)
                    self.player.image = pygame.transform.rotate(
                        self.player_ship, 90)

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
                        if random.randrange(4) == 1:

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
                        if random.randrange(8) == 1:
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
                        if random.randrange(16) == 1:
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

        if self.game_state == 0:  # main menu

            screen.blit(BACKGROUND_LIST[0], [0, 0])
            pygame.draw.rect(screen, BUTTONS_COLOR, [
                             SCREEN_WIDTH/2-100, SCREEN_HEIGHT/2-50, 200, 50])
            pygame.draw.rect(
                screen, BLACK, [SCREEN_WIDTH/2-100, SCREEN_HEIGHT/2-50, 200, 50], 4)
            pygame.draw.rect(screen, BUTTONS_COLOR, [
                             SCREEN_WIDTH/2-100, SCREEN_HEIGHT/2+10, 200, 50])
            pygame.draw.rect(
                screen, BLACK, [SCREEN_WIDTH/2-100, SCREEN_HEIGHT/2+10, 200, 50], 4)

            pygame.draw.rect(screen, BUTTONS_COLOR, [
                             SCREEN_WIDTH/2-100, SCREEN_HEIGHT/2+70, 200, 50])
            pygame.draw.rect(
                screen, BLACK, [SCREEN_WIDTH/2-100, SCREEN_HEIGHT/2+70, 200, 50], 4)

            game_titel_text = game_titel_font.render(
                "Spacegame", True, WHITE)
            game_menu_play = game_menu_font.render(
                "PLAY", True, WHITE)
            game_menu_ships = game_menu_font.render(
                "SHIPS", True, WHITE)
            game_score_list_text = game_menu_font.render(
                "Highscore List", True, WHITE)
            x = (SCREEN_WIDTH // 2) - (game_titel_text.get_width() // 2)
            y = (SCREEN_HEIGHT // 2) - (game_titel_text.get_height() // 2)
            screen.blit(game_titel_text, [x, y-150])
            x = (SCREEN_WIDTH // 2) - (game_menu_play.get_width() // 2)
            y = (SCREEN_HEIGHT // 2) - (game_menu_play.get_height() // 2)
            screen.blit(game_menu_play, [x, y-25])
            x = (SCREEN_WIDTH // 2) - (game_menu_ships.get_width() // 2)
            y = (SCREEN_HEIGHT // 2) - (game_menu_ships.get_height() // 2)
            screen.blit(game_menu_ships, [x, y+35])
            x = (SCREEN_WIDTH // 2) - (game_score_list_text.get_width() // 2)
            y = (SCREEN_HEIGHT // 2) - (game_score_list_text.get_height() // 2)
            screen.blit(game_score_list_text, [x, y+95])

            pygame.draw.rect(screen, ALICE_BLUE, [
                             SCREEN_WIDTH//2+200, SCREEN_HEIGHT//2-200, 300, 400])
            pygame.draw.rect(
                screen, BLACK, [SCREEN_WIDTH//2+200, SCREEN_HEIGHT//2-200, 300, 400], 3)

            high_score_text = game_menu_font.render(
                "The current Highscore is: ", True, BLACK)
            stats = game_menu_font.render(
                "Game Stats: ", True, BLACK)
            high_Score_text_2 = game_menu_font.render(self.high_score["Name"] + ": "+str(self.high_score["Score"]), True, BLACK)
            screen.blit(stats, [SCREEN_WIDTH//2+200, SCREEN_HEIGHT//2-150])
            screen.blit(high_score_text, [SCREEN_WIDTH//2+200, SCREEN_HEIGHT//2-100])
            screen.blit(high_Score_text_2, [SCREEN_WIDTH//2+200, SCREEN_HEIGHT//2-100+high_Score_text_2.get_height()])


        elif self.game_state == 0.1:  # menu ship select
            screen.blit(BACKGROUND_LIST[0], [0, 0])
            menu = pygame.draw.rect(screen, ALICE_BLUE, [
                                    SCREEN_WIDTH//2-160, SCREEN_HEIGHT//2-240, 320, 480])
            pygame.draw.rect(screen, BLACK, [
                             SCREEN_WIDTH//2-160, SCREEN_HEIGHT//2-240, 320, 480], 4)  # 96, 64
            #pygame.draw.rect(screen,BLACK, [256+128*i, SCREEN_HEIGHT//2- 128, ship.get_width(), ship.get_height()], 4)

            for i in range(6):
                x = SCREEN_WIDTH//2 - 150
                y = SCREEN_HEIGHT//2 - 230
                pygame.draw.rect(screen, MARINE_BLUE, [
                                 SCREEN_WIDTH//2 - 140, SCREEN_HEIGHT//2+180, 240, 40])
                for i in range(6):
                    pygame.draw.rect(
                        screen, WHITE, [SCREEN_WIDTH//2 - 140 + 40*i, SCREEN_HEIGHT//2+180, 40, 40], 3)
                    number = game_titel_font.render(str(i), True, WHITE)
                    screen.blit(number, [10+SCREEN_WIDTH //
                                         2 - 140 + 40*i, SCREEN_HEIGHT//2+180])
                screen.blit(self.menu_ship, [
                            SCREEN_WIDTH//2 - self.menu_ship.get_width()//2, y])

            ships_instructions = game_titel_font.render(
                "Press ESC to get back to the main menu", True, (87, 119, 119))
            x = (SCREEN_WIDTH // 2) - (ships_instructions.get_width() // 2)
            y = (SCREEN_HEIGHT // 2) - (ships_instructions.get_height() // 2)
            pygame.draw.ellipse(screen, MARINE_BLUE, [x-30, y+300-ships_instructions.get_height(
            )//2, ships_instructions.get_width()+60, 2*ships_instructions.get_height()])
            screen.blit(ships_instructions, [x, y+300])
        elif self.game_state == 0.2:  # highscorelist
            screen.blit(BACKGROUND_LIST[8], [0, 0])
            

            high_score_text = game_titel_font.render(
                "Press ESC to get back to the main menu", True, (87, 119, 119))
            x = (SCREEN_WIDTH // 2) - (high_score_text.get_width() // 2)
            y = (SCREEN_HEIGHT // 2) - (high_score_text.get_height() // 2)
            pygame.draw.ellipse(screen, MARINE_BLUE, [x-30, y+300-high_score_text.get_height(
            )//2, high_score_text.get_width()+60, 2*high_score_text.get_height()])
            screen.blit(high_score_text, [x, y+300])
            #pygame.draw.rect(screen, BLACK)
        elif self.game_state == 1:  # level1
            screen.blit(BACKGROUND_LIST[1], [0, 0])

            self.all_sprites_list.draw(screen)
            text_score = font.render("Score: " + str(self.score), True, WHITE)
            screen.blit(text_score, [5, 5])
            text_ammo = font.render(
                "AMMO: " + str(self.player.ammo), True, WHITE)
            screen.blit(
                text_ammo, [SCREEN_WIDTH-text_ammo.get_width()-40, SCREEN_HEIGHT - 40])

            if self.flag == 1:
                if self.high_score["Score"] < self.score:
                    self.new_high_score = True
                screen.blit(HEALTH[0], [
                    self.player.rect.x, self.player.rect.y - 4])
                self.game_state = 9

            else:
                if self.flag == 2:
                    if self.high_score["Score"] < self.score:
                        self.new_high_score = True
                    self.game_state = 8
                screen.blit(HEALTH[self.health_bar], [
                    self.player.rect.x, self.player.rect.y - 4])

        elif self.game_state == 2:  # level2
            screen.blit(BACKGROUND_LIST[2], [0, 0])

            self.all_sprites_list_1.draw(screen)

            text_score = font.render("Score: " + str(self.score), True, WHITE)
            screen.blit(text_score, [5, 5])
            text_ammo = font.render(
                "AMMO: " + str(self.player.ammo), True, WHITE)
            screen.blit(
                text_ammo, [SCREEN_WIDTH-text_ammo.get_width()-40, SCREEN_HEIGHT - 40])
            if self.flag == 1:
                if self.high_score["Score"] < self.score:
                    self.new_high_score = True
                screen.blit(HEALTH[0], [
                    self.player.rect.x, self.player.rect.y - 4])
                self.game_state = 9

            else:
                if self.flag == 2:
                    if self.high_score["Score"] < self.score:
                        self.new_high_score = True
                    self.game_state = 7
                screen.blit(HEALTH[self.health_bar], [
                    self.player.rect.x, self.player.rect.y - 4])

        elif self.game_state == 3:  # level3
            screen.blit(BACKGROUND_LIST[3], [0, 0])

            self.all_sprites_list_2.draw(screen)

            text_score = font.render("Score: " + str(self.score), True, WHITE)
            screen.blit(text_score, [5, 5])
            text_ammo = font.render(
                "AMMO: " + str(self.player.ammo), True, WHITE)
            screen.blit(
                text_ammo, [SCREEN_WIDTH-text_ammo.get_width()-40, SCREEN_HEIGHT - 40])
            if self.flag == 1:
                if self.high_score["Score"] < self.score:
                    self.new_high_score = True
                screen.blit(HEALTH[0], [
                    self.player.rect.x, self.player.rect.y - 4])
                self.game_state = 9

            else:
                if self.flag == 2:
                    if self.high_score["Score"] < self.score:
                        self.new_high_score = True
                    self.game_state = 10
                screen.blit(HEALTH[self.health_bar], [
                    self.player.rect.x, self.player.rect.y - 4])

        elif self.game_state == 8 or self.game_state == 7:
            time.sleep(1)
            game_instruction_text = game_titel_font.render(
                "Press ESC to get back to Menu", True, (47, 79, 79))
            game_instruction_text_1 = game_titel_font.render(
                "Press SPACE to go to the next Level", True, (47, 79, 79))
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
            screen.blit(BACKGROUND_LIST[9], [0, 0])

            game_over_text = game_titel_font.render(
                "Game Over \n leftclick to get back to the menu", True, WHITE)
            score_text = game_titel_font.render(
                "Your Score is: " + str(self.score), True, WHITE)
            previous_score_text = game_titel_font.render(
                "Your previous Score was: " + str(self.previous_score), True, WHITE)
            x = (SCREEN_WIDTH // 2) - (game_over_text.get_width() // 2)
            y = (SCREEN_HEIGHT // 2) - (game_over_text.get_height() // 2) - 200
            if self.new_high_score:
                input_rect = pygame.draw.rect(
                    screen, BLACK, [x, y+300, 300, 50])
                input_rect_frame = pygame.draw.rect(
                    screen, WHITE, [x, y+300, 300, 50], 3)
                high_score_text = game_titel_font.render(
                    "New Highscore! Write your name :) ", True, WHITE)
                name_text = game_titel_font.render(
                    self.high_score_name, True, WHITE)
                screen.blit(name_text, [x, y+300])
            else:
                high_score_text = game_titel_font.render(
                    "The Highscore is: " + self.high_score["Name"] + " "+str(self.high_score["Score"]), True, WHITE)

            screen.blit(game_over_text, [x, y])
            screen.blit(score_text, [x, y+150])
            screen.blit(previous_score_text, [x, y+200])

            screen.blit(high_score_text, [x, y+250])

        elif self.game_state == 10:
            screen.blit(BACKGROUND_LIST[9], [0, 0])
            game_won_text = game_titel_font.render(
                "You won! leftclick to get back to the menu", True, WHITE)
            x = (SCREEN_WIDTH // 2) - (game_won_text.get_width() // 2)
            y = (SCREEN_HEIGHT // 2) - (game_won_text.get_height() // 2)-200
            score_text = game_titel_font.render(
                "Your Score is: " + str(self.score), True, WHITE)
            previous_score_text = game_titel_font.render(
                "Your previous Score was: " + str(self.previous_score), True, WHITE)
            if self.new_high_score:
                input_rect = pygame.draw.rect(
                    screen, BLACK, [(SCREEN_WIDTH//2) + 150, (SCREEN_HEIGHT//2)+25, 300, 50])
                input_rect_frame = pygame.draw.rect(
                    screen, WHITE, [(SCREEN_WIDTH//2)+150, (SCREEN_HEIGHT//2)+25, 300, 50], 3)
                high_score_text = game_titel_font.render(
                    "New Highscore! Write your name :) ", True, WHITE)
                name_text = game_titel_font.render(
                    self.high_score_name, True, WHITE)
                screen.blit(name_text, [SCREEN_WIDTH//2,
                                        (SCREEN_HEIGHT//2)+50, 200, 50])
            else:
                high_score_text = game_titel_font.render(
                    "The Highscore is: " + self.high_score["Name"] + " "+str(self.high_score["Score"]), True, WHITE)
            screen.blit(game_won_text, [x, y])
            screen.blit(score_text, [x, y+150])
            screen.blit(previous_score_text, [x, y+200])
            screen.blit(high_score_text, [x, y+250])
        pygame.display.flip()
