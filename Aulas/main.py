import pygame
import sys 
import Settings 
import Ship
import game_function as gf


def run_game():
    pygame.init()
    ai_settings = Settings.settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Ivasion')
    ship =Ship(screen)

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)


run_game()
