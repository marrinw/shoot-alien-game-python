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
        self.width = 150
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
        self.rect.top = self.screen_rect.top + 26
        self.rect.left = self.screen_rect.left
        self.prep_msg(msg)


class Button_background(Button_play):
    """
        修改background按钮
    """

    def __init__(self, game_settings, screen, msg):
        super().__init__(game_settings, screen, msg)
        self.width = 150
        self.height = 25
        self.button_color = (127, 127, 127)
        self.font = pygame.font.SysFont(None, 20)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.top = self.screen_rect.top + 52
        self.rect.left = self.screen_rect.left
        self.prep_msg(msg)


class Button_ship_img(Button_play):
    """
        修改ship img按钮
    """

    def __init__(self, game_settings, screen, msg):
        super().__init__(game_settings, screen, msg)
        self.width = 150
        self.height = 25
        self.button_color = (127, 127, 127)
        self.font = pygame.font.SysFont(None, 20)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.top = self.screen_rect.top + 78
        self.rect.left = self.screen_rect.left
        self.prep_msg(msg)


class Button_bgm_on(Button_play):
    """
        修改ship img按钮
    """

    def __init__(self, game_settings, screen, msg=""):
        super().__init__(game_settings, screen, msg)
        self.width = 150
        self.height = 25
        self.button_color = (127, 127, 127)
        self.font = pygame.font.SysFont(None, 20)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.top = self.screen_rect.top + 130
        self.rect.left = self.screen_rect.left
        self.game_settings = game_settings
        self.prep_msg(self.get_msg())

    def get_msg(self):
        """
            获得显示文字
        """
        if self.game_settings.bgm_on == True:
            return "Turn off bgm in game"
        return "Turn on bgm in game"

    def draw_button(self):
        """
            画图
        """
        self.prep_msg(self.get_msg())
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Button_bgm(Button_play):
    """
        修改bgm按钮
    """

    def __init__(self, game_settings, screen, msg):
        super().__init__(game_settings, screen, msg)
        self.width = 150
        self.height = 25
        self.button_color = (127, 127, 127)
        self.font = pygame.font.SysFont(None, 20)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.top = self.screen_rect.top + 104
        self.rect.left = self.screen_rect.left
        self.prep_msg(msg)
