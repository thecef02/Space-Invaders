
from constants import *
from Classes.moving_actor import MovingActor
import math, arcade

"""
Experience: this will display the experience ball.
    Attributes:
    center.y (float) : y value for the bullte
    center.x (float) : x value for the bullet
    radius (float) : radius of the bullet
    angle (int) : angle of the bullet
    image (png) : image of the bullet
    sound (arcade) : sound when bullet is fired
    texture (arcade) : loading image of bullet
    alive (boolean) : if game end, bullet isn't alive
    rotate (float): in case the image is different shape than a circle
    retatespeed (float) : the speed of the rotation
    sound (int) : the sound number to play

"""
class Experience(MovingActor):
    def __init__(self, x, y):
        """
        Constructor of the experience image
        Args:
        x (float) : a x position 
        y (float) : a y position
        """
        super().__init__()
        self.center.x = x
        self.center.y = y
        self.velocity.dx = 0
        self.velocity.dy = 0
        self.angle = EXPERIENCE_SPIN
        self.rotateSpeed = 0
        self.radius = EXPERIENCE_RADIUS
        self.image = ROOT + "/images/xp.png"
        self.texture = arcade.load_texture(self.image)
        self.sound = arcade.Sound(PICKUP_SOUND)
        self.size = 2
        self.alive = True
    def advance(self, shipx, shipy):
        """
        This will move the experience actor towars the ship
        Args:
        shipx (float) : the x position of the ship
        shipy (float) : the y position of the ship
        """
        self.center.x += -3 * ((self.center.x - shipx)/(SCREEN_WIDTH/2)) 
        self.center.y += -3 * ((self.center.y - shipy)/shipy) 

        #self.center.x += -1 * (self.center.x/WINDOW.ship.center.x) 
        #self.center.y += -1 * (self.center.y/WINDOW.ship.center.y)     
    def draw(self):
        """draw the actor
        """
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.texture.width/2, self.texture.height/2, self.texture, self.angle, 255)
    def split(self):
        """flag to clear the actor from the screen
        """
        self.alive = False