"""Module containing the Button class"""

import pygame.font

class Button:
    """Creates a button"""

    def __init__(self, sp_game, msg):
        """Initialize button attributes."""
        self.screen = sp_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 150, 50
        self.button_color = (233, 206, 245)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the botton"""
        self.msg_image = self.font.render(msg, True, self.text_color, \
            self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_play_button(self):
        """Draw blank button and then draw message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
    
    def draw_button(self, x, y):
        """Draws blank button and message"""
        if self.rect.center == self.screen_rect.center: 
            self.rect.x += x
            self.rect.y += y
            self.msg_image_rect.x += x
            self.msg_image_rect.y += y
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
