import pygame
import time


class Settings():
    """
        游戏设置
    """

    def __init__(self):
        self.screen_height = 800
        self.screen_width = 1600
        self.background = pygame.image.load("./data/image/background.gif")
        self.background = pygame.transform.scale(self.background, (self.screen_width, self.screen_height))
        self.ship_moving_speed = 1.5
        self.ships_limit = 3  # 一共有多少玩家飞船
        self.ship_life = 5  # 每个玩家飞船的生命
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = "yellow"
        self.strong_bullet_color = "red"
        self.bullet_unlimited_time = time.time()
        self.bullet_max = 3
        self.wide_bullet_width = 300
        self.wide_bullet_remain = 0
        self.strong_bullet_remain = 0
        self.alien_reward = [0, 0, {"wide_bullet_num": 1}, {"strong_bullet_num": 2}, {"unlimited_bullet_time": 3}]
        self.alien_ship_reward = {"wide_bullet_num": 0, "strong_bullet_num": 0, "ship_life_increase": 2}
        self.boss_alien_reward = {"wide_bullet_num": 1, "strong_bullet_num": 1, "ship_life_max": True}
        self.alien_bullet_speed = 0.4
        self.alien_bullet_width = 3
        self.alien_bullet_height = 15
        self.alien_bullet_color = "green"
        self.alien_fire_bullet_random = 400
        self.alien_ships_fire_bullet_random = 600
        if (pygame.mixer):
            self.bullet_fire_sound = pygame.mixer.Sound("./data/sound/bullet_fire.wav")
            self.boom_sound = pygame.mixer.Sound("./data/sound/boom.wav")
            self.alien_bullet_fire_sound = pygame.mixer.Sound("./data/sound/alien_bullet_fire.mp3")
        self.alien_speed = 1
        self.fleet_drop_speed = 15
        self.fleet_direction = 1  # 1右
        self.speedup_scale = 1.02
        self.alien_points = 50
        self.points_scale = 1.5
        self.alien_types = 4
        self.alien_type_rate = 30
        self.alien_ship_life = 3
        self.alien_ship_speed = 0.2
        self.alien_ship_max = 2
        self.alien_ship_changing_direction_time = 1
        self.alien_ship_points = 100
        self.boss_alien_life = 10
        self.is_boss_alien = False
        self.boss_alien_appearance_round = 2
        self.boss_alien_points = 500
        self.boss_bullet_max = 30
        self.boss_bullet_min = 10
        self.boss_bullet_speed = 1
        self.boss_bullet_grow_time = 0.5
        self.boss_bullet_grow_rate_max = 1.2
        self.boss_bullet_size = 10
        self.boss_bullet_size_max = 30
        self.initialize_dynamic_settings()

    def increase_speed(self):
        self.ship_moving_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_bullet_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.points_scale)
        self.alien_ship_life += 1
        self.alien_ship_speed *= self.speedup_scale
        self.alien_ship_points = int(self.alien_ship_points * self.speedup_scale)
        self.boss_alien_life += 2
        self.boss_alien_points = int(self.boss_alien_points * self.speedup_scale)
        self.boss_bullet_max += 10
        self.boss_bullet_min += 5

    def initialize_dynamic_settings(self):
        self.alien_speed = 1
        self.alien_ship_speed = 0.2
        self.alien_bullet_speed = 0.4
        self.bullet_speed = 3
        self.ship_moving_speed = 1.5
        self.boss_alien_points = 500
        self.alien_points = 50
        self.alien_ship_points = 100
        self.boss_alien_life = 10
        self.alien_ship_life = 3
        self.ship_life = 5
        self.boss_bullet_max = 30
        self.boss_bullet_min = 10
