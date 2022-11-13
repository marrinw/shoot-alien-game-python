import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from pygame.sprite import Group
from alien import Alien
from explosion import Explosion
from game_stats import Gamestats
from button import Button
from scoreboard import Scoreboard
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
    explosions = Group()
    create_fleet(game_settings, screen, aliens, ship)

    while True:
        check_events(ship, bullets, game_settings, screen, aliens, stats, play_button, scoreboard)
        if stats.game_active:
            ship.update()
            update_bullets(bullets, aliens, game_settings, screen, ship, explosions, stats, scoreboard)
            update_aliens(aliens, game_settings, ship, stats, screen, bullets, scoreboard)
        # print(len(aliens),aliens.sprites()[0].rect.y,aliens.sprites()[0].rect.x,aliens.sprites()[0].speed)
        update_screen(game_settings, screen, ship, bullets, aliens, explosions, stats, play_button, scoreboard)


if __name__ == '__main__':
    run_game()
