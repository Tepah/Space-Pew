"""Creates the bullets that the aliens shoot"""

import pygame
from pygame.sprite import Sprite

class AlienProjectile(Sprite):
    """A class to manage bullets fired by aliens"""

    def __init__(self, sp_game):
        """Create a AlienProjectile obj at the ship's location."""
        super().__init__()
        self.screen = sp_game.screen
        self.settings = sp_game.settings
        self.color = self.settings.bullet_color

        # Creates the rect at (0, 0) and then sets the 
        # position to the alien
        self.rect = pygame.Rect (0, 0, \
            self.settings.alien_bullet_size, \
            self.settings.alien_bullet_size)
        self.rect.midbottom = sp_game.alien.midbottom

        # Store the bullet's position as a decimal
        self.y = float(self.rect.y)