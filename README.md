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

PyGame Org: ![PyGame Org](https://www.pygame.org/)

PyGame Documentation: ![PyGame Doc](https://www.pygame.org/docs/)

2) sprite- This class belongs to PyGame and is used for grouping similar objects. There are several useful methods associated with this module such as Group(), spritecollideany(), groupcollide(), etc.

Sprite Documentation: ![Sprite Doc](http://www.pygame.org/docs/ref/sprite.html)

3) sys- This module is used for managing the system. For example, sys.exit() is used for closing the current application (program).

Sys Documentation: ![Sys Doc](https://docs.python.org/3/library/sys.html)

4) time- This module is used for pausing the game when the ship loses one lifeline. 'sleep()' accepts an argument in seconds to produce a delay.

Time Documentation: ![Time Doc](https://docs.python.org/3/library/time.html)
