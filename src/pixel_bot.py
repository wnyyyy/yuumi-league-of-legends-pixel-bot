import logging
from time import sleep
import time
import psutil
import keyboard as py_keyboard
import helpers.util as ut
from helpers.keyboard import keyboard_helper as keyboard
from yuumi import Yuumi
from constants.buffers import *
from constants.coordinates import *
from constants.hashes import *

# classe da engine
class PixelBot:
    def __init__(self):
        self.yuumi = Yuumi(Coords.ALLY_ADC)
        self.active = True

    # checa se processo do jogo existe
    def __is_ingame(self):
        for proc in psutil.process_iter():
            try:
                if 'League of Legends' in proc.name():
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False

    # aperta y para trancar câmera
    def __lock_camera(self):
        keyboard.press_in_game('y')

    def __get_playing_side(self):
        try:
            blue_side_check = self.yuumi.img_p.get_box_hash(Coords.MAP_BLUE_BASE_UL_COORD[0], Coords.MAP_BLUE_BASE_UL_COORD[1], Coords.MAP_BLUE_BASE_LR_COORD[0], Coords.MAP_BLUE_BASE_LR_COORD[1])
            red_side_check = self.yuumi.img_p.get_box_hash(Coords.MAP_RED_BASE_UL_COORD[0], Coords.MAP_RED_BASE_UL_COORD[1], Coords.MAP_RED_BASE_LR_COORD[0], Coords.MAP_RED_BASE_LR_COORD[1])
        except:
            logging.warning('Falha ao calcular hash')
            return False
        if (blue_side_check == Hashes.BLUE_SIDE_BLUE_CHECK and red_side_check == Hashes.BLUE_SIDE_RED_CHECK):
            self.yuumi.playing_side = 'b'
            logging.info('on blue team')
        elif (blue_side_check == Hashes.RED_SIDE_BLUE_CHECK and red_side_check == Hashes.RED_SIDE_RED_CHECK):
            logging.info('on red team')
            self.yuumi.playing_side = 'r'

    # freeza o bot
    def thread_freeze_bot(self):
        while True:
            py_keyboard.record('F10')
            if (self.active):
                self.active = False
            else:
                self.active = True
        
    # primeira ação do bot ao entrar na partida
    def game_init(self):
        ut.set_window_active()
        self.__lock_camera()
        self.__get_playing_side()
        # self.yuumi.buy_items()
    
    # loop que faz o bot agir enquanto o jogo estiver aberto
    def play_game(self):
        while self.__is_ingame():
            time.sleep(Buffers.BUFFER_ACTION_DELAY)
            if (self.active):
                #ut.set_window_active()
                #time.sleep(Buffers.BUFFER_WINDOW_FOCUSED)
                if (self.yuumi.playing_side == 'x'):
                    self.__get_playing_side()
                self.yuumi.play()
            
