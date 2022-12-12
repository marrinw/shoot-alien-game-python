import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import *
from pygame.sprite import Group
from alien import *
from explosion import Explosion
from game_stats import Gamestats
from button import *
from scoreboard import Scoreboard
import time
import os
from game_functions import *


def run_game():
    # 初始化
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))  # 屏幕大小
    pygame.display.set_caption("shoot alien game")  # 游戏名
    if os.path.exists("./icon.ico"):  # 游戏图标
        icon = pygame.image.load("./icon.ico")
        pygame.display.set_icon(icon)
    stats = Gamestats(game_settings)
    scoreboard = Scoreboard(game_settings, screen, stats)
    screen.blit(game_settings.background, (0, 0))
    play_button = Button_play(game_settings, screen, "Play")
    reset_button = Button_reset(game_settings, screen, "reset score")
    difficulty_button = Button_difficulty(game_settings, screen, "Change Difficulity")
    ship = Ship(screen, game_settings)
    bullets = Group()
    aliens = Group()
    alien_ships = Group()
    explosions = Group()
    alien_bullets = Group()
    boss_aliens = Group()
    boss_bullets = Group()
    # create_fleet(game_settings, screen, aliens, ship)

    while True:  # 游戏开始，不断循环判断
        check_events(ship, bullets, game_settings, screen, aliens, stats, play_button, scoreboard, alien_bullets,
                     alien_ships, boss_aliens, boss_bullets, explosions, reset_button, difficulty_button)  # 判断玩家操作
        if stats.game_active:  # 游戏进行中
            # 游戏数据信息更新
            ship.update()
            update_aliens(aliens, game_settings, ship, stats, screen, bullets, scoreboard, alien_bullets, alien_ships,
                          boss_aliens, boss_bullets, explosions)
            update_bullets(bullets, aliens, game_settings, screen, ship, explosions, stats, scoreboard, alien_bullets,
                           alien_ships, boss_aliens, boss_bullets)

        # 屏幕显示更新
        update_screen(game_settings, screen, ship, bullets, aliens, explosions, stats, play_button, scoreboard,
                      alien_bullets, alien_ships, boss_aliens, boss_bullets, reset_button, difficulty_button)


if __name__ == '__main__':
    run_game()
