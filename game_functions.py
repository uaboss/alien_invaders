import sys
import pygame


def check_events():
    """ Processing events and key press """
    for event in pygame.event.get(): # if have any event, process cycle
        if event.type == pygame.QUIT: # stop cycle if close main window
            sys.exit()


def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.bg_color) # fill main window solid color
    ship.blitme()
    pygame.display.flip() # redraw all object in main window
