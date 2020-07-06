"""Ship Class"""
import pygame
from pygame.sprite import Sprite

from setup import resource_path

class Ship(Sprite):
    """The ship that the player controls"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the ship image and get its rect.
        asset_url = resource_path('images/ship.bmp')
        self.image = pygame.image.load(asset_url)
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        self.spawn_position = self.rect.y - self.rect.height
        self.rect.y += self.rect.height * 2

        # Store a decimal value for the ship's horizontal positon.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
        # Determines if the ship is shooting
        self.is_shooting = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < \
        self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < \
        self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def ship_spawn(self):
        """Spawns the ship and moves it to center"""
        # Centers the ship on the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y += self.rect.height * 2

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.settings.ship_speed /= 2
        self.moving_up = True
        while self.rect.y != self.spawn_position:
            self.update()
        self.moving_up = False
        self.settings.ship_speed *= 2

    def upgrade_bullet(self):
        """Make a small incremental upgrade to bullets"""
        self.settings.bullet_damage *= 1.1

    def upgrade_pierece(self):
        """Increases pierce mechanic"""
        self.settings.bullet_pierce += 1