import sys
import pygame
from settings import Settings


def run_game():
    '''Main function'''
    pygame.init() # initialization pygame library
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_height, ai_settings.screen_width)) # create main window for game
    pygame.display.set_caption('Alien_invasion') # set label for main window
    while True:
        for event in pygame.event.get(): # if have any event, process cycle
            if event.type == pygame.QUIT: # stop cycle if close main window
                sys.exit()
        screen.fill(ai_settings.bg_color) # fill main window solid color
        pygame.display.flip() # redraw all object in main window


run_game() # Call function 'run_game'
