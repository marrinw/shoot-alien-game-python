import os
import configparser


class Gamestats():
    """
        游戏统计
    """

    def __init__(self, game_settings):
        self.game_settings = game_settings
        self.reset_stats()
        self.game_active = False
        self.score = 0
        self.highest_score = {"Easy": 0, "Normal": 0, "Hard": 0}
        self.high_score = self.highest_score[self.game_settings.difficulty]
        self.level = 1
        if os.path.exists(self.game_settings.highest_score_path):  # 读取highest score
            config = configparser.ConfigParser()
            config.read(self.game_settings.highest_score_path)
            for key in self.highest_score:
                self.highest_score[key] = int(config[key]['highest_score'])
        self.high_score = self.highest_score[self.game_settings.difficulty]

    def reset_stats(self):
        """
            重置统计信息
        """
        self.ships_left = self.game_settings.ships_limit
        self.score = 0
        self.level = 1

    def stats_difficulity_score(self):
        """
            根据难度修改最高分
        """
        self.high_score = self.highest_score[self.game_settings.difficulty]
