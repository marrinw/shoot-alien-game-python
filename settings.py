import pygame
class Settings():
        def __init__(self):
            self.screen_height=800
            self.screen_width=1200
            self.backgroud=pygame.image.load("./data/image/background.JPG")
            self.backgroud= pygame.transform.scale(self.backgroud,(self.screen_width,self.screen_height))
            self.ship_moving_speed=1.5
            self.bullet_speed=1
            self.bullet_width=3
            self.bullet_height=15
            self.bullet_color="yellow"
            self.bullet_max=3
            if(pygame.mixer):
                self.bullet_fire_sound=pygame.mixer.Sound("./data/sound/bullet_fire.wav")
