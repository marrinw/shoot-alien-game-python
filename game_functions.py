import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from pygame.sprite import Group
from alien import Alien
from explosion import Explosion
from game_stats import Gamestats
from button import Button
from scoreboard import Scoreboard

from time import sleep


def ship_hit(game_settings, stats, screen, ship, aliens, bullets, scoreboard):
    stats.ships_left -= 1
    scoreboard.prep_ships()
    if pygame.mixer:
        game_settings.boom_sound.play()
    if stats.ships_left > 0:
        aliens.empty()
        bullets.empty()
        create_fleet(game_settings, screen, aliens, ship)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(False)


def get_number_aliens_x(game_settings, alien_width):
    available_space_x = game_settings.screen_width - 8 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(game_settings, ship_height, alien_height):
    available_space_y = (game_settings.screen_height - 3 * alien_height - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(game_settings, screen, aliens, alien_number, row_number):
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(game_settings, screen, aliens, ship):
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    number_aliens_x = get_number_aliens_x(game_settings, alien_width)
    alien_height = alien.rect.height
    number_rows = get_number_rows(game_settings, ship.rect.height, alien_height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(game_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(game_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(game_settings, aliens)
            break


def change_fleet_direction(game_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += game_settings.fleet_drop_speed
    game_settings.fleet_direction *= -1


def check_play_button(ship, bullets, game_settings, screen, aliens, stats, play_button, mouse_x, mouse_y, scoreboard):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        game_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        scoreboard.prep_score()
        scoreboard.prep_level()
        scoreboard.prep_high_score()

        aliens.empty()
        bullets.empty()

        create_fleet(game_settings, screen, aliens, ship)
        ship.center_ship()


def check_events(ship, bullets, game_settings, screen, aliens, stats, play_button, scoreboard):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ship, bullets, game_settings, screen, aliens, stats, play_button, mouse_x, mouse_y,
                              scoreboard)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                ship.moving_left = True
            if event.key == pygame.K_UP:
                ship.moving_up = True
            if event.key == pygame.K_DOWN:
                ship.moving_down = True
            if event.key == pygame.K_SPACE:
                if len(bullets) < game_settings.bullet_max:
                    new_bullet = Bullet(game_settings, screen, ship)
                    bullets.add(new_bullet)
                    if pygame.mixer:
                        game_settings.bullet_fire_sound.play()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False
            if event.key == pygame.K_UP:
                ship.moving_up = False
            if event.key == pygame.K_DOWN:
                ship.moving_down = False


def update_bullets(bullets, aliens, game_settings, screen, ship, explosions, stats, scoreboard):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collision(bullets, aliens, game_settings, screen, ship, explosions, stats, scoreboard)
    for explosion in explosions.sprites():
        explosion.update()


def check_bullet_alien_collision(bullets, aliens, game_settings, screen, ship, explosions, stats, scoreboard):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for boom in collisions:
            for alien in collisions[boom]:
                stats.score += game_settings.alien_points
                check_high_score(stats, scoreboard)
                scoreboard.prep_score()
                explosions.add(Explosion(alien))
                if pygame.mixer:
                    game_settings.boom_sound.play()
    if len(aliens) == 0:
        # bullets.empty()
        stats.level += 1
        scoreboard.prep_level()
        game_settings.increase_speed()
        create_fleet(game_settings, screen, aliens, ship)


def update_aliens(aliens, game_settings, ship, stats, screen, bullets, scoreboard):
    check_fleet_edges(game_settings, aliens)
    aliens.update()
    if (pygame.sprite.spritecollideany(ship, aliens)):
        ship_hit(game_settings, stats, screen, ship, aliens, bullets, scoreboard)
    check_aliens_bottom(aliens, game_settings, ship, stats, screen, bullets, scoreboard)


def check_aliens_bottom(aliens, game_settings, ship, stats, screen, bullets, scoreboard):
    screen_rect = screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(game_settings, stats, screen, ship, aliens, bullets, scoreboard)
            break


def update_screen(game_settings, screen, ship, bullets, aliens, explosions, stats, play_button, scoreboard):
    screen.blit(game_settings.backgroud, (0, 0))
    ship.blitme()
    explosions.draw(screen)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    aliens.draw(screen)
    scoreboard.show_score()

    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()


def check_high_score(stats, scoreboard):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        scoreboard.prep_high_score()
