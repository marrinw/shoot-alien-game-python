import pygame.font


class Button_play():
    """
        开始游戏按钮
    """

    def __init__(self, game_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width = 200
        self.height = 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """
            修改显示的信息内容
        """
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """
            画图
        """
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Button_reset(Button_play):
    """
        重置score history按钮
    """

    def __init__(self, game_settings, screen, msg):
        super().__init__(game_settings, screen, msg)
        self.width = 80
        self.height = 25
        self.button_color = (127, 127, 127)
        self.font = pygame.font.SysFont(None, 20)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.top = self.screen_rect.top
        self.rect.left = self.screen_rect.left
        self.prep_msg(msg)


class Button_difficulty(Button_play):
    """
        重置score history按钮
    """

    def __init__(self, game_settings, screen, msg):
        super().__init__(game_settings, screen, msg)
        self.width = 150
        self.height = 25
        self.button_color = (127, 127, 127)
        self.font = pygame.font.SysFont(None, 20)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.top = self.screen_rect.top
        self.rect.left = self.screen_rect.left + 85
        self.prep_msg(msg)
