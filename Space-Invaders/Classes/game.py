from constants import *
from Classes.spaceship import SpaceShip
from Classes.enemy import Enemy
from Classes.wave_handler import WaveHandler
from Classes.enemy2 import Enemy2
from Classes.bullet import Bullet


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
        self.background = arcade.load_texture("images/background.jpg")

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
        """

        # clear the screen to begin drawing
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
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
        self.draw_wave()

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
        self.check_wave_remainder()
        
        
        
        # TODO: Tell everything to advance or move forward one step in time
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

    def draw_wave(self):
        draw_text = self.wave.name
        draw_x = SCREEN_WIDTH/2 - 50
        draw_y = SCREEN_HEIGHT - 90
        arcade.draw_text(draw_text, start_x=draw_x, start_y=draw_y, font_size=20, color=arcade.color.WHITE)

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
       
        for enemies in self.wave.currentWave:
            if enemies == "A":
                enemy = Enemy()
                self.enemies.append(enemy)
            elif enemies == "B":
                enemy = Enemy2()
                self.enemies.append(enemy)
            else:
                print(enemies)

    def check_wave_remainder(self):

        if len(self.enemies) == 0:
            self.wave.nextWave(self.wave.next)
            self.create_enemy()     
    
        

       
        
        

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