import pygame
from pygame.sprite import Sprite


class Explosion(Sprite):
    """
        爆炸（外星人被摧毁的爆炸图片）
    """
    containers = all

    def __init__(self, actor):
        super(Explosion, self).__init__()
        self.image_orgin = pygame.image.load("./data/image/explosion.gif")
        self.image = pygame.image.load("./data/image/explosion.gif")
        self.orign_size = 9
        self.image = pygame.transform.scale(self.image_orgin, (self.orign_size, self.orign_size))
        self.center = actor.rect.center
        self.rect = self.image.get_rect(center=self.center)
        self.size = self.orign_size
        self.life = 12  # 生命周期（存在帧数）

    def update(self):
        """
            更新
        """
        self.life = self.life - 1
        self.grow()  # 增长
        if self.life <= 0:  # 到帧数后消失
            self.kill()

    def grow(self):
        """
            增长，爆炸图像变大
        """
        self.size += self.orign_size
        self.image = pygame.transform.scale(self.image_orgin, (self.size, self.size))
        self.rect = self.image.get_rect(center=self.center)
