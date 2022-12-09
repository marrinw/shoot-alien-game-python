import pygame
from pygame.sprite import Sprite


class Explosion(Sprite):
    """
        爆炸（外星人被摧毁的爆炸图片）
    """
    containers = all

    def __init__(self, actor):
        super(Explosion, self).__init__()
        self.image = pygame.image.load("./data/image/explosion.gif")
        self.rect = self.image.get_rect(center=actor.rect.center)
        self.life = 10  # 生命周期（存在帧数）

    def update(self):
        """
            更新
        """
        self.life = self.life - 1
        if self.life <= 0:
            self.kill()
