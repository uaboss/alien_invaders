import pygame


class Ship():
    """Class for ship implementation"""

    def __init__(self,screen): # initialization ship on main window
        """Constructor for Ship (load image and define start position)"""
        self.screen = screen

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect() # ship image rectangle sprite init
        self.screen_rect = screen.get_rect() # screen rectangle init

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
