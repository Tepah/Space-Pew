"""Stores all the stats the game uses"""

import json

class GameStats:
    """Track statistics for Space Pew."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # High score should never be reset.
        self.high_score = 0
        self._get_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

        # Start Space pew in an inactive state
        self.game_active = False
        self.difficulty_menu = False

    def _get_high_score(self):
        try:
            with open('info.json') as f:
                self.high_score = json.load(f)
        except FileNotFoundError:
            with open('info.json', 'w') as f:
                json.dump(self.high_score, f)

    