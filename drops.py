"""The drops that the aliens give"""

import pygame
from pygame.sprite import Sprite

class Drops(Sprite):
    """A class that manages the drops/droprate for the aliens"""

    def __init__(self, sp_game, alien):
        """Initialize the base drops that the game gives."""
        super().__init__()
        self.screen = sp_game.screen
        self.settings = sp_game.settings

        # Creates a drop at 0, 0 and sets it to center of the alien
        self.rect = pygame.Rect(0, 0, self.settings.drop_size, \
            self.settings.drop_size)
        self.rect.center = alien.rect.center

        # Store the drop's position to a decimal for movement
        self.y = float(self.rect.y)

    def update(self):
        """Move the drops"""
        # Update the decimal position of the bullet.
        self.y += self.settings.drop_speed
        self.rect.y = self.y

    def draw_drop(self):
        """Make the drop appear"""
        pygame.draw.rect(self.screen, self.color, self.rect)
    
    def upgrade_drop(self):
        """Defines the upgrade drop"""
        self.color = self.settings.upgrade_drop_color
        self.type = 'upgrade'

    def pierce_drop(self):
        """Defines the upgrade drop"""
        self.color = self.settings.pierce_drop_color
        self.type = 'pierce'
