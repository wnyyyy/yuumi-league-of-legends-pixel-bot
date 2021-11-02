import logging
import time
from helpers.mouse_helper import MouseHelper

width = 1281
height = 721
x_pad = 319
y_pad = 154


logging.info("Starting game...")
# yuumi = Yuumi()
# pixelBot = PixelBot(yuumi)
# pixelBot.game_init()
# pixelBot.play_game()

mouse_helper = MouseHelper(x_pad, y_pad)
# loga coordenadas do cursor para debug
while True:
    mouse_helper.get_coords()
    time.sleep(0.5)
