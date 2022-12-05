import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import *
from pygame.sprite import Group
from alien import *
from explosion import Explosion
from game_stats import Gamestats
from button import Button
from scoreboard import Scoreboard
import random
import time


def create_alien(game_settings, screen, aliens, alien_number, row_number, alien_type):
    """
        创造单个普通外星人，通过位置
    """
    alien = Alien(game_settings, screen, alien_type)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_aliens_x(game_settings, alien_width):
    """
        计算一行有多少外星人
    """
    available_space_x = game_settings.screen_width - 8 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(game_settings, ship_height, alien_height):
    """
        计算一共有多少行外星人
    """
    available_space_y = (game_settings.screen_height - 3 * alien_height - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_fleet(game_settings, screen, aliens, ship, alien_ships):
    """
        创造一个外星舰队（一群外星人）
    """
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    number_aliens_x = get_number_aliens_x(game_settings, alien_width)
    alien_height = alien.rect.height
    number_rows = get_number_rows(game_settings, ship.rect.height, alien_height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            alien_type = random.randint(1, game_settings.alien_type_rate)  # 设置普通外星人的类型（有特殊奖励）
            if (alien_type > game_settings.alien_types):
                alien_type = 1
            create_alien(game_settings, screen, aliens, alien_number, row_number, alien_type)
    create_alien_ships(game_settings, screen, alien_ships)


def create_boss_alien(game_settings, screen, alien_ships, boss_aliens):
    """
        创造单个boss外星人
    """
    boss_aliens.add(Boss_alien(game_settings, screen))
    create_alien_ships(game_settings, screen, alien_ships)


def create_alien_ships(game_settings, screen, alien_ships):
    """
        创造外星飞机
    """
    alien_ship_numbers = random.randint(0, game_settings.alien_ship_max)
    for alien_ship_number in range(alien_ship_numbers):
        new_alien_ship = Alien_ship(game_settings, screen)
        alien_ships.add(new_alien_ship)


def check_fleet_edges(game_settings, aliens):
    """
        判断外形舰队是否碰到边
    """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(game_settings, aliens)
            break


def change_fleet_direction(game_settings, aliens):
    """
        修改外星舰队方向
    """
    for alien in aliens.sprites():
        alien.rect.y += game_settings.fleet_drop_speed
    game_settings.fleet_direction *= -1


def check_aliens_bottom(aliens, game_settings, ship, stats, screen, bullets, scoreboard, alien_bullets, alien_ships,
                        boss_aliens, boss_bullets, explosions):
    """
        判断外星舰队是否碰到底
    """
    screen_rect = screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(game_settings, stats, screen, ship, aliens, bullets, scoreboard, alien_bullets, alien_ships,
                     boss_aliens, boss_bullets, explosions)
            break


def ship_hit(game_settings, stats, screen, ship, aliens, bullets, scoreboard, alien_bullets, alien_ships, boss_aliens,
             boss_bullets, explosions):
    """
        飞船被击毁
    """
    game_settings.wide_bullet_remain = 0
    game_settings.strong_bullet_remain = 0
    stats.ships_left -= 1
    scoreboard.prep_ships()
    if pygame.mixer:
        game_settings.boom_sound.play()
    if stats.ships_left > 0:  # 还有飞船继续游戏
        aliens.empty()
        alien_bullets.empty()
        bullets.empty()
        alien_ships.empty()
        boss_aliens.empty()
        boss_bullets.empty()
        explosions.empty()
        create_fleet(game_settings, screen, aliens, ship, alien_ships)
        game_settings.is_boss_alien = False
        ship.reset()
        time.sleep(0.5)
    else:  # 游戏结束
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_play_button(ship, bullets, game_settings, screen, aliens, stats, play_button, mouse_x, mouse_y, scoreboard,
                      alien_bullets, alien_ships, boss_aliens, boss_bullets, explosions):
    """
        判断开始游戏按钮是否被点击
    """
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        game_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        scoreboard.prep_score()
        scoreboard.prep_level()
        scoreboard.prep_high_score()
        scoreboard.prep_bullets()
        aliens.empty()
        bullets.empty()
        alien_bullets.empty()
        alien_ships.empty()
        boss_aliens.empty()
        boss_bullets.empty()
        explosions.empty()
        ship.reset()
        create_fleet(game_settings, screen, aliens, ship, alien_ships)


def ship_fire_bullet(ship, bullets, game_settings, screen, scoreboard):
    """
        玩家开火
    """
    if len(bullets) < game_settings.bullet_max or int(game_settings.bullet_unlimit_time) > int(time.time()):
        # 子弹未到上限或在无限子弹时间内
        is_wide = False
        is_strong = False
        # 判断是否存在强力的子弹类型
        if (game_settings.wide_bullet_remain):
            is_wide = True
            game_settings.wide_bullet_remain -= 1
        if (game_settings.strong_bullet_remain):
            is_strong = True
            game_settings.strong_bullet_remain -= 1
        new_bullet = Bullet(game_settings, screen, ship, is_wide, is_strong)
        bullets.add(new_bullet)
        scoreboard.prep_bullets()
        if pygame.mixer:  # 开火声
            game_settings.bullet_fire_sound.play()


def alien_ships_fire(alien_ships, game_settings, screen, alien_bullets):
    """
        外星飞机开火
    """
    if len(alien_ships):  # 还有外星飞机能开火，随机开火
        if (random.randint(1, game_settings.alien_ships_fire_bullet_random) == 1):
            i = random.randint(0, len(alien_ships) - 1)
            new_alien_bullet = Alien_bullet(game_settings, screen, alien_ships.sprites()[i])
            alien_bullets.add(new_alien_bullet)
            if pygame.mixer:  # 开火声
                game_settings.alien_bullet_fire_sound.play()


def aliens_fire(aliens, game_settings, screen, alien_bullets):
    """
        普通外星人开火
    """
    if len(aliens):  # 还有外星人能开火，随机开火
        if (random.randint(1, game_settings.alien_fire_bullet_random) == 1):
            i = random.randint(0, len(aliens) - 1)
            new_alien_bullet = Alien_bullet(game_settings, screen, aliens.sprites()[i])
            alien_bullets.add(new_alien_bullet)
            if pygame.mixer:  # 开火声
                game_settings.alien_bullet_fire_sound.play()


def boss_fire(boss_aliens, game_settings, screen, boss_bullets):
    """
        外星boss开火
    """
    if len(boss_bullets) <= game_settings.boss_bullet_min and len(boss_aliens):
        # 有外星boss并且子弹数小于上限
        attack_type = random.randint(0, 2)
        # 第一种开火方式（从boss向四面八方开火）
        if attack_type == 1:
            boss_bullets_num = random.randint(1, game_settings.boss_bullet_max - len(boss_bullets))
            for i in range(0, boss_bullets_num):
                boss_bullet_grow_rate = random.uniform(1, game_settings.boss_bullet_grow_rate_max)  # 子弹变大速率
                boss_bullet_direction = random.uniform(0, 3.14)  # 开火方向
                new_boss_bullet = Boss_bullet(game_settings, screen, boss_aliens.sprites()[0].rect.centerx,
                                              boss_aliens.sprites()[0].rect.centery, boss_bullet_direction,
                                              boss_bullet_grow_rate)
                boss_bullets.add(new_boss_bullet)
                if pygame.mixer:
                    game_settings.alien_bullet_fire_sound.play()
        # 第二种开火方式（从屏幕边缘发射）
        elif attack_type == 2:
            boss_bullets_num = random.randint(1, game_settings.boss_bullet_max - len(boss_bullets))
            # 开火方向
            for i in range(0, boss_bullets_num // 3):
                y = random.randint(0, screen.get_rect().bottom)
                new_boss_bullet = Boss_bullet(game_settings, screen, 0, y, 0, 1)
                boss_bullets.add(new_boss_bullet)
            for i in range(0, boss_bullets_num // 3):
                y = random.randint(0, screen.get_rect().bottom)
                new_boss_bullet = Boss_bullet(game_settings, screen, screen.get_rect().right, y, 3.14, 1)
                boss_bullets.add(new_boss_bullet)
            for i in range(0, boss_bullets_num // 3):
                x = random.randint(0, screen.get_rect().right)
                new_boss_bullet = Boss_bullet(game_settings, screen, x, 0, 1.57, 1)
                boss_bullets.add(new_boss_bullet)


def check_ship_alien_bullet_collision(bullets, aliens, game_settings, screen, ship, stats, scoreboard, alien_bullets,
                                      alien_ships, boss_aliens, boss_bullets, explosions):
    """
        判断玩家飞船是否被外星子弹击中
    """
    hitted_alien_bullets = pygame.sprite.spritecollide(ship, alien_bullets, True)  # 被普通子弹击中
    hitted_boss_bullets = pygame.sprite.spritecollide(ship, boss_bullets, True)  # 被boss子弹击中
    if (hitted_alien_bullets or hitted_boss_bullets):  # 被击中
        for hitted_alien_bullet in hitted_alien_bullets:
            ship.life -= 1
            ship.prep_life()
        for hitted_boss_bullet in hitted_boss_bullets:
            ship.life -= 1
            ship.prep_life()
        if ship.life <= 0:  # 飞船没血了
            ship_hit(game_settings, stats, screen, ship, aliens, bullets, scoreboard, alien_bullets, alien_ships,
                     boss_aliens, boss_bullets, explosions)


def check_mutual_bullet_collision(bullets, alien_bullets, boss_bullets):
    """
        判断玩家子弹是否碰到并机会外星子弹
    """
    # 击毁外星人的子弹
    collisions1 = pygame.sprite.groupcollide(bullets, alien_bullets, False, True)
    collisions2 = pygame.sprite.groupcollide(bullets, boss_bullets, False, True)


def check_bullet_alien_collision(bullets, aliens, game_settings, screen, ship, explosions, stats, scoreboard,
                                 alien_ships, boss_aliens, alien_bullets, boss_bullets):
    """
        判断玩家子弹是否击中外星人
    """

    # 击中普通外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)
    if collisions:
        for bullet in collisions:
            # 子弹类型
            if bullet.is_strong_bullet == False:
                bullet.kill()
            for alien in collisions[bullet]:
                # 奖励类型
                if alien.type == 2:
                    game_settings.wide_bullet_remain += game_settings.alien_reward[alien.type]["wide_bullet_num"]
                elif alien.type == 3:
                    game_settings.strong_bullet_remain += game_settings.alien_reward[alien.type]["strong_bullet_num"]
                elif alien.type == 4:
                    game_settings.bullet_unlimit_time = max(game_settings.bullet_unlimit_time, time.time()) + \
                                                        game_settings.alien_reward[alien.type]["unlimited_bullet_time"]
                stats.score += game_settings.alien_points
                check_high_score(stats, scoreboard)
                scoreboard.prep_score()
                explosions.add(Explosion(alien))  # 爆炸
                if pygame.mixer:  # 爆炸声
                    game_settings.boom_sound.play()
    # 击中外星飞机
    collisions2 = pygame.sprite.groupcollide(bullets, alien_ships, False, False)
    if collisions2:
        for bullet in collisions2:
            # 子弹类型
            if bullet.is_strong_bullet == False:
                bullet.kill()
            for alien_ship in collisions2[bullet]:  # 外星飞机掉血
                alien_ship.life -= 1
                if alien_ship.life <= 0:  # 外星飞机没血
                    # 奖励
                    stats.score += game_settings.alien_ship_points
                    check_high_score(stats, scoreboard)
                    scoreboard.prep_score()
                    alien_ship.kill()
                    game_settings.wide_bullet_remain += game_settings.alien_ship_reward["wide_bullet_num"]
                    game_settings.strong_bullet_remain += game_settings.alien_ship_reward["strong_bullet_num"]
                    if ship.life < ship.life_max:
                        ship.life = ship.life_max
                    ship.prep_life()
                    explosions.add(Explosion(alien_ship))  # 爆炸
                    if pygame.mixer:  # 爆炸声
                        game_settings.boom_sound.play()
    # 击中外星boss
    collisions3 = pygame.sprite.groupcollide(bullets, boss_aliens, False, False)
    if collisions3:
        for bullet in collisions3:
            bullet.kill()
            for boss_alien in collisions3[bullet]:  # 外星boss掉血
                boss_alien.life -= 1
        for boss_alien in boss_aliens.sprites():
            if boss_alien.life <= 0:  # 外星boss没血了
                # 奖励
                stats.score += game_settings.boss_alien_points
                check_high_score(stats, scoreboard)
                scoreboard.prep_score()
                boss_alien.kill()
                game_settings.wide_bullet_remain += game_settings.boss_alien_reward["wide_bullet_num"]
                game_settings.strong_bullet_remain += game_settings.boss_alien_reward["strong_bullet_num"]
                if ship.life < ship.life_max:
                    ship.life = ship.life_max
                ship.life += game_settings.boss_alien_reward["ship_life_increase"]
                ship.prep_life()
                explosions.add(Explosion(boss_alien))  # 爆炸
                if pygame.mixer:  # 爆炸声
                    game_settings.boom_sound.play()

    scoreboard.prep_bullets()
    # 刷新外星人
    if len(aliens) == 0 and len(alien_ships) == 0 and len(boss_aliens) == 0:
        # bullets.empty()
        if (stats.level % game_settings.boss_alien_appearance_round == 0 and game_settings.is_boss_alien == False):
            # 每过一定轮次创造boss
            alien_bullets.empty()
            boss_bullets.empty()
            explosions.empty()
            ship.center_ship()
            create_boss_alien(game_settings, screen, alien_ships, boss_aliens)
            game_settings.is_boss_alien = True
        else:
            # 创造普通外星舰队并加强
            game_settings.is_boss_alien = False
            stats.level += 1
            scoreboard.prep_level()
            game_settings.increase_speed()
            alien_bullets.empty()
            boss_bullets.empty()
            explosions.empty()
            ship.center_ship()
            create_fleet(game_settings, screen, aliens, ship, alien_ships)


def check_high_score(stats, scoreboard):
    """
        判断最高分并更新
    """
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        scoreboard.prep_high_score()


def check_events(ship, bullets, game_settings, screen, aliens, stats, play_button, scoreboard, alien_bullets,
                 alien_ships, boss_aliens, boss_bullets, explosions):
    """
        判断玩家操作
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ship, bullets, game_settings, screen, aliens, stats, play_button, mouse_x, mouse_y,
                              scoreboard, alien_bullets, alien_ships, boss_aliens, boss_bullets, explosions)
        elif True:  # 判断按键
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    ship.moving_left = True
                if event.key == pygame.K_UP:
                    ship.moving_up = True
                if event.key == pygame.K_DOWN:
                    ship.moving_down = True
                if event.key == pygame.K_SPACE:
                    ship_fire_bullet(ship, bullets, game_settings, screen, scoreboard)
                if event.key==pygame.K_ESCAPE:
                    stats.game_active = False
                    pygame.mouse.set_visible(True)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    ship.moving_left = False
                if event.key == pygame.K_UP:
                    ship.moving_up = False
                if event.key == pygame.K_DOWN:
                    ship.moving_down = False


def update_bullets(bullets, aliens, game_settings, screen, ship, explosions, stats, scoreboard, alien_bullets,
                   alien_ships, boss_aliens, boss_bullets):
    """
        更新玩家子弹及其效果
    """
    bullets.update()  # 玩家子弹位置更新
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:  # 玩家子弹出边界，清除
            bullets.remove(bullet)
            scoreboard.prep_bullets()
    # 判断玩家子弹是否击中外星人
    check_bullet_alien_collision(bullets, aliens, game_settings, screen, ship, explosions, stats, scoreboard,
                                 alien_ships, boss_aliens, alien_bullets, boss_bullets)
    check_mutual_bullet_collision(bullets, alien_bullets, boss_bullets)  # 判断玩家子弹是否击毁外星人子弹
    for explosion in explosions.sprites():
        explosion.update()  # 爆炸效果


def update_aliens(aliens, game_settings, ship, stats, screen, bullets, scoreboard, alien_bullets, alien_ships,
                  boss_aliens, boss_bullets, explosions):
    """
        更新外星人及其攻击效果
    """
    check_fleet_edges(game_settings, aliens)
    aliens.update()  # 舰队更新
    alien_bullets.update()  # 外星子弹位置更新
    for alien_bullet in alien_bullets.copy():  # 外星子弹出边界，清除
        if alien_bullet.rect.bottom >= screen.get_rect().bottom:
            alien_bullets.remove(alien_bullet)
    boss_bullets.update()  # 外星boss子弹位置更新
    for boss_bullet in boss_bullets.copy():  # 外星boss子弹出边界，清除
        if boss_bullet.rect.bottom <= 0:
            boss_bullets.remove(boss_bullet)
        elif boss_bullet.rect.top >= screen.get_rect().bottom:
            boss_bullets.remove(boss_bullet)
        elif boss_bullet.rect.right <= 0:
            boss_bullets.remove(boss_bullet)
        elif boss_bullet.rect.left >= screen.get_rect().right:
            boss_bullets.remove(boss_bullet)
    # 判断玩家飞船是否碰到外星人，外星飞机，外星boss
    if (pygame.sprite.spritecollideany(ship, aliens)):
        ship_hit(game_settings, stats, screen, ship, aliens, bullets, scoreboard, alien_bullets, alien_ships,
                 boss_aliens, boss_bullets, explosions)
    if (pygame.sprite.spritecollideany(ship, alien_ships)):
        ship_hit(game_settings, stats, screen, ship, aliens, bullets, scoreboard, alien_bullets, alien_ships,
                 boss_aliens, boss_bullets, explosions)
    if (pygame.sprite.spritecollideany(ship, boss_aliens)):
        ship_hit(game_settings, stats, screen, ship, aliens, bullets, scoreboard, alien_bullets, alien_ships,
                 boss_aliens, boss_bullets, explosions)
    check_aliens_bottom(aliens, game_settings, ship, stats, screen, bullets, scoreboard, alien_bullets, alien_ships,
                        boss_aliens, boss_bullets, explosions)  # 判断外星人是否到底
    aliens_fire(aliens, game_settings, screen, alien_bullets)  # 外星人开火
    alien_ships_fire(alien_ships, game_settings, screen, alien_bullets)  # 外星飞机开火
    boss_fire(boss_aliens, game_settings, screen, boss_bullets)  # 外星人boss开火
    alien_ships.update()  # 外星飞机位置更新
    check_ship_alien_bullet_collision(bullets, aliens, game_settings, screen, ship, stats, scoreboard, alien_bullets,
                                      alien_ships, boss_aliens, boss_bullets, explosions)  # 判断玩家是否被子弹击中


def update_screen(game_settings, screen, ship, bullets, aliens, explosions, stats, play_button, scoreboard,
                  alien_bullets, alien_ships, boss_aliens, boss_bullets):
    """
        更新屏幕显示内容
    """
    screen.blit(game_settings.backgroud, (0, 0))
    ship.blitme()
    explosions.draw(screen)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for alien_bullet in alien_bullets.sprites():
        alien_bullet.draw_bullet()
    for boss_bullet in boss_bullets.sprites():
        boss_bullet.draw_bullet()
    aliens.draw(screen)
    alien_ships.draw(screen)
    boss_aliens.draw(screen)
    scoreboard.show_score()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()
