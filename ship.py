import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, screen, game_settings):
        super(Ship, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("./data/image/ship1.png")
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

    def update(self):
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
        self.rect.centerx = self.screen_rect.centerx
        self.centerx = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.bottom=self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)
