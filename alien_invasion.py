import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    """Main function"""
    pygame.init() # initialization pygame library

    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) # create main window for game
    pygame.display.set_caption('Alien_invasion') # set label for main window
    ship = Ship(ai_settings, screen)K
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, aliens)
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets, myfont)


run_game() # Call function 'run_game'

