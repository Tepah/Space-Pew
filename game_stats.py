class GameStats:
    """Track statistics for Space Pew."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit

        # Start Space pew in an inactive state
        self.game_active = False
        self.difficulty_menu = False
