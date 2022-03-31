# Space Invaders
Use your left and right arrow keey to move your spaceship! By pressing space bar, shoot the pullets and kill the space invaders!

## Getting Started
---
Make sure you have Python 3.8.0 and download packages to run this game
```
pip install -r requirements.txt
```
Arter finishing download requirements.txt, please go to __main__.py and hit 'run' icon

## Project Structure
---
The project files and folders are organized as follows:
```
SPACE-INVADERS  (project root folder)
+--classes              (source classes for game)
  +-- Bullete.py        (bullet for the game)
  +-- enemy.py          (create enemies)
  +-- experience.py     (green images after killing enemies)
  +-- game.py           (conductor of the game)
  +-- moving_actor.py   (parent class for the object)
  +-- point.py          (score for the player)
  +-- spaceship.py      (spaceship for the game)
  +-- velocity.py       (velocity of the game)
  +-- wave_handler.py   (wave handler for the game)
  +-- __main__.py         (main file to run the game)
+-- requirements.txt    (download requirements)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0
* Packages in the requirements.txt

## Authors
* Mallory Lee : Used maintainability on Enemy class by making setup functions. Created README file. Cleaned up the code.
* Cristian Fernandez : 
* Zachary Thompson :  Created all the classes, got it up and running, sourced all the sounds and  drew all the images (excluding the background image), created the wave system, created all of the constants. Created documentation for spaceship and wave_handler.
* Nathanael Budge : 
* Oliverio Forentino Cameron Muñoz : Clean the game.py and make docstrings for game.py
