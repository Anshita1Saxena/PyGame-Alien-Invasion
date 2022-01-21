# PyGame-Alien-Invasion

The credit for this project goes to "Python Crash Course" by "Eric Matthes". I would like to pay my kind regards to this book for enhancing and adding a new skill in me for designing and developing games using a wonderful library: **PyGame**. As written in the book about pygame.mixer module, I have added the sound to the game where the alien fleet hit the ship and one lifeline is gone.

![Alien Invasion Game Screenshot](https://github.com/Anshita1Saxena/PyGame-Alien-Invasion/blob/main/images/alien_invasion_game.png)
Alien Invasion is a classic game where aliens move on the screen from left to right and our mission is to fire bullets from the ship and kill all the aliens who approach the ship.

## Description

**Alien Invasion Game is based on the eight modules:**

1) Aliens (alien.py)
2) Bullets (bullet.py)
3) Button (button.py)
4) Game Statistics (game_stats.py)
5) Scoreboard (scoreboard.py)
6) Ship (ship.py)
7) Settings (settings.py)
8) Main Alien Invasion Game File (alien_invasion_settings.py)

**Special libraries/modules/functions:**

1) pygame- This module is used for developing the games in Python. Methods used include image.load(), font.SysFont(), display.flip(), etc.

PyGame Org: [PyGame Org](https://www.pygame.org/)

PyGame Documentation: [PyGame Doc](https://www.pygame.org/docs/)

2) sprite- This class belongs to PyGame and is used for grouping similar objects. There are several useful methods associated with this module such as Group(), spritecollideany(), groupcollide(), etc.

Sprite Documentation: [Sprite Doc](http://www.pygame.org/docs/ref/sprite.html)

3) sys- This module is used for managing the system. For example, sys.exit() is used for closing the current application (program).

Sys Documentation: [Sys Doc](https://docs.python.org/3/library/sys.html)

4) time- This module is used for pausing the game when the ship loses one lifeline. 'sleep()' accepts an argument in seconds to produce a delay.

Time Documentation: [Time Doc](https://docs.python.org/3/library/time.html)

## Environment Details

This project is developed and run on the following platform:

1. Language:- Python 3.9.9
2. Operating System:- Windows 10
3. Libraries:- PyGame 2.1.2
4. IDE:- PyCharm

This project uses an object-oriented approach and supports moving the object left, right, and up directions along with the sound effect of an explosion at the time of collision of aliens to the ship. The sound effect is the enhancement done on the original project. Appreciate Eric Matthes for recording this notion in his book for future enhancements on the project.

## Working Details

This code can be pulled using version control and imported in an IDE or can be run independently in any machine having Python 3.X. To play this game, use the following command to run or run the `alien_invasion_settings.py` code via IDE:

`python3 alien_invasion_settings.py`

To run this program for an indefinite time, you can use `nohup` command:

`nohup python3 alien_invasion_settings.py &`

After the game (application) is up and running, press the `Play` button to start playing the game. 

Happy Playing!
