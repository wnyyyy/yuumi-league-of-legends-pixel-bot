import logging
from time import sleep
import time
import psutil
import keyboard as py_keyboard
from coordinates import *
import helpers.util as ut
from enums import Buffers, Hashes
from helpers.keyboard import keyboard_helper as keyboard
from yuumi import Yuumi
from coordinates import coordinates as coord

# classe da engine
class PixelBot:
    def __init__(self):
        self.yuumi = Yuumi(coord.ALLY_ADC)
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
        keyboard.press_ingame('y')

    def __get_playing_side(self):
        try:
            blue_side_check = self.yuumi.img_p.get_box_hash(MAP_BLUE_BASE_UL[0], MAP_BLUE_BASE_UL[1], MAP_BLUE_BASE_LR[0], MAP_BLUE_BASE_LR[1])
            red_side_check = self.yuumi.img_p.get_box_hash(MAP_RED_BASE_UL[0], MAP_RED_BASE_UL[1], MAP_RED_BASE_LR[0], MAP_RED_BASE_LR[1])
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
                ut.set_window_active()
                time.sleep(Buffers.BUFFER_WINDOW_FOCUSED)
                self.yuumi.play()
            
