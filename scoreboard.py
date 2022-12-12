import pygame.font
import time


class Scoreboard():
    """
        计分板
    """

    def __init__(self, game_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.game_settings = game_settings
        self.stats = stats
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.bullet_font = pygame.font.SysFont(None, 24)
        self.bg_color = (0, 0, 0)
        self.prep_high_score()
        self.prep_score()
        self.prep_level()
        self.prep_ships()
        self.prep_bullets()

    def prep_score(self):
        """
            修改信息
        """
        score_str = "score is " + str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """
            修改信息
        """
        high_score_str = self.stats.game_settings.difficulty + " mode highest score is " + str(self.stats.high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_level(self):
        """
            修改信息
        """
        level_str = "level is " + str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.bg_color)
        self.level_rect = self.score_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """
            修改信息
        """
        ships_str = "ships left " + str(self.stats.ships_left)
        self.ships_image = self.font.render(ships_str, True, self.text_color, self.bg_color)
        self.ships_rect = self.ships_image.get_rect()
        self.ships_rect.left = 10
        self.ships_rect.top = self.screen_rect.top

    def prep_bullets(self):
        """
            修改信息
        """
        ships_str = "wide " + str(self.game_settings.wide_bullet_remain) + " strong " + str(
            self.game_settings.strong_bullet_remain) + " unlimited time " + str(
            max(0, int(self.game_settings.bullet_unlimited_time - time.time())))
        self.bullets_image = self.bullet_font.render(ships_str, True, self.text_color, self.bg_color)
        self.bullets_rect = self.bullets_image.get_rect()
        self.bullets_rect.left = 10
        self.bullets_rect.bottom = self.screen_rect.bottom

    def show_score(self):
        """
            画图，展示信息
        """
        if self.stats.game_active:
            self.prep_bullets()
            self.screen.blit(self.score_image, self.score_rect)
            self.screen.blit(self.level_image, self.level_rect)
            self.screen.blit(self.ships_image, self.ships_rect)
            self.screen.blit(self.bullets_image, self.bullets_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
