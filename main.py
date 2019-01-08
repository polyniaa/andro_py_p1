# -*- coding: utf-8 -*-
"""
edited by me simple android game
@author: Chris Minar
game entry point
"""

import game_engine
#
import pygame_sdl2
pygame_sdl2.import_as_pygame()

import pygame

if __name__ in ('__android__',"__main__"):
    ge = game_engine.game_engine()
    ge.game_loop()
    ge.quit_game()
