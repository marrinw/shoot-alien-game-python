import pygame
from pygame.sprite import Sprite
import math
import time
import random


class Bullet(Sprite):
    """
        玩家子弹
    """

    def __init__(self, game_settings, screen, ship, is_wide_bullet=False, is_strong_bullet=False):
        super(Bullet, self).__init__()
        self.screen = screen
        self.is_wide_bullet = is_wide_bullet
        self.is_strong_bullet = is_strong_bullet
        if self.is_wide_bullet:
            self.rect = pygame.Rect(0, 0, game_settings.wide_bullet_width, game_settings.bullet_height)
        else:
            self.rect = pygame.Rect(0, 0, game_settings.bullet_width, game_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        if self.is_strong_bullet:
            self.color = game_settings.strong_bullet_color
        else:
            self.color = game_settings.bullet_color
        self.speed = game_settings.bullet_speed

    def update(self):
        """
            更新
        """
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """
            画图
        """
        pygame.draw.rect(self.screen, self.color, self.rect)


class Alien_bullet(Sprite):
    """
        外星人子弹
    """

    def __init__(self, game_settings, screen, alien):
        super(Alien_bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, game_settings.alien_bullet_width, game_settings.alien_bullet_height)
        self.rect.centerx = alien.rect.centerx
        self.rect.top = alien.rect.bottom
        self.y = float(self.rect.y)
        self.color = game_settings.alien_bullet_color
        self.speed = game_settings.alien_bullet_speed

    def update(self):
        """
            更新
        """
        # 移动
        self.y += self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """
            画图
        """
        pygame.draw.rect(self.screen, self.color, self.rect)


class Boss_bullet(Sprite):
    """
        外星boss子弹
    """

    def __init__(self, game_settings, screen, x, y, direction, grow_rate=1, rand_dir=False):
        super(Boss_bullet, self).__init__()
        self.screen = screen
        self.rand_dir = rand_dir
        self.rect = pygame.Rect(0, 0, game_settings.boss_bullet_size, game_settings.boss_bullet_size)
        self.rect.centerx = x
        self.rect.centery = y
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.size = float(game_settings.boss_bullet_size)
        self.color = game_settings.alien_bullet_color
        self.speed = game_settings.boss_bullet_speed = 1
        self.direction = direction
        self.grow_time = game_settings.boss_bullet_grow_time
        self.grow_rate = grow_rate
        self.size_max = game_settings.boss_bullet_size_max
        self.last_grow_time = time.time()
        self.last_direction_time = time.time()
        self.direction_time = game_settings.boss_bullet_direction_time

    def update(self):
        """
            更新
        """
        if time.time() - self.last_grow_time >= self.grow_time and self.size < self.size_max:
            # 变大
            self.size *= self.grow_rate
            self.rect.width = self.size
            self.rect.height = self.size
            self.last_grow_time = time.time()
        if self.rand_dir and time.time() - self.last_direction_time >= self.direction_time:  # 随机方向
            self.direction = random.uniform(0, 6.28)
            self.last_direction_time = time.time()
        # 移动
        self.y += self.speed * math.sin(self.direction)
        self.x += self.speed * math.cos(self.direction)
        self.rect.y = self.y
        self.rect.x = self.x

    def draw_bullet(self):
        """
            画图
        """
        pygame.draw.rect(self.screen, self.color, self.rect)
