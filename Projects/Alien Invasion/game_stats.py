class GameStats:
    """
    Track statistics for Alien Invasion.
    """

    def __init__(self, game):
        """
        Initializes statistics.
        :param game:
        """
        self.settings = game.settings
        self.reset_stats()

        # Start Alien Invasion in an active state.
        self.game_active = True

        # High score should never be reset
        self.high_score = 0

    def reset_stats(self):
        """
        Initializes statistics that can change during the game.
        :return:
        """
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
