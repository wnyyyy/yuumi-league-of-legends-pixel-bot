import os
from time import sleep
from PIL import ImageGrab, ImageOps
import numpy as np
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
        try:
            window = self.__get_window_pos()
        except:
            return False
        # print('window pos: {}'.format(window))
        bbox = (lux + window[0], luy + window[1], rlx + window[0], rly + window[1])
        im = ImageGrab.grab(bbox)        
        return im

    # transforma img em grayscale e soma pixels
    def get_box_hash(self, lux: int, luy: int, rlx: int, rly: int):
        im = self.__screen_grab(lux, luy, rlx, rly)
        if (im != False):
            im = ImageOps.grayscale(im)
            a = np.array(im.getcolors())
            a = a.sum()
            # print('pixel sum: {}'.format(a))
            # im.save(os.getcwd() + '\\cut_' + str(a) + '_' + str(datetime.datetime.now()).replace(':','') + '.png', 'PNG')
            return a
        else:
            return -1


