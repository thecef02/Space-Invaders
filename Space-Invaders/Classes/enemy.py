from constants import *
from Classes.moving_actor import MovingActor
import random, arcade
from Classes.experience import Experience

class Enemy(MovingActor):
    """ 
    Creates enemy class, which will be the base for all asteroids

    Attributes:
    base_setup (method) : base setup for enemies
    """
    def __init__(self, type = 1):
        """
        constructs enemy
        Args:
            type (int) : 2nd arg is optional but if it is not given, take type as 1.
        """
        super().__init__()
        self.base_setup()
        if type == 1:
            self.type1_setup()
        if type == 2:
            self.type2_setup()

    def base_setup(self):
        """
        base setup for the enemy
        Args:
        """
        self.center.x = random.randint(1, SCREEN_WIDTH)
        self.center.y = SCREEN_HEIGHT
        self.velocity.dx = random.uniform(-1 * ENEMY_SPEED, ENEMY_SPEED)
        self.velocity.dy = random.uniform(-1 * ENEMY_SPEED, -2 * ENEMY_SPEED)
        self.angle = ENEMY_SPIN
        self.rotateSpeed = ENEMY_SPIN
        self.radius = ENEMY_RADIUS
        self.alive = True
        self.size = 3
        self.image = ENEMY_IMAGE_1
        self.texture = arcade.load_texture(self.image)
        self.sound = arcade.Sound(EXPLOSION_SOUND)

    def type1_setup(self):
        """
        type1 enemy. Will take everything from base setup
        Args:
        """
        pass

    def type2_setup(self):
        """
        type2 enemy.
        Args:
        """
        self.velocity.dx = random.uniform(-6 * ENEMY_SPEED, 6* ENEMY_SPEED)
        self.velocity.dy = random.uniform(-1.5 * ENEMY_SPEED, -3 * ENEMY_SPEED)
        self.image = ENEMY_IMAGE_2
        self.texture = arcade.load_texture(self.image)

    def draw(self):
        """
        Draw a textured rectangle on the screen
        Args:
        """
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.texture.width/2, self.texture.height/2, self.texture, self.angle, 255)

    def split(self, experienceList):
        """
        change the bullet setting when game ends
        Args:
        exprienceList(list) : list of exprience
        """
        self.alive = False
        xp1 = Experience(self.center.x, self.center.y)
        self.sound.play(0.5, 1)
        experienceList.append(xp1)
        