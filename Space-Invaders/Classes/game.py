from constants import *
from Classes.spaceship import SpaceShip
from Classes.enemy import Enemy
from Classes.wave_handler import WaveHandler
from Classes.bullet import Bullet
import os


class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    This class will then call the appropriate functions of
    each of the above classes.

    Atributtes:
    backgrounds (arcade): set the texture of the background of screen.
    held_keys (arcade): keys that are being held down
    ship: The ship of our responsability
    bullets (list): Quantity of bullets 
    enemies (list): All the asteroids who came to attack us
    experience (list): Number of rounds runs
    enemyMax (int): The amount of the enemies
    wave (list): the level of enemies .

    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        Args:
            width: Screen width
            height: Screen height
        """
        super().__init__(width, height)
        self.background = arcade.load_texture(ROOT +'/images/background.jpg')

        self.held_keys = set()
        self.ship = SpaceShip()
        self.bullets = []
        self.enemies = []
        self.experience = []
        self.enemyMax = ENEMY_AMOUNT
        self.wave = WaveHandler()
        self.wave.nextWave(LEVEL_1)
        
       

        #Looking into animation
        #self.player_list = arcade.SpriteList()
        #self.player_sprite = arcade.Sprite(ENEMY_IMAGE_1, 1)
        #self.player_sprite.center_x = 50
        #self.player_sprite.center_y = 50
        #self.player_list.append(self.player_sprite)

        self.create_enemy()
        arcade.Sound(START_SOUND).play(0.5, 0)
        arcade.Sound(MUSIC).play(.5, 0, True)


        # TODO: declare anything here you need the game class to track
        

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        Args:
            none
        """

        # clear the screen to begin drawing
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.ship.draw()

        # TODO: draw each object
        # print(f"Drawing {len(self.bullets)} bullets, {len(self.enemies)} enemies, {len(self.experience)} experiences")
        for bullet in self.bullets:
            bullet.draw()
        
        for enemy in self.enemies:
            enemy.draw()
        
        for experience in self.experience:
            experience.draw()

        self.draw_lives()
        self.draw_points()
        self.draw_wave()

        if self.ship.alive == False:
            self.game_over()

    def update(self, delta_time):
        """
        This function update each object in the game.
        Args:
            delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()
        self.check_collisions()
        self.check_off_screen()
        self.cleanup()
        self.check_wave_remainder()
        
        
        
        # TODO: Tell everything to advance or move forward one step in time
        # print(f"Advancing {len(self.bullets)} bullets, {len(self.enemies)} enemies, {len(self.experience)} experiences")
        for bullet in self.bullets:
            bullet.advance()
            

        for enemy in self.enemies:
            enemy.advance()

        for experience in self.experience:
            experience.advance(self.ship.center.x, self.ship.center.y)
        
        
            self.ship.advance()

        # TODO: Check for collisions

    def draw_lives(self):
        """
        This function puts the current lifes on the screen
        Args:
            none
        """
        lives = self.ship.lives
        lives_text = "Life: {}".format(lives)
        lives_x = 80
        lives_y = SCREEN_HEIGHT - 50
        if lives >= 1:
            arcade.draw_text(lives_text, start_x=lives_x, start_y=lives_y, font_size=30, color=arcade.color.WHITE, font_name="Kenney Pixel")
        else:
            arcade.draw_text("Life: 0", start_x=lives_x, start_y=lives_y, font_size=30, color=arcade.color.WHITE, font_name="Kenney Pixel")

    def draw_points(self):
        """
        This function puts the current score on the screen
        Args:
            none
        """
        points_text = "Points: {}".format(self.ship.points)
        points_x = SCREEN_WIDTH - 170
        points_y = SCREEN_HEIGHT - 50
        arcade.draw_text(points_text, start_x=points_x, start_y=points_y, font_size=30, color=arcade.color.WHITE, font_name="Kenney Pixel")

    def draw_wave(self):
        """
        This function puts the current waves on the screen
        Args:
            none
        """
        draw_text = self.wave.name
        draw_x = SCREEN_WIDTH/2 - 70
        draw_y = SCREEN_HEIGHT - 50
        arcade.draw_text(draw_text, start_x=draw_x, start_y=draw_y, font_size=25, color=arcade.color.WHITE, font_name="Kenney Blocks")

    def game_over(self):
        """
        This function finish the game, with a message on the screen.
        Args:
            none
        """
        gameOver_text = "Game Over"
        gameOver_x = SCREEN_WIDTH/2 - 250
        gameOver_y = SCREEN_HEIGHT/2
        arcade.draw_text(gameOver_text, start_x=gameOver_x, start_y=gameOver_y, font_size=60, color=arcade.color.WHITE, font_name="Kenney Blocks")

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        Args:
            none
        """
        if arcade.key.LEFT in self.held_keys or arcade.key.A in self.held_keys:
            self.ship.goLeft()         

        if arcade.key.RIGHT in self.held_keys or arcade.key.D in self.held_keys:
            self.ship.goRight()
            
        if arcade.key.UP in self.held_keys or arcade.key.W in self.held_keys:
            self.ship.goForward()

        if arcade.key.DOWN in self.held_keys or arcade.key.S in self.held_keys:
            self.ship.goBack()

    
        


    def check_off_screen(self):
        """
        Checks to see if bullets or targets have left the screen
        and if so wraps them around
        Args: 
            none
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
        This function checks Collisions and then remove the dead objects
        Args:
            none
        """    
        for bullet in self.bullets:
            for enemy in self.enemies:

                if bullet.alive and enemy.alive:
                    too_close = bullet.radius + enemy.radius
                    # print(too_close)
                    if (abs(bullet.center.x - enemy.center.x) < too_close and abs(bullet.center.y - enemy.center.y) < too_close):
                        bullet.alive = False
                        enemy.split(self.experience)
                        
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
        print(f"Totals => B={len(self.bullets)} E={len(self.enemies)} Exp={len(self.experience)}")
        self.cleanup()

                
    def cleanup(self):
        """
        This function Clean up the bullet or targets.
        Args:
            none
        """
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
        """
        Create a new enemy
        Args:
            none
        """       
        for enemies in self.wave.currentWave:
            if enemies == "A":
                self.enemies.append(Enemy())
            elif enemies == "B":
                self.enemies.append(Enemy(type = 2))
            else:
                print(enemies)

    def check_wave_remainder(self):
        """
        This function check Wave remainder and create new enemy
        Args:
            none
        """
        if len(self.enemies) == 0:
            self.wave.nextWave(self.wave.next)
            self.create_enemy()     
    
           

    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        Args:
            key: key that is held.
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
        This function removes the current key from the set of held keys.
        Args:
            key: key that the user can held.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)