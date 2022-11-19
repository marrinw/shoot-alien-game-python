import pygame
import time


class Settings():
    def __init__(self):
        self.screen_height = 800
        self.screen_width = 1600
        self.backgroud = pygame.image.load("./data/image/background.JPG")
        self.backgroud = pygame.transform.scale(self.backgroud, (self.screen_width, self.screen_height))
        self.ship_moving_speed = 1.5
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = "yellow"
        self.strong_bullet_color = "red"
        self.bullet_unlimit_time = time.time()
        self.bullet_max = 3
        self.wide_bullet_width = 300
        self.wide_bullet_remain = 0
        self.strong_bullet_remain = 0
        self.alien_reward = [0, 0, {"wide_bullet_num": 2}, {"strong_bullet_num": 2}, {"unlimited_bullet_time": 3}]
        self.alien_bullet_speed = 0.3
        self.alien_bullet_width = 3
        self.alien_bullet_height = 15
        self.alien_bullet_color = "green"
        self.alien_fire_bullet_random = 200
        if (pygame.mixer):
            self.bullet_fire_sound = pygame.mixer.Sound("./data/sound/bullet_fire.wav")
            self.boom_sound = pygame.mixer.Sound("./data/sound/boom.wav")
            self.alien_bullet_fire_sound = pygame.mixer.Sound("./data/sound/alien_bullet_fire.mp3")
        self.alien_speed = 1
        self.fleet_drop_speed = 15
        self.fleet_direction = 1  # 1右
        self.ships_limit = 3
        self.speedup_scale = 1.1
        self.alien_points = 50
        self.points_scale = 1.5
        self.alien_types = 4
        self.alien_type_rate = 30
        self.initialize_dynamic_settings()

    def increase_speed(self):
        self.ship_moving_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.points_scale)

    def initialize_dynamic_settings(self):
        self.alien_speed = 1
        self.bullet_speed = 3
        self.ship_moving_speed = 1.5
