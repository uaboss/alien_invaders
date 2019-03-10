import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class for Bullet implementation"""

    def __init__(self, ai_setting, screen, ship):
        """Constructor for Bullet"""
        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, ai_setting.bullet_width, ai_setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = ai_setting.bullet_color
        self.speed_factor = ai_setting.bullet_speed_factor


    def update(self):
        """ animate bullet to top of window """
        self.y -= self.speed_factor
        self.rect.y = self.y


    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


