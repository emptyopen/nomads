'''
everyone is a pixel, fighting against bosses. as more people play, pixels get smaller

You can be: Warrior (tanky), Hunter (ranged, pet), Mage (ranged, magic), Farmer, Medic

Stats/inventory are displayed on takaomatt.com

starts with 10x10 grid?
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


class Game:
# ----------------------------------------------------------------------------------------------------------------------------------- PREP

    def __init__(self):

        # window
        self.caption = "The Nomads"
        self.fps = 60
        self.clock = pg.time.Clock()
        self.grid_size_pixel = 800
        self.screen = pg.display.set_mode((1200, 800))
        self.background = pg.image.load('img/white-background.png')

        self.players = []
        self.num_players = len(self.players)
        self.grid_size = 5
        self.checkpoint = dt.datetime.now()

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

        # Decide action
        if dt.datetime.now() - self.checkpoint > dt.timedelta(seconds=10):
            if DEBUG:
                temp_action = raw_input('next action: ').lower()
                self.action = temp_action
            else:
                self.action = self.parse_twitch_chat_file()
            self.checkpoint = dt.datetime.now()

# DISPLAY -----------------------------------------------------------------------------------------------------------------------------------

    def update_display(self):

        self.screen.blit(self.background, (0,0))
        self.draw_board()
        background_color = (0, 0, 0)
        text_color = (255, 255, 255)
        time_left = str(10 - (dt.datetime.now() - self.checkpoint).seconds)
        font_object = pg.font.SysFont(FONT, FONTSIZE).render(time_left, True, text_color, background_color)
        self.screen.blit(font_object, (810, 20))



    def draw_board(self):
        interval = self.grid_size_pixel / round(self.grid_size)
        for i in range(1, self.grid_size):
            pg.draw.line(self.screen, (0, 0, 0), (i * interval, 0), (i * interval, self.grid_size_pixel))
            pg.draw.line(self.screen, (0, 0, 0), (0, i * interval), (self.grid_size_pixel, i * interval))

    def add_player(self, player):
        self.players.append(player)




class Player(object):

    def __init__(self):

        self.profession = 'Warrior'
        self.inventory = []
        self.equipped = {'head':None, 'chest':None, 'arms':None, 'legs':None, 'misc1':None, 'misc2':None}
        self.level = 1
        self.health = 10
        self.mana = 0

    def reset_character():
        pass

    def change_character():
        pass



class Boss():

    def __init__(self, health, abilities):
        self.health = health
        self.abilities = abilities

G = Game()
G.main()
