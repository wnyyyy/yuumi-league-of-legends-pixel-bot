import os
from PIL import ImageGrab, ImageOps
import numpy as np
import datetime
import win32gui

class ImageProcessing:

    def __init__(self, game_width, game_heigth):
        self._game_heigth = game_heigth
        self._game_width = game_width

    # pega posiçao da janela focada na tela
    def __get_window_pos(self):
        window = win32gui.GetForegroundWindow()
        try:
            window_pos_x, window_pos_y, *etc = win32gui.GetWindowRect(window)
        finally:
            return (window_pos_x, window_pos_y)

    # janela do jogo
    def screen_grab_game_window(self):
        im = self.__screen_grab(1, 1, self._game_width, self._game_heigth)
        # im.save(os.getcwd() + '\\full_snap__' + str(datetime.datetime.now()).replace(':','') + '.png', 'PNG')
    
    def __screen_grab(self, lux, luy, rlx, rly):
        window = self.__get_window_pos()
        # print('window pos: {}'.format(window))
        bbox = (lux + window[0], luy + window[1], rlx + window[0], rly + window[1])
        im = ImageGrab.grab(bbox)
        im.save(os.getcwd() + '\\cut__' + str(datetime.datetime.now()).replace(':','') + '.png', 'PNG')
        return im

    # transforma img em grayscale e soma pixels
    def get_mean_pixel_value(self, lux: int, luy: int, rlx: int, rly: int):
        im = ImageOps.grayscale(self.__screen_grab(lux, luy, rlx, rly))
        a = np.array(im.getcolors())
        a = a.sum()
        print('pixel sum: {}'.format(a))
        return a
