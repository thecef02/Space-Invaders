
from Classes.moving_actor import MovingActor
from constants import *
import arcade, math

"""
Creates class for bullets
"""
class Bullet(MovingActor):
    def __init__(self, x, y):
        super().__init__()
        self.center.y = y
        self.center.x = x
        self.radius = BULLET_RADIUS
        self.rotateSpeed = SHIP_SPEED
        self.angle = BIG_ENEMY_SPIN
        self.image = ROOT + "/images/laser.png"
        self.sound = arcade.Sound(LASER_SOUND)
        self.texture = arcade.load_texture(self.image)
        self.alive = True
        self.time = 0

    def draw(self):
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.texture.width, self.texture.height, self.texture, self.angle, 255)

    def fire(self, angle, dx, dy):
        self.angle = angle + 90
        self.velocity.dy = math.sin(math.radians(self.angle)) * (dy + BULLET_SPEED)
        self.velocity.dx = math.cos(math.radians(self.angle)) * (dx + BULLET_SPEED)
        self.sound.play(0.2, 0)
        
    def advance(self):
        self.center.y += self.velocity.dy
        self.center.x += self.velocity.dx
        self.time += 1
        if self.time >= BULLET_LIFE:
            self.alive = False

    def is_off_screen(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        is_off_screen = False
        
        #Creates Screen Wrapping effect
        if self.center.x > SCREEN_WIDTH:
            self.center.x = 0
        elif self.center.x < 0:
            self.center.x = SCREEN_WIDTH
        return is_off_screen
   
        