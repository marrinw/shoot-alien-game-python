import pygame
from pygame.sprite import Sprite
import random
import time


class Alien(Sprite):
    def __init__(self, game_settings, screen, type=0):
        super(Alien, self).__init__()
        self.screen = screen
        self.game_settings = game_settings
        self.speed = game_settings.alien_speed
        self.drop_speed = game_settings.fleet_drop_speed
        self.type = type
        if (self.type == 2):
            self.image = pygame.image.load("./data/image/alien2.png")
        elif (self.type == 3):
            self.image = pygame.image.load("./data/image/alien3.png")
        elif (self.type == 4):
            self.image = pygame.image.load("./data/image/alien4.png")
        else:
            self.image = pygame.image.load("./data/image/alien1.png")
        self.image = pygame.transform.scale(self.image, (60, 80))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        return False

    def update(self):
        self.x += self.speed * self.game_settings.fleet_direction
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Alien_ship(Sprite):
    def __init__(self, game_settings, screen):
        super(Alien_ship, self).__init__()
        self.screen = screen
        self.game_settings = game_settings
        self.life = game_settings.alien_ship_life
        self.speed = self.game_settings.alien_ship_speed
        self.image = pygame.image.load("./data/image/alien_ship.png")
        self.image = pygame.transform.scale(self.image, (100, 120))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top
        self.centerx = float(self.rect.centerx)
        self.moving_direction = random.randint(-1, 1)
        self.changing_direction_time = game_settings.alien_ship_changing_direction_time
        self.last_changing_direction_time = time.time()

    def update(self):
        if time.time() - self.last_changing_direction_time >= self.changing_direction_time:
            self.moving_direction = random.randint(-1, 1)
            self.last_changing_direction_time = time.time()
        self.centerx += self.moving_direction * self.speed
        self.rect.centerx = self.centerx
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen_rect.right:
            self.rect.right = self.screen_rect.right
        self.centerx = float(self.rect.centerx)

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Boss_alien(Sprite):
    def __init__(self, game_settings, screen):
        super(Boss_alien, self).__init__()
        self.screen = screen
        self.game_settings = game_settings
        self.life = game_settings.boss_alien_life
        self.image = pygame.image.load("./data/image/boss_alien.jpg")
        self.image = pygame.transform.scale(self.image, (400, 360))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top

    def blitme(self):
        self.screen.blit(self.image, self.rect)
