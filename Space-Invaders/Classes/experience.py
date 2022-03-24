
from constants import *
from Classes.moving_actor import MovingActor
import math, arcade

"""
Experience
"""
class Experience(MovingActor):
    def __init__(self, x, y):
        super().__init__()
        self.center.x = x
        self.center.y = y
        self.velocity.dx = math.sin(WINDOW.ship.center.x/self.center.x)
        self.velocity.dy = math.sin(WINDOW.ship.center.y/self.center.y)
        self.angle = MEDIUM_ENEMY_SPIN
        self.rotateSpeed = 0
        self.radius = MEDIUM_ENEMY_RADIUS
        self.radius = BIG_ENEMY_RADIUS
        self.image = ROOT + "/images/xp.png"
        self.texture = arcade.load_texture(self.image)
        self.sound = arcade.Sound(PICKUP_SOUND)
        self.size = 2
        self.alive = True
    def advance(self):
        self.center.x += -3 * ((self.center.x - WINDOW.ship.center.x)/(SCREEN_WIDTH/2)) 
        self.center.y += -3 * ((self.center.y - WINDOW.ship.center.y)/WINDOW.ship.center.y) 

        #self.center.x += -1 * (self.center.x/WINDOW.ship.center.x) 
        #self.center.y += -1 * (self.center.y/WINDOW.ship.center.y)     
    def draw(self):
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.texture.width/2, self.texture.height/2, self.texture, self.angle, 255)
    def split(self):
        self.alive = False