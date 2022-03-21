
from pickle import TRUE
from turtle import Screen
import arcade
import math
import random
from abc import ABC
import pathlib, os, sys
from arcade.color import BLUE, RED


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 900

BULLET_RADIUS = 10
BULLET_SPEED = 10
BULLET_LIFE = 90

SHIP_SPEED = 8
#Modifying ship for easier control
SHIP_THRUST_AMOUNT = 0.25/25
SHIP_RADIUS = 30
SHIP_LIVES = 1
SHIP_SCALE = .8
START_POINTS = 0

ROOT = os.path.dirname(sys.modules['__main__'].__file__)
EXPLOSION_SOUND = ROOT + "/sounds/explosion.wav" 
LASER_SOUND = ROOT + "/sounds/laserShoot.wav"
START_SOUND = ROOT + "/sounds/start.wav"
HURT_SOUND = ROOT + "/sounds/hitHurt.wav"
PICKUP_SOUND = ROOT + "/sounds/pickup.wav"
MUSIC = ROOT + "/sounds/ai_song.wav"

INITIAL_ENEMY_COUNT = 10

BIG_ENEMY_SPIN = 0
BIG_ENEMY_SPEED = 1.5
BIG_ENEMY_RADIUS = 15
ENEMY_IMAGE_1 = ROOT + "/images/enemy.png"
ENEMY_IMAGE_2 = ROOT + "/images/enemy2.png"

MEDIUM_ENEMY_SPIN = -2
MEDIUM_ENEMY_RADIUS = 5

SMALL_ENEMY_SPIN = 5
SMALL_ENEMY_RADIUS = 2

ENEMY_AMOUNT = 2 

"""
Creates Point class, used to keep track of location
"""
class Point:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
"""
Creates Velocity class, used to keep track of movement
"""        
class Velocity:
    def __init__(self):
        self.dx = 0.0
        self.dy = 0.0

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



    def split(self):
        self.alive = False
        xp1 = Experience(self.center.x, self.center.y)
        #smallEnemy1 = SmallEnemy(self.center.x, self.center.y)
        self.sound.play(0.5, 1)
        window.experience.append(xp1)
        #window.enemies.append(smallEnemy1)

class Enemy2(Enemy):
    def __init__(self):
        super().__init__()
        self.velocity.dx = random.uniform(-6 * BIG_ENEMY_SPEED, 6* BIG_ENEMY_SPEED)
        self.velocity.dy = random.uniform(-1.5 * BIG_ENEMY_SPEED, -3 * BIG_ENEMY_SPEED)
        self.image = ENEMY_IMAGE_2
        self.texture = arcade.load_texture(self.image)
    



"""
Experience
"""
class Experience(MovingActor):
    def __init__(self, x, y):
        super().__init__()
        self.center.x = x
        self.center.y = y
        self.velocity.dx = math.sin(window.ship.center.x/self.center.x)
        self.velocity.dy = math.sin(window.ship.center.y/self.center.y)
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
        self.center.x += -3 * ((self.center.x - window.ship.center.x)/(SCREEN_WIDTH/2)) 
        self.center.y += -3 * ((self.center.y - window.ship.center.y)/window.ship.center.y) 

        #self.center.x += -1 * (self.center.x/window.ship.center.x) 
        #self.center.y += -1 * (self.center.y/window.ship.center.y)     
    def draw(self):
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.texture.width/2, self.texture.height/2, self.texture, self.angle, 255)
    def split(self):
        self.alive = False
     


        
             
"""
Sets up Spaceship class. this is the player
"""
class SpaceShip(MovingActor):
    def __init__(self):
        super().__init__()
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
   
        


class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

        self.held_keys = set()
        self.ship = SpaceShip()
        self.bullets = []
        self.enemies = []
        self.experience = []
        self.enemyMax = ENEMY_AMOUNT

        #Looking into animation
        #self.player_list = arcade.SpriteList()
        #self.player_sprite = arcade.Sprite(ENEMY_IMAGE_1, 1)
        #self.player_sprite.center_x = 50
        #self.player_sprite.center_y = 50
        #self.player_list.append(self.player_sprite)

        
        arcade.Sound(START_SOUND).play(0.5, 0)
        arcade.Sound(MUSIC).play(.5, 0, True)


        # TODO: declare anything here you need the game class to track
        

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()
        self.ship.draw()

        # TODO: draw each object
        for bullet in self.bullets:
            bullet.draw()

        for enemy in self.enemies:
            enemy.draw()

        for experience in self.experience:
            experience.draw()

        self.draw_lives()
        self.draw_points()

        if self.ship.alive == False:
            self.game_over()

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()
        self.check_collisions()
        self.check_off_screen()
        self.cleanup()
        self.create_enemy()
        
        
        # TODO: Tell everything to advance or move forward one step in time
        for bullet in self.bullets:
            bullet.advance()
            

        for enemy in self.enemies:
            enemy.advance()

        for experience in self.experience:
            experience.advance()
        
        
            self.ship.advance()

        # TODO: Check for collisions
    def draw_lives(self):
        """
        Puts the current score on the screen
        """
        lives_text = "Life: {}".format(self.ship.lives)
        lives_x = 10
        lives_y = SCREEN_HEIGHT - 40
        arcade.draw_text(lives_text, start_x=lives_x, start_y=lives_y, font_size=30, color=arcade.color.WHITE)
    
    def draw_points(self):
        points_text = "Points: {}".format(self.ship.points)
        points_x = SCREEN_WIDTH - 200
        points_y = SCREEN_HEIGHT - 40
        arcade.draw_text(points_text, start_x=points_x, start_y=points_y, font_size=30, color=arcade.color.WHITE)

    def game_over(self):
        """
        Puts the current score on the screen
        """
        gameOver_text = "Game Over"
        gameOver_x = SCREEN_WIDTH/2 - 220
        gameOver_y = SCREEN_HEIGHT/2
        arcade.draw_text(gameOver_text, start_x=gameOver_x, start_y=gameOver_y, font_size=60, color=arcade.color.WHITE)

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys or arcade.key.A in self.held_keys:
            self.ship.goLeft()
            

        if arcade.key.RIGHT in self.held_keys or arcade.key.D in self.held_keys:
            self.ship.goRight()
            

        if arcade.key.UP in self.held_keys or arcade.key.W in self.held_keys:
            self.ship.goForward()

        if arcade.key.DOWN in self.held_keys or arcade.key.S in self.held_keys:
            self.ship.goBack()

    
        


        
        

        # Machine gun mode...
        #if arcade.key.SPACE in self.held_keys:
        #    pass

    def check_off_screen(self):
        """
        Checks to see if bullets or targets have left the screen
        and if so wraps them around
        """
        for bullet in self.bullets:
            if bullet.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.bullets.remove(bullet)

        for enemy in self.enemies:
            enemy.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT)

        for experience in self.experience:
            experience.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT)
            
        self.ship.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT)


    def check_collisions(self):
        """
        Checks Collisions
        """

       
        for bullet in self.bullets:
            for enemy in self.enemies:

               
                if bullet.alive and enemy.alive:
                    too_close = bullet.radius + enemy.radius

                    if (abs(bullet.center.x - enemy.center.x) < too_close and
                                abs(bullet.center.y - enemy.center.y) < too_close):
                        bullet.alive = False
                        enemy.split()
                        
        for enemy in self.enemies:
            
            too_close = enemy.radius + self.ship.radius

            if (abs(enemy.center.x - self.ship.center.x) < too_close and
                    abs(enemy.center.y - self.ship.center.y) < too_close):
                enemy.rotateSpeed *= -1       
                self.ship.velocity.dx = (-.7 * self.ship.velocity.dx)
                self.ship.velocity.dy = (-.7 * self.ship.velocity.dy)
                self.ship.lives -= 1
                if self.ship.lives <= 0:
                    self.ship.alive = False
                    

        for experience in self.experience:
            
            too_close = experience.radius + self.ship.radius

            if (abs(experience.center.x - self.ship.center.x) < too_close and
                    abs(experience.center.y - self.ship.center.y) < too_close):
                experience.alive = False
                self.ship.points += 1
                experience.sound.play(0.05, 0.01)
                if(self.ship.points % 10 == 0):
                    self.enemyMax += 1
                          
                        # We will wait to remove the dead objects until after we
                        # finish going through the list

        # Now, check for anything that is dead, and remove it
        self.cleanup()

                
    def cleanup(self):
        for bullet in self.bullets:
            if bullet.alive == False:
                self.bullets.remove(bullet)
        for enemy in self.enemies:
            if enemy.alive == False:
                self.enemies.remove(enemy)
        for experience in self.experience:
            if experience.alive == False:
                self.experience.remove(experience)
        if self.ship.alive == False:
            self.ship.death()
      
                

    def create_enemy(self):
       
        while len(self.enemies) < self.enemyMax:
            x = random.randint(1, 2)
            if x == 1:      
                enemy = Enemy()
            else:
                enemy = Enemy2()
            self.enemies.append(enemy)
        

    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        if self.ship.alive == True:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                bullet = Bullet(self.ship.center.x, self.ship.center.y)
                bullet2 = Bullet(self.ship.center.x, self.ship.center.y - 10)
                bullet3 = Bullet(self.ship.center.x, self.ship.center.y - 10)
            
                bullet.fire(self.ship.angle, self.ship.velocity.dx, self.ship.velocity.dy)
                bullet2.fire(-5, self.ship.velocity.dx, self.ship.velocity.dy)
                bullet3.fire( 5, self.ship.velocity.dx, self.ship.velocity.dy)
                
                if self.ship.points < 50:
                    self.bullets.append(bullet)
                elif self.ship.points >= 50 and self.ship.points < 100:
                    self.bullets.append(bullet2)
                    self.bullets.append(bullet3)
                elif self.ship.points >= 100:
                    self.bullets.append(bullet)
                    self.bullets.append(bullet2)
                    self.bullets.append(bullet3)
                


                pass

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)

arcade.run()
