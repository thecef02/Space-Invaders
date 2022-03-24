from constants import *
from Classes.moving_actor import MovingActor
import random, arcade
from Classes.experience import Experience




"""
Creates enemy class, which will be the base for all asteroids
currently set up as the large asteroid
"""
class Enemy(MovingActor):
    def __init__(self):
        super().__init__()
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
        
    def draw(self):
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.texture.width/2, self.texture.height/2, self.texture, self.angle, 255)



    def split(self, experienceList):
        self.alive = False
        xp1 = Experience(self.center.x, self.center.y)
        #smallEnemy1 = SmallEnemy(self.center.x, self.center.y)
        self.sound.play(0.5, 1)
        experienceList.append(xp1)
        #WINDOW.enemies.append(smallEnemy1)