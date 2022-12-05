class Gamestats():
    """
        游戏统计
    """

    def __init__(self, game_settings):
        self.game_settings = game_settings
        self.reset_stats()
        self.game_active = False
        self.score = 0
        self.high_score = 0
        self.level = 1

    def reset_stats(self):
        """
            重置统计信息
        """
        self.ships_left = self.game_settings.ships_limit
        self.score = 0
        self.level = 1
