import pygame
from pygame.sprite import Sprite


class Explosion(Sprite):
    containers = all

    def __init__(self, actor):
        super(Explosion, self).__init__()
        # Sprite.__init__(self, self.containers)
        self.image = pygame.image.load("./data/image/explosion.gif")
        self.rect = self.image.get_rect(center=actor.rect.center)
        self.life = 12

    def update(self):
        self.life = self.life - 1
        if self.life <= 0:
            self.kill()
