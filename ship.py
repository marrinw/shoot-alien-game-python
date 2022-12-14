import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """
        玩家飞机
    """

    def __init__(self, screen, game_settings):
        super(Ship, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(game_settings.ship_img_path)
        self.image = pygame.transform.scale(self.image, (60, 80))
        self.rect = self.image.get_rect()
        self.moving_speed = game_settings.ship_moving_speed
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.centerx = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.bottom = float(self.screen_rect.bottom)
        self.life_max = game_settings.ship_life
        self.life = self.life_max
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 24)
        self.bg_color = (0, 0, 0)
        self.prep_life()

    def update(self):
        """
            更新移动位置
        """
        # 判断方位且不能出界，移动
        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.centerx += self.moving_speed
        if self.moving_left == True and self.rect.left > 0:
            self.centerx -= self.moving_speed
        if self.moving_up == True and self.rect.top > 0:
            self.bottom -= self.moving_speed
        if self.moving_down == True and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.moving_speed
        self.rect.centerx = self.centerx
        self.rect.bottom = self.bottom

    def center_ship(self):
        """
            飞机回到最下面中央
        """
        self.rect.centerx = self.screen_rect.centerx
        self.centerx = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """
            画图
        """
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.life_image, self.life_rect)

    def reset(self):
        """
            重置
        """
        self.center_ship()
        self.life = self.life_max
        self.prep_life()

    def prep_life(self):
        """
            显示生命值
        """
        high_score_str = "ship life remains " + str(self.life)
        self.life_image = self.font.render(high_score_str, True, self.text_color, self.bg_color)
        self.life_rect = self.life_image.get_rect()
        self.life_rect.right = self.screen_rect.right
        self.life_rect.bottom = self.screen_rect.bottom

    def change_img(self, img):
        """
            改变飞船图片
        """
        self.image = img
        self.image = self.image = pygame.transform.scale(self.image, (60, 80))
