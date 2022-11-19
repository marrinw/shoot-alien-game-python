import pygame
from pygame.sprite import Sprite


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
