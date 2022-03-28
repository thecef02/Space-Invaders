

import os,sys, arcade, random, math
from arcade.color import BLUE, RED


LEVEL_10= ["Wave 10", "A", "B", "B", "B", "B", "B", "B", "B", "B", "A", "A", "A","B", "B", "A","B", "B", "A","B", "B", "A","B", "B", "A", "end"]
LEVEL_9 = ["Wave 9", "A", "B", "B", "B", "B", "B", "B", "B", "A","B", "B", "A","B", "B", "A","B", "B", "A","B", "B", "A", globals()["LEVEL_10"]]
LEVEL_8 = ["Wave 8", "A", "B", "A", "A", "B", "A", "B", "B", "A","A", "B", "A","A", "B", "A", "B", "B", "A", globals()["LEVEL_9"]]
LEVEL_7 = ["Wave 7", "A", "B", "A", "B", "B", "A", "A", "B", "A", "A", "B", "B","B", "B", "A", globals()["LEVEL_8"]]
LEVEL_6 = ["Wave 6", "A", "B", "B", "B", "B", "A", "A", "B", "B", "A", "B", "A", globals()["LEVEL_7"]]
LEVEL_5 = ["Wave 5", "A", "B", "B", "A", "B", "A", "B", "B", "A", "B", globals()["LEVEL_6"]]
LEVEL_4 = ["Wave 4", "A", "B", "A", "A", "B", "A","A", "B", "A", globals()["LEVEL_5"]]
LEVEL_3 = ["Wave 3", "A", "B", "A", "A", "A","A", "B", "A", globals()["LEVEL_4"]]
LEVEL_2 = ["Wave 2", "A", "B", "A", "A", "A", "B", "A", globals()["LEVEL_3"]]
LEVEL_1 = ["Wave 1", "A", "B", "A", "A", "B", "A", globals()["LEVEL_2"]]



SCREEN_WIDTH = 600
SCREEN_HEIGHT = 900

BULLET_RADIUS = 10
BULLET_SPEED = 10
BULLET_LIFE = 90

SHIP_SPEED = 8
#Modifying ship for easier control
SHIP_THRUST_AMOUNT = 0.25/25
SHIP_RADIUS = 30
SHIP_LIVES = 1
SHIP_SCALE = .8
START_POINTS = 0

ROOT = os.path.dirname(sys.modules['__main__'].__file__)
EXPLOSION_SOUND = ROOT + "/sounds/explosion.wav" 
LASER_SOUND = ROOT + "/sounds/laserShoot.wav"
START_SOUND = ROOT + "/sounds/start.wav"
HURT_SOUND = ROOT + "/sounds/hitHurt.wav"
PICKUP_SOUND = ROOT + "/sounds/pickup.wav"
MUSIC = ROOT + "/sounds/ai_song.wav"

INITIAL_ENEMY_COUNT = 10

BIG_ENEMY_SPIN = 0
BIG_ENEMY_SPEED = 1.5
BIG_ENEMY_RADIUS = 15
ENEMY_IMAGE_1 = ROOT + "/images/enemy.png"
ENEMY_IMAGE_2 = ROOT + "/images/enemy2.png"

MEDIUM_ENEMY_SPIN = -2
MEDIUM_ENEMY_RADIUS = 5

SMALL_ENEMY_SPIN = 5
SMALL_ENEMY_RADIUS = 2

ENEMY_AMOUNT = 2 