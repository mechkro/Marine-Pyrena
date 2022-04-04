# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 15:05:11 2018

@author: Mechkro
"""

from lib2to3 import pygram
import pygame as pg
from settings import *

#Soldier Creation Class - For now it will be just a single player vs mob type
#functionality. Later on will look into need for additional classes if necc.
#for multiplayer across networks.

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        """Define players position in terms of x and y and alters it by the
        change in x and y"""
        i = pg.sprite.spritecollide(self, self.game.walls, False)
        if i:
            if dx:
                self.x += -1
            if dy:
                self.y += -1
        else:
            self.x += dx
            self.y += dy

    def update(self):
        """Update func to supply positional data at an innstant"""
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

#Defining the walls which act as an enviroment boundries. Will define player
#Movements.
        
class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
