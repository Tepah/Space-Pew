"""A minimalistic bullet hell"""

# TODO: Add a limiting FPS
import sys
from time import sleep

import pygame
from random import randint

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from wind import Wind
from drops import Drops

class SpacePew:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Space Pew")

        # Create an instance to store game stats and create a scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.wind = pygame.sprite.Group()
        self.drops = pygame.sprite.Group()

        # Make the Play button.
        self.play_button = Button(self, "Play")

        # Make the Normal and Hard Difficulty buttons.
        self.normal_button = Button(self, "Peewee")
        self.hard_button = Button(self, "REAL PP")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._fire_bullet()
                if self.bullets:
                    self._update_bullets()
                if self.drops:
                    self._update_drops()
                self._update_aliens()
                if self.settings.spawn_ship:
                    self.ship.ship_spawn()
                    self.settings.spawn_ship = False

            self._blow_wind()
            self._update_wind()
            self._update_screen()
    
    def _check_events(self):
        """Responds to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if not self.stats.game_active \
                    and not self.stats.difficulty_menu:
                    self._check_play_button(mouse_pos)
                elif self.stats.difficulty_menu:
                    self._check_difficulty_menu(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when a player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked:
            # Shows the difficulty buttons
            self.stats.difficulty_menu = True
            
    def _check_difficulty_menu(self, mouse_pos):
        if self.normal_button.rect.collidepoint(mouse_pos):
            # Reset the game settings.
            self.settings.initialize_dynamic_settings()
            self._start_game()
            self.stats.difficulty_menu = False
        elif self.hard_button.rect.collidepoint(mouse_pos):
            # Starts game in HARD MODE
            self.settings.initialize_dynamic_settings()
            self.settings.hard_mode_settings()
            self._start_game()
            self.stats.difficulty_menu = False

    def _start_game(self):
        # Reset the game statistics.
        self.stats.reset_stats()
        self.stats.game_active = True

        # Get rid of any remaining aliens and bullets.
        self.aliens.empty()
        self.bullets.empty()

        # Create a new flseet and center the ship.
        self._create_fleet()
        self.ship.ship_spawn()
        
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Responds to keypresses"""
        if event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_w:
            self.ship.moving_up = True
        elif event.key == pygame.K_s:
            self.ship.moving_down = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_k:
            self._continue_shooting()
        elif event.key == pygame.K_EQUALS:
            self.settings.switch_god_bullet()
        elif event.key == pygame.K_p:
            if not self.stats.game_active:
                self._start_game()
        
    def _continue_shooting(self):
        if not self.ship.is_shooting:
            self.ship.is_shooting = True
        else:
            self.ship.is_shooting = False
        
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed and \
            self.ship.is_shooting and self.settings.bullet_counter % 100 == 0:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
        self.settings.bullet_counter += 1

    def _blow_wind(self):
        if len(self.wind) < self.settings.wind_limit and \
            self.settings.wind_counter % 300 == 0:
            new_wind = Wind(self)
            self.wind.add(new_wind)
        self.settings.wind_counter += 1

    def _check_keyup_events(self, event):
        """Responds to Key releasing"""
        if event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_a:
            self.ship.moving_left = False
        elif event.key == pygame.K_w:
            self.ship.moving_up = False
        elif event.key == pygame.K_s:
            self.ship.moving_down = False

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _update_drops(self):
        """Update the position of the drops and get rid of old drops"""
        # update drop position
        self.drops.update()

        # Get rid of drops that are gone
        for drop in self.drops.copy():
            if drop.rect.top >= self.settings.screen_height:
                self.drops.remove(drop)

    def _check_bullet_alien_collisions(self):
        # Check for any bullets that have hit aliens.
        # If so, get rid of the bullet and the alien.
        collisions = pygame.sprite.groupcollide(\
            self.bullets, self.aliens, (self.settings.god_switch == -1), \
                True)
        drop_determine = randint(1, 100)

        if collisions:
            for aliens in collisions.values():
                if drop_determine <= 5:
                    for alien in aliens:
                        new_drop = Drops(self, alien)
                        new_drop.upgrade_drop()
                        self.drops.add(new_drop)
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        
        # Checks if aliens are all dead
        if not self.aliens:
            # Destroy existing bullets and create a new fleet.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()

    def _update_aliens(self):
        """Check if the fleet is at the edge, then
        Update the position of the aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen.
        self._check_alien_bottom()
    
    def _update_wind(self):
        """Update the position of the wind particles and gets rid of them"""
        self.wind.update()

        # Get rid of the wind that disappear
        for air in self.wind.copy():
            if air.rect.top > self.settings.screen_height:
                self.wind.remove(air)

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""

        if self.stats.ships_left > 0:
            # Decrement ships_left
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()

            # Pause.
            sleep(0.5)
            self.settings.spawn_ship = True
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _create_fleet(self):
        """Create a fleet of aliens"""
        # Make an Alien.
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - \
            (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - \
            (3 * alien_height) - ship_height)
        number_rows = available_space_y // (3 * alien_height)

        # Create the full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height \
            * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _check_alien_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom > screen_rect.bottom:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Update images on screen and flips to new screen"""
        self.screen.fill(self.settings.bg_color)
        for air in self.wind.sprites():
            air.draw_wind()
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for drop in self.drops.sprites():
            drop.draw_drop()
        self.aliens.draw(self.screen)

        # Draw the score information.
        self.sb.show_score()

        # Draw the play button if the game is inactive.
        if not self.stats.game_active and not self.stats.difficulty_menu:
            self.play_button.draw_play_button()
        elif self.stats.difficulty_menu and not self.stats.game_active:
            # Draws the difficulty buttons
            self.normal_button.draw_button(0, -60)
            self.hard_button.draw_button(0, 60)

        pygame.display.flip()

if __name__ == "__main__":
    # Make a game instance, and run the game.
    sp = SpacePew()
    sp.run_game()

