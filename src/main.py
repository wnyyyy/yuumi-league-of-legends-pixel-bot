import logging
import time
from helpers.mouse_helper import mouse_helper as mouse_helper
from pixel_bot import PixelBot
import threading as th


width = 1921
height = 1081
debug = True

logging.basicConfig(filename='pixelbot.log', encoding='utf-8', level=logging.DEBUG)
logging.info("Starting game...")
pixel_bot = PixelBot()
th.Thread(target = pixel_bot.thread_freeze_bot, args = (), name = pixel_bot.thread_freeze_bot).start()
# pixel_bot.game_init()
pixel_bot.play_game()

# registra coordenadas do cursor para debug
if (debug):
    while True:
        time.sleep(1)
        try:
            mouse_helper.get_coords()
        finally:
            time.sleep(1)

