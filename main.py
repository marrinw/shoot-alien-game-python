import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from bullet import Alien_bullet
from pygame.sprite import Group
from alien import *
from explosion import Explosion
from game_stats import Gamestats
from button import Button
from scoreboard import Scoreboard
import time
from game_functions import *


def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("game")
    stats = Gamestats(game_settings)
    scoreboard = Scoreboard(game_settings, screen, stats)
    screen.blit(game_settings.backgroud, (0, 0))
    play_button = Button(game_settings, screen, "Play")
    ship = Ship(screen, game_settings)
    bullets = Group()
    aliens = Group()
    alien_ships = Group()
    explosions = Group()
    alien_bullets = Group()
    boss_aliens = Group()
    # create_fleet(game_settings, screen, aliens, ship)

    while True:
        check_events(ship, bullets, game_settings, screen, aliens, stats, play_button, scoreboard, alien_bullets,
                     alien_ships, boss_aliens)
        if stats.game_active:
            ship.update()
            update_aliens(aliens, game_settings, ship, stats, screen, bullets, scoreboard, alien_bullets, alien_ships,
                          boss_aliens)
            update_bullets(bullets, aliens, game_settings, screen, ship, explosions, stats, scoreboard, alien_bullets,
                           alien_ships, boss_aliens)

        update_screen(game_settings, screen, ship, bullets, aliens, explosions, stats, play_button, scoreboard,
                      alien_bullets, alien_ships, boss_aliens)


if __name__ == '__main__':
    run_game()
