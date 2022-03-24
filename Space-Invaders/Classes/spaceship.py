from constants import *
from Classes.moving_actor import MovingActor

"""
Sets up Spaceship class. this is the player
"""
class SpaceShip(MovingActor):
    def __init__(self):
        super().__init__()
        print(SCREEN_HEIGHT)
        self.center.y = SCREEN_HEIGHT/15
        self.center.x = SCREEN_WIDTH/2
        self.angle = 0
        self.accelerate = SHIP_THRUST_AMOUNT
        self.moveSpeed = SHIP_SPEED
        self.alive = True
        self.isShooting = True
        self.radius = SHIP_RADIUS
        self.lives = SHIP_LIVES
        self.points = START_POINTS
        self.image = ROOT + "/images/playerShip.png"
        self.texture = arcade.load_texture(self.image)

    def draw(self):
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.texture.width*SHIP_SCALE, self.texture.height*SHIP_SCALE, self.texture, self.angle, 255)

    def goLeft(self):
        self.center.x -= self.moveSpeed 
        #self.velocity.dx -= self.accelerate
        
    def goRight(self):
        self.center.x += self.moveSpeed
        #self.velocity.dx += self.accelerate
        
    def goForward(self):
        self.center.y += self.moveSpeed/2 
       
        
    def goBack(self):
        self.center.y -= self.moveSpeed/2 
     
    def death(self):
        self.image = ROOT + "/images/playerShip.png"
        self.texture = arcade.load_texture(self.image)

    def is_off_screen(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        is_off_screen = False
        #Creates Screen Bounds
        if self.center.x > SCREEN_WIDTH:
            self.center.x = SCREEN_WIDTH -1
        elif self.center.x < 5:
            self.center.x = 5
        elif self.center.y > SCREEN_HEIGHT:
            self.center.y = SCREEN_HEIGHT - 1
        elif self.center.y < 1:
            self.center.y = 1
        return is_off_screen