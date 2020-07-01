"""Creates the bullets that the aliens shoot"""

import pygame
from pygame.sprite import Sprite

class AlienProjectile(Sprite):
    """A class to manage bullets fired by aliens"""

    def __init__(self, sp_game, alien):
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
        self.rect.midbottom = alien.rect.midbottom

        # Store the bullet's position as a decimal
        self.y = float(self.rect.y)

    def update(self):
        """Moves projectiles down the screen"""
        # Updates the decimal position of the projectile.
        self.y += self.settings.alien_projectile_speed
        # Update the rect position
        self.rect.y = self.y
    
    def draw_projectile(self):
        """Draw the projectile to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)