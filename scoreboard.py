import pygame.font


class Scoreboard():
    def __init__(self, game_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.game_settings = game_settings
        self.stats = stats
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.bg_color = (0, 0, 0)
        self.prep_high_score()
        self.prep_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        score_str = "score is " + str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        high_score_str = "highest score is " + str(self.stats.score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_level(self):
        level_str = "level is " + str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.bg_color)
        self.level_rect = self.score_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        ships_str = "ships left " + str(self.stats.ships_left)
        self.ships_image = self.font.render(ships_str, True, self.text_color, self.bg_color)
        self.ships_rect = self.ships_image.get_rect()
        self.ships_rect.left = 10
        self.ships_rect.top = self.screen_rect.top

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.ships_image, self.ships_rect)
