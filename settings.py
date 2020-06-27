"""Setting class to store settings."""

class Settings:
    """Class storing all settings for SP"""

    def __init__(self):
        """Initializing the game's static settings"""
        # Screen settings:
        self.screen_width = 600
        self.screen_height = 1000
        self.bg_color = (177, 155, 217)

        # Ship settings:
        self.ship_limit = 2
        self.spawn_ship = True

        # Bullet settings:
        self.default_bullet()

        # Alien settings:
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.5
        
        # Wind settings
        self.wind_height, self.wind_width = 80, 1
        self.wind_speed = 1
        self.wind_limit = 5
        self.wind_counter = 0

        self.initialize_dynamic_settings()

    def switch_god_bullet(self):
        if self.god_switch is -1:
            self.god_bullet()
        elif self.god_switch is 1:
            self.default_bullet()
            self.god_switch *= -1

# Different Bullet Types
    def default_bullet(self):
        """Changes bullets to default bullets"""
        self.bullet_width = 5
        self.bullet_height = 35
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 5
        self.bullet_counter = 0
        self.bullet_damage = 10
        self.god_switch = -1

    def god_bullet(self):
        """Changes bullets to GOD BULLETS"""
        self.bullet_speed = 5
        self.bullet_width = 40
        self.bullet_height = 100
        self.bullet_damage = 99999
        self.god_switch *= -1

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = .75
        self.bullet_speed = 1
        self.alien_speed = .2

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def hard_mode_settings(self):
        """Change values to represent a harder mode."""
        self.alien_speed *= 2
        self.speedup_scale = 1.3
        self.score_scale = 1.7

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)