import time
import logging
from coordinates import *
from enums import Hashes
from helpers.image_processing import ImageProcessing
from helpers.keyboard import keyboard_helper as keyboard

# classe que contém as funcionalidades do bot
class Yuumi:

    def __init__(self):
        self.attached = None
        self.img_p = ImageProcessing(1600, 900)

    def __current_w_status(self):
        hash = self.img_p.get_box_hash(CH_W_UL[0], CH_W_UL[1], CH_W_LR[0], CH_W_LR[1])
        if (hash == Hashes.SKILL_W_IS_ATTACHED):
            logging.info('w status: attached')
        elif (hash == Hashes.SKILL_W_IS_UP):
            logging.info('w status: skill up')
        elif (hash == Hashes.SKILL_W_IS_CASTING):
            logging.info('w status: casting')
        else:
            logging.info('w status: cooldown')
    
    # itera pela string de prioridade e pressiona ctrl + tecla para cada skill, em ordem de prioridade
    def __level_up(priority: str):        
        for char in priority:
            keyboard.pressHoldRelease_ingame('ctrl', char)
            time.sleep(.05)

    # função executada para comandar o bot
    def play(self):

        # img_p = ImageProcessing(1600, 900)
        # img_p.get_box_hash(CH_W_UL[0], CH_W_UL[1], CH_W_LR[0], CH_W_LR[1])
        self.__current_w_status()

        # upa skills prioridade para upar skills é R > E > W > Q
        #self.__level_up('rewq')

        # timer para adicionar tempo mínimo entre as ações
        time.sleep(.5)
