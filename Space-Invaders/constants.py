import pathlib, os, sys
from game.casting.color import Color

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Batter"
FRAME_RATE = 60
ROOT = os.path.dirname(sys.modules['__main__'].__file__) 
# SCREEN
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = ROOT + "/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
EXPLOSION_SOUND = ROOT + "/assets/NewSounds/explosion.wav"
HURT_SOUND = ROOT + "/assets/NewSounds/hithurt.wav"
LASER_SOUND = ROOT + "/assets/NewSounds/laserShoot.wav"
PICKUP_SOUND = ROOT + "/assets/NewSounds/laserShoot.wav"
WELCOME_SOUND = ROOT + "/assets/sounds/start.wav"
OVER_SOUND = ROOT + "/assets/sounds/over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# LEVELS
LEVEL_FILE = ROOT + "/assets/data/level-{:03}.txt"
BASE_LEVELS = 5

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5

# HUD
HUD_MARGIN = 15
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
LEVEL_FORMAT = "LEVEL: {}"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"

# BALL
BALL_GROUP = "balls"
BALL_IMAGE = ROOT + "/assets/images/000.png"
BALL_WIDTH = 100
BALL_HEIGHT = 180
BALL_VELOCITY = 6

# SPACE SHIP
RACKET_GROUP = "rackets"
RACKET_IMAGES = [f"{ROOT}/assets/images/{n:03}.png" for n in range(100, 103)]
RACKET_WIDTH = 72
RACKET_HEIGHT = 74
RACKET_RATE = 6
RACKET_VELOCITY = 7

# BRICK
BRICK_GROUP = "bricks"
BRICK_IMAGES = {
    "b": [f"{ROOT}/assets/images/{i:03}.png" for i in range(10,19)],
    "g": [f"{ROOT}/assets/images/{i:03}.png" for i in range(20,29)],
    "p": [f"{ROOT}/assets/images/{i:03}.png" for i in range(30,39)],
    "y": [f"{ROOT}/assets/images/{i:03}.png" for i in range(40,49)]
}
BRICK_WIDTH = 80
BRICK_HEIGHT = 28
BRICK_DELAY = 0.5
BRICK_RATE = 4
BRICK_POINTS = 50

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"