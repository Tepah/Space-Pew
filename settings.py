class Settings:
    """Class storing all settings for AI"""

    def __init__(self):
        """Initializing the game settings"""
        # Screen settings:
        self.screen_width = 600
        self.screen_height = 1000
        self.bg_color = (177, 155, 217)

        # Ship settings:
        self.ship_speed = .5

        # Bullet settings:
        self.bullet_speed = .8
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 7

        # Alien settings:
        self.alien_speed = .2
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

    
    