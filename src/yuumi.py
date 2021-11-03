import time
from coordinates import *
from helpers.image_processing import ImageProcessing
from helpers.keyboard import keyboard_helper as keyboard

# classe que contém as funcionalidades do bot
class Yuumi:

    def __init__(self):
        self.attached = None
        self.img_p = ImageProcessing(1600, 900)

    def __current_w_status(self):
        hash = self.img_p.get_box_hash(CH_W_UL[0], CH_W_UL[1], CH_W_LR[0], CH_W_LR[1])
        if (hash == 9953):
            print('w status: attached')
        if (hash == 9378):
            print('w status: skill up')
        if (hash == 2345):
            print('w status: casting')
    
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
