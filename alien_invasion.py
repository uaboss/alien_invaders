import sys
import pygame


def run_game():
    '''Main function'''
    pygame.init() # initialization pygame library
    screen = pygame.display.set_mode((1200, 700)) # create main window for game
    pygame.display.set_caption('Alien_invasion') # set label for main window
    bg_color = (230, 230, 230)
    while True:
        for event in pygame.event.get(): # if have any event, process cycle
            if event.type == pygame.QUIT: # stop cycle if close main window
                sys.exit()
        screen.fill(bg_color) # fill main window solid color
        pygame.display.flip() # redraw all object in main window


run_game() # Call function 'run_game'
