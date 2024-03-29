"""The bullets that the player shoots"""

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, sp_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = sp_game.screen
        self.settings = sp_game.settings
        self.color = self.settings.bullet_color

        # Sets the piercing values
        self.pierce = sp_game.settings.bullet_pierce
        self.prev_alien = None

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, \
            self.settings.bullet_height)
        self.rect.midtop = sp_game.ship.rect.midtop

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def set_pierced_alien(self, alien):
        """Sets an alien that was hit"""
        self.prev_alien = alien

    
