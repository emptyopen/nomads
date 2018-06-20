'''
everyone is a pixel, fighting against bosses. as more people play, pixels get
smaller

You can be: Warrior (tanky), Hunter (ranged, pet), Mage (ranged, magic),
Farmer, Medic

Stats/inventory are displayed on takaomatt.com

starts with 10x10 grid?

anyone who types during setup period will not be eligible for entering next
'''

import random
import string
import datetime as dt
import sys
import os
import numpy as np
import pygame as pg
from pygame.locals import QUIT
import textwrap
pg.font.init()

FONT = 'aerxtablets'
FONTSIZE = 28
DEBUG = True
WIDTH = 800
HEIGHT = 800


class Game:

    def __init__(self):

        self.caption = "The Nomads"
        self.fps = 60
        self.clock = pg.time.Clock()
        self.grid_size_pixel = 800
        self.grid_size = 10
        self.grid_interval = self.grid_size_pixel / self.grid_size
        self.screen = pg.display.set_mode((WIDTH + 400, HEIGHT))
        self.background = pg.image.load('img/white-background.png')

        self.players = []
        self.player_limit = 5
        self.checkpoint = dt.datetime.now()
        self.all_sprites = pg.sprite.Group()

    def main(self):

        pg.init()
        pg.display.set_caption(self.caption)

        while True:
            self.update_state()
            self.update_display()
            pg.display.update()
            self.clock.tick(self.fps)
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit

# STATE -----------------------------------------------------------------------

    def update_state(self):

        if dt.datetime.now() - self.checkpoint > dt.timedelta(seconds=10):
            if DEBUG:
                temp_action = raw_input('next action: ').lower()
                self.action = temp_action
            else:
                self.action = self.parse_twitch_chat_file()
            self.checkpoint = dt.datetime.now()

# DISPLAY ---------------------------------------------------------------------

    def update_display(self):

        self.screen.blit(self.background, (0, 0))
        self.draw_board()
        self.draw_players()
        self.draw_boss()
        self.draw_time()

# DRAW ------------------------------------------------------------------------

    def draw_board(self):

        interval = self.grid_size_pixel / round(self.grid_size)
        for i in range(1, self.grid_size):
            pg.draw.line(self.screen, (100, 100, 100), (i * interval, 0),
                         (i * interval, self.grid_size_pixel))
            pg.draw.line(self.screen, (100, 100, 100), (0, i * interval),
                         (self.grid_size_pixel, i * interval))

    def draw_players(self):

        self.all_sprites.update()
        self.all_sprites.draw(self.screen)

    def draw_boss(self):

        pass

    def draw_time(self):

        time_left = str(10 - (dt.datetime.now() - self.checkpoint).seconds)
        font_object = pg.font.SysFont(FONT, FONTSIZE)
        font_object = font_object.render(time_left, True, (255, 255, 255),
                                         (0, 0, 0))
        self.screen.blit(font_object, (810, 20))

# STATUS TOOLS ----------------------------------------------------------------

    def add_player(self, player):

        if len(self.players) < self.player_limit:
            player.rect.x = self.grid_interval * 4 + 5
            player.rect.y = self.grid_interval * 4 + 5
            player.change_size_color(self.grid_interval - 5,
                                     self.grid_interval - 5)
            self.players.append(player)
            self.all_sprites.add(player)


class Player(pg.sprite.Sprite):

    def __init__(self, username, profession='Warrior'):

        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([71, 71])
        self.image.fill(list(np.random.choice(range(256), size=3)))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 5, 5

        self.username = username
        self.profession = profession
        self.inventory = []
        self.equipped = {'head': None, 'chest': None, 'arms': None,
                         'legs': None, 'misc1': None, 'misc2': None}
        self.level = 1
        self.health = 10
        self.mana = 0

    def reset_character(self):

        pass

    def change_character(self):

        pass

    def change_size_color(self, x, y, color=list(np.random.choice(range(256),
                                                 size=3))):

        self.image = pg.Surface([x, y])
        self.image.fill(color)
        self.rect = self.image.get_rect()


class Boss():

    def __init__(self, health, abilities):

        self.health = health
        self.abilities = abilities


G = Game()
P = Player('emptyopen')
G.add_player(P)
G.main()
