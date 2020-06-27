"""Creates the wind class that makes things look fast"""

import pygame
from pygame.sprite import Sprite
from random import randint

class Wind(Sprite):
    """A class that manages the wind particles"""

    def __init__(self, sp_game):
        """Initialize the settings for wind"""
        super().__init__()
        self.screen = sp_game.screen
        self.color = (255, 255, 255)
        self.settings = sp_game.settings

        # Create a wind at 0, 0
        self.rect = pygame.Rect(0, 0, self.settings.wind_width,\
             self.settings.wind_height)
        self.rect.y = self.rect.y - self.settings.wind_height
        self._random_wind()

        self.y = float(self.rect.y)

    def update(self):
        """Moves all the wind down the screen"""
        self.y += self.settings.wind_speed
        self.rect.y = self.y

    def draw_wind(self):
        """Creates the wind!"""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def _random_wind(self):
        shift = randint(10, 200)
        if shift % 2 == 0:
            self.rect.x += shift
        else:
            self.rect.x = self.settings.screen_width - shift