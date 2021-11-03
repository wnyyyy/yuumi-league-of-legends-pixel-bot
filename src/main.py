import logging
import time

from helpers.mouse_helper import MouseHelper
from pixel_bot import PixelBot
from yuumi import Yuumi

width = 1921
height = 1081
debug = True

logging.info("Starting game...")
yuumi = Yuumi()
pixel_bot = PixelBot(yuumi)
# pixelBot.game_init()
# pixelBot.play_game()

mouse_helper = MouseHelper()
# registra coordenadas do cursor para debug
if (debug):
    while True:
        time.sleep(1)
        mouse_helper.get_coords()
        time.sleep(1)
