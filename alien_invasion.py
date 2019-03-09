import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    '''Main function'''
    pygame.init() # initialization pygame library
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) # create main window for game
    pygame.display.set_caption('Alien_invasion') # set label for main window
    ship = Ship(screen)
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)
run_game() # Call function 'run_game'
