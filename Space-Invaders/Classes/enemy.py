from constants import *
from Classes.moving_actor import MovingActor
import random, arcade
from Classes.experience import Experience


"""
Creates enemy class, which will be the base for all asteroids
currently set up as the large asteroid
2nd arg is optional. If it not given, it is 1.
"""

class Enemy(MovingActor):
    def __init__(self, type = 1):
        super().__init__()
        self.base_setup()
        if type == 1:
            self.type1_setup()
        if type == 2:
            self.type2_setup()

    def base_setup(self):
        self.center.x = random.randint(1, SCREEN_WIDTH)
        self.center.y = SCREEN_HEIGHT
        self.velocity.dx = random.uniform(-1 * BIG_ENEMY_SPEED, BIG_ENEMY_SPEED)
        self.velocity.dy = random.uniform(-1 * BIG_ENEMY_SPEED, -2 * BIG_ENEMY_SPEED)
        self.angle = BIG_ENEMY_SPIN
        self.rotateSpeed = BIG_ENEMY_SPIN
        self.radius = BIG_ENEMY_RADIUS
        self.alive = True
        self.size = 3
        self.image = ENEMY_IMAGE_1
        self.texture = arcade.load_texture(self.image)
        self.sound = arcade.Sound(EXPLOSION_SOUND)

    def type1_setup(self):
        pass

    def type2_setup(self):
        self.velocity.dx = random.uniform(-6 * BIG_ENEMY_SPEED, 6* BIG_ENEMY_SPEED)
        self.velocity.dy = random.uniform(-1.5 * BIG_ENEMY_SPEED, -3 * BIG_ENEMY_SPEED)
        self.image = ENEMY_IMAGE_2
        self.texture = arcade.load_texture(self.image)

    def draw(self):
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.texture.width/2, self.texture.height/2, self.texture, self.angle, 255)

    def split(self, experienceList):
        self.alive = False
        xp1 = Experience(self.center.x, self.center.y)
        #smallEnemy1 = SmallEnemy(self.center.x, self.center.y)
        self.sound.play(0.5, 1)
        experienceList.append(xp1)
        #WINDOW.enemies.append(smallEnemy1)