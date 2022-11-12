import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from pygame.sprite import Group
def check_events(ship,bullets,game_settings,screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right=True
            elif event.key==pygame.K_LEFT:
                ship.moving_left=True
            elif event.key==pygame.K_SPACE:
                if len(bullets)<game_settings.bullet_max:
                    new_bullet=Bullet(game_settings,screen,ship)
                    bullets.add(new_bullet)
                    if pygame.mixer:
                        game_settings.bullet_fire_sound.play()

        if event.type==pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right=False
            elif event.key==pygame.K_LEFT:
                ship.moving_left=False

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

def update_screen(game_settings, screen, ship,bullets):
    screen.blit(game_settings.backgroud, (0, 0))
    ship.update()
    ship.blitme()
    update_bullets(bullets)


    pygame.display.flip()


def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("game")
    screen.blit(game_settings.backgroud, (0, 0))
    ship = Ship(screen,game_settings)
    bullets=Group()


    while True:
        check_events(ship,bullets,game_settings,screen)
        update_screen(game_settings, screen, ship,bullets)



if __name__ == '__main__':
    run_game()
