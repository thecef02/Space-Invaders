
from Classes.moving_actor import MovingActor
from constants import *
import arcade, math

class Bullet(MovingActor):
    """ This will display bullets.

    Attributes:
    center.y (float) : y value for the bullte
    center.x (float) : x value for the bullet
    radius (float) : radius of the bullet
    angle (int) : angle of the bullet
    image (png) : image of the bullet
    sound (arcade) : sound when bullet is fired
    texture (arcade) : loading image of bullet
    alive (boolean) : if game end, bullet isn't alive
    time (int) : time for alive
    """
    def __init__(self, x, y):
        """
        constructs Bullet
        Args:
            center.y(int): bullet position in y
            center.x(int): bullet position in x
        """
        super().__init__()
        self.center.y = y
        self.center.x = x
        self.radius = BULLET_RADIUS
        self.angle = BULLET_SPIN
        self.image = ROOT + "/images/laser.png"
        self.sound = arcade.Sound(LASER_SOUND)
        self.texture = arcade.load_texture(self.image)
        self.alive = True
        self.time = 0
        super().advance()
        self.time += 1
        if self.time >= BULLET_LIFE:
            self.alive = False


    def draw(self):
        """
        Draw the way of bullets
        Args:
        """
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.texture.width, self.texture.height, self.texture, self.angle, 255)

    def fire(self, angle, dx, dy):
        """
        Shot the Bullet
        Args:
            angle(int): angle of bullets
            velocity.dy(float): velocity for dx
            velocity.dx(float): velocity for dy
        """
        self.angle = angle + 90
        self.velocity.dy = math.sin(math.radians(self.angle)) * (dy + BULLET_SPEED)
        self.velocity.dx = math.cos(math.radians(self.angle)) * (dx + BULLET_SPEED)
        self.sound.play(0.2, 0)

    def is_off_screen(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        """
        Bullets should be inside of the screen
        Args:
            SCREEN_WIDTH(int): width of screen
            SCREEN_HEIGHT(INT): height of screen
        """
        is_off_screen = False
        
        #Creates Screen Wrapping effect
        if self.center.x > SCREEN_WIDTH:
            self.center.x = 0
        elif self.center.x < 0:
            self.center.x = SCREEN_WIDTH
        elif self.center.y > SCREEN_HEIGHT:
            is_off_screen = True
        return is_off_screen
   
        