import sys
from time import sleep
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        pygame.mixer.init()
        self.settings = Settings()

        #  The argument (1200, 600) is a tuple that defines the dimensions of
        #  the game window. width = 1200, height = 600
        # The object we assigned to self.screen is called a surface.
        # self.screen = pygame.display.set_mode((
        #     self.settings.screen_width,
        #     self.settings.screen_height))
        # Below code for full screen mode
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        # Set the background color.
        self.bg_color = self.settings.bg_color
        # Create an instance to store game statistics.
        # and create a scoreboard.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        # Make a ship instance
        self.ship = Ship(self)
        # Create a group of bullets
        self.bullets = pygame.sprite.Group()
        # Create a group of aliens
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        # Make the Play button
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        # Decrement ships_left.
        if self.stats.ships_left > 0:
            # Decrement ships_left, and update scoreboard.
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Play sound
            explosion_sound = pygame.mixer.Sound("sound/explosion.wav")
            pygame.mixer.Sound.play(explosion_sound)

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
            break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        """Check if the fleet is at an edge,
            then update the positions of all aliens in the fleet.
        """
        self._check_fleet_edges()
        self.aliens.update()
        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Make an alien.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        # Horizontal space availability
        available_space_x = self.settings.screen_width - (2 * alien_width)
        # // -> Floor division
        number_aliens_x = available_space_x // (2 * alien_width)
        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        # Vertical space availability
        available_space_y = (self.settings.screen_height
                             - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create the full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        # we use the attribute size, which contains a tuple with the width and
        # height of a rect object.
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()
        # Get rid of bullets that have disappeared.
        # The bullets actually continue to exist; their y-coordinate values
        # just grow increasingly negative. This is a problem, because they
        # continue to consume memory and processing power.
        # Because we can’t remove items from a list or group within a for
        # loop, we have to loop over a copy of the group.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))
        # Check for any bullets that have hit aliens.
        # If so, get rid of the bullet and the alien.
        # First True is for bullets
        # Second True is for alien
        # The two True arguments tell Pygame to delete the bullets and aliens
        # that have collided. (To make a high-powered bullet that can travel
        # to the top of the screen, destroying every alien in its path, you
        # could set the first Boolean argument to False and keep the second
        # Boolean argument set to True. The aliens hit would disappear, but
        # all bullets would stay active until they disappeared off the top of
        # the screen.)
        collisions = pygame.sprite.groupcollide(self.bullets,
                                                self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()

    def _check_events(self):
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # KEYDOWN means one by one position change
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                # KEYUP means change of position until release of key
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset the game settings.
            self.settings.initialize_dynamic_settings()
            # Reset the game statistics.
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()
            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()
            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right.
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.bg_color)
        # Set a ship on screen
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        # Draw the score information.
        self.sb.show_score()
        # Draw the play button if the game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()
        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()