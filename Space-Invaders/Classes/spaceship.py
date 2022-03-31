from constants import *
from Classes.moving_actor import MovingActor


class SpaceShip(MovingActor):
    """ This works as the main class for the player, creating the spaceship 

    Attributes:
    center.y (float) : y value for the ship
    center.x (float) : x value for the ship
    angle (int) : angle of the ship
    accelerate (int) : Thrust amount for ship (if we decide we want a velocity based movement)
    moveSpeed (int) : Speed that the Ship moves at. Point based movement rather than velocity based
    alive (boolean) : Keeps track of if the ship is alive
    radius (int): keeps track of the size of the hitbox
    points (int) : Point obtained by the player
    image (png) : image of the ship
    texture (arcade) : loading image of ship
    time (int) : time for alive
    """
    def __init__(self):
        """
        constructs Spaceship
        Args:
            none
        """
        super().__init__()
        self.center.y = SCREEN_HEIGHT/15 + 60
        self.center.x = SCREEN_WIDTH/2
        self.angle = 0
        #self.accelerate = SHIP_THRUST_AMOUNT
        self.moveSpeed = SHIP_SPEED
        self.alive = True
        self.radius = SHIP_RADIUS
        self.lives = SHIP_LIVES
        self.points = START_POINTS
        self.image = SHIP_IMAGE
        self.texture = arcade.load_texture(self.image)

    def draw(self):
        """
        draw method for the spaceship, draws a rectangle with self.texture
        Args:
            none
        """
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.texture.width*SHIP_SCALE, self.texture.height*SHIP_SCALE, self.texture, self.angle, 255)

    def goLeft(self):
        """
        Used to move the spaceship to the left
        Args:
            none
        """
        self.center.x -= self.moveSpeed 
        #self.velocity.dx -= self.accelerate
        
    def goRight(self):
        """
        Used to move the spaceship to the right
        Args:
            none
        """
        self.center.x += self.moveSpeed
        #self.velocity.dx += self.accelerate
        
    def goForward(self):
        """
        Used to move the spaceship forward (slower right/left movement is more important)
        Args:
            none
        """
        self.center.y += self.moveSpeed/2 
       
        
    def goBack(self):
        """
        Used to move the spaceship backwards (slower right/left movement is more important)
        Args:
            none
        """
        self.center.y -= self.moveSpeed/2 
     
    def death(self):
        """
        Changes spaceship image on death
        Args:
            none
        """
        self.image = EXPLOSION_IMAGE
        self.texture = arcade.load_texture(self.image)

    def is_off_screen(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        """
        Keeps the ship from leaving the screen
        Args:
            SCREEN_WIDTH (INT) : Width of screen 
            SCREEN_HEIGHT (INT) : height of screen
        """
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