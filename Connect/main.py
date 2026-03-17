
#always set screen first before importing game library and working on game design
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = f'{50}, {50}'

import random
import pgzrun

WIDTH = 1000
HEIGHT = 600


def draw():
    screen.clear()
    screen.blit('background', (100, 100))


pgzrun.go()
