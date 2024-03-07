

class GameStats():
    """Track statistics for Alien Invasation."""
    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """initialize statistics that can change during the game."""    
        self.ship_left = self.settings.ship_limit
        self.score = 0

      

