# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 15:03:07 2018

@author: Mechkro
"""

#Defining RGB Color Combos
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

#Game Settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16 - Needs to be easily divisible
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12 - Needs to be easily divisible
FPS = 60                            
TITLE = "Marine Pyrena"
BGCOLOR = DARKGREY

TILESIZE = 32                       #Tile Size - dependent on pref. and art
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE
