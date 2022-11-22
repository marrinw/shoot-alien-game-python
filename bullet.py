import pygame
from pygame.sprite import Sprite
import math
import time


class Bullet(Sprite):
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
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Alien_bullet(Sprite):
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
        self.y += self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Boss_bullet(Sprite):
    def __init__(self, game_settings, screen, x, y, direction, grow_rate):
        super(Boss_bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, game_settings.alien_bullet_width, game_settings.alien_bullet_height)
        self.rect.centerx = x
        self.rect.centery = y
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.width = float(game_settings.alien_bullet_width)
        self.height = float(game_settings.alien_bullet_height)
        self.color = game_settings.alien_bullet_color
        self.speed = game_settings.boss_bullet_speed = 1
        self.direction = direction
        self.grow_time = game_settings.boss_bullet_grow_time
        self.grow_rate = grow_rate
        self.last_grow_time = time.time()

    def update(self):
        if time.time() - self.last_grow_time >= self.grow_time:
            self.width *= self.grow_rate
            self.height *= self.grow_rate
            self.rect.width = self.width
            self.rect.height = self.height
            self.last_grow_time = time.time()
        self.y += self.speed * math.sin(self.direction)
        self.x += self.speed * math.cos(self.direction)
        self.rect.y = self.y
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
