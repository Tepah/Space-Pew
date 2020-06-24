class Settings:
    """Class storing all settings for AI"""

    def __init__(self):
        """Initializing the game settings"""
        # Screen settings:
        self.screen_width = 600
        self.screen_height = 1000
        self.bg_color = (177, 155, 217)

        # Ship settings:
        self.ship_speed = .75
        self.ship_limit = 3
        self.spawn_ship = True

        # Bullet settings:
        self.bullet_speed = 1
        self.bullet_width = 4
        self.bullet_height = 20
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 7
        self.god_bullet_on = False

        # Alien settings:
        self.alien_speed = .2
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

    def god_bullet(self):
        """Changes bullets to GOD BULLETS"""
        self.bullet_speed = 5
        self.bullet_width = 40
        self.bullet_height = 100
        self.god_bullet_on = True

    
    