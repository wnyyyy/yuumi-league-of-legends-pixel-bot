import logging
import time
from helpers.mouse_helper import MouseHelper

width = 1921
height = 1081
x_pad = 0
y_pad = 0
debug = True

logging.info("Starting game...")
# yuumi = Yuumi()
# pixelBot = PixelBot(yuumi)
# pixelBot.game_init()
# pixelBot.play_game()

mouse_helper = MouseHelper(x_pad, y_pad)
# registra coordenadas do cursor para debug
if (debug):
    while True:
        mouse_helper.get_coords()
        time.sleep(1)
