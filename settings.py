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
        self.ship_speed = .6
        self.ship_limit = 2
        self.spawn_ship = True

        # Bullet settings:
        self.default_bullet()

        # Alien settings:
        self.fleet_drop_speed = 10
        self.alien_bullet_size = 15
        self.alien_projectile_counter = 1

        # Drop settings:
        self.drop_size = 30
        self.drop_speed = .2
        self.upgrade_drop_color = (148, 223, 255)
        self.pierce_drop_color = (66, 245, 114)

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.difficulty_scale = 1.2
        self.alien_health_spike = 1.2

        # How quickly the alien point values increase
        self.score_scale = 1.5
        
        # Wind settings
        self.wind_height, self.wind_width = 80, 1
        self.wind_limit = 5
        self.wind_counter = 0

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.bullet_speed = .8
        self.wind_speed = .8

        # Alien dynamic variables
        self.alien_speed = .2
        self.alien_health = 20
        self.alien_projectile_speed = .5
        self.alien_projectile_limit = 3
        self.alien_projectile_shoot = 500

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def switch_god_bullet(self):
        if self.god_switch == -1:
            self.god_bullet()
        elif self.god_switch == 1:
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
        self.bullet_pierce = 0
        self.bullet_level = 1
        self.god_switch = -1

    def god_bullet(self):
        """Changes bullets to GOD BULLETS"""
        self.bullet_speed = 5
        self.bullet_width = 40
        self.bullet_height = 100
        self.bullet_damage = 99999
        self.bullet_pierce = 20
        self.god_switch *= -1

    def hard_mode_settings(self):
        """Change values to represent a harder mode."""
        self.alien_speed *= 2
        self.speedup_scale = 1.1
        self.score_scale = 1.7
        self.alien_projectile_limit += 1
        self.alien_projectile_speed *= 1.5

    def increase_difficulty(self, level):
        """Increase speed settings."""
        self.alien_speed *= self.speedup_scale
        self.alien_projectile_speed *= self.speedup_scale

        self.wind_speed *= self.speedup_scale
        if level % 2 == 0:
            self.alien_projectile_limit += 1
        self.alien_projectile_shoot -= round(self.alien_projectile_shoot * .1)

        self.alien_points = int(self.alien_points * self.score_scale)