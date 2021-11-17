from logging import error
from time import sleep
from PIL import ImageGrab, ImageOps
import numpy as np
import helpers.util as ut

class ImageProcessing:

    def __init__(self, game_width, game_heigth):
        self._game_heigth = game_heigth
        self._game_width = game_width

    # janela do jogo
    def screen_grab_game_window(self):
        im = self.__screen_grab(self, 1, 1, self._game_width, self._game_heigth)
        # im.save(os.getcwd() + '\\full_snap__' + str(datetime.datetime.now()).replace(':','') + '.png', 'PNG')
    
    def __screen_grab(self, lux, luy, rlx, rly):
        try:
            window = ut.get_window_pos()
        except:
            raise Exception
        # print('window pos: {}'.format(window))
        bbox = (lux + window[0], luy + window[1], rlx + window[0], rly + window[1])
        im = ImageGrab.grab(bbox)        
        return im
    
    # transforma img em grayscale e soma pixels
    def get_box_hash(self, lux: int, luy: int, rlx: int, rly: int):
        try:
            im = self.__screen_grab(lux, luy, rlx, rly)
            im = ImageOps.grayscale(im)
            a = np.array(im.getcolors())
            a = a.sum()
            # print('pixel sum: {}'.format(a))
            # im.save(os.getcwd() + '\\cut_' + str(a) + '_' + str(datetime.datetime.now()).replace(':','') + '.png', 'PNG')
            return a
        except:
            raise Exception

    def get_pixels_amount(self, lux: int, luy: int, rlx: int, rly: int, target_hash: int, error_margin: int):
        try:
            im = self.__screen_grab(lux, luy, rlx, rly)
            im = ImageOps.grayscale(im)
            pixels = list(im.getdata())
            amount = 0
            for i in pixels:
                if (abs(i - target_hash) <= error_margin):
                    amount += 1

            return amount
        except:
            raise Exception


