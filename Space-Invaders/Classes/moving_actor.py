from abc import ABC
from Classes.point import Point
from Classes.velocity import Velocity
from constants import *
"""
Creates Abstract Flying object class, used to help define other classes
"""     
class MovingActor(ABC):

    
    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()
        
    def advance(self):
        self.center.y += self.velocity.dy
        self.center.x += self.velocity.dx

    def draw(self):
        return

    def is_off_screen(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        is_off_screen = False
        
        #Creates Screen Wrapping effect
        if self.center.x > SCREEN_WIDTH:
            self.center.x = 0
        elif self.center.x < 0:
            self.center.x = SCREEN_WIDTH
        elif self.center.y > SCREEN_HEIGHT:
            self.center.y = 0
        elif self.center.y < 0:
            self.center.y = SCREEN_HEIGHT
        return is_off_screen