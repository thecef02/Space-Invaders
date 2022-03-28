
# from pickle import TRUE
from Classes.game import Game
from constants import *
import arcade
"""
Creates Abstract Flying object class, used to help define other classes
"""     
# Creates the game and starts it going
WINDOW = Game(SCREEN_WIDTH, SCREEN_HEIGHT)

arcade.run()
