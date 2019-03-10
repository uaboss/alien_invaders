import sys
import pygame
from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """ Processing events and key press """
    for event in pygame.event.get(): # if have any event, process cycle
        if event.type == pygame.QUIT: # stop cycle if close main window
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets, myfont):
    screen.fill(ai_settings.bg_color) # fill main window solid color
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    textsurface = myfont.render(str(len(bullets)), False, (0, 0, 0))
    screen.blit(textsurface, (0, 0))
    ship.blitme()
    pygame.display.flip() # redraw all object in main window
