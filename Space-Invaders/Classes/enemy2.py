from Classes.enemy import Enemy
from constants import *
import random, arcade


class Enemy2(Enemy):
    def __init__(self):
        super().__init__()
        self.velocity.dx = random.uniform(-6 * BIG_ENEMY_SPEED, 6* BIG_ENEMY_SPEED)
        self.velocity.dy = random.uniform(-1.5 * BIG_ENEMY_SPEED, -3 * BIG_ENEMY_SPEED)
        self.image = ENEMY_IMAGE_2
        self.texture = arcade.load_texture(self.image)