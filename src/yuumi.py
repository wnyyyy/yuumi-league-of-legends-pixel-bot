import time
import logging
from coordinates import *
from enums import Hashes, Buffers
from helpers.image_processing import ImageProcessing
from helpers.keyboard import keyboard_helper as keyboard
from helpers.mouse_helper import mouse_helper as mouse

# classe que contém as funcionalidades do bot
class Yuumi:

    def __init__(self, buddyId):
        self.attached = False
        self.buddyId = buddyId
        self.img_p = ImageProcessing(1600, 900)

    def __current_w_status(self):
        try:
            hash = self.img_p.get_box_hash(CH_W_UL[0], CH_W_UL[1], CH_W_LR[0], CH_W_LR[1])
        except:
            logging.warning('Falha ao calcular hash')
            return 0
        if (hash == Hashes.SKILL_W_IS_ATTACHED):
            logging.info('w status: attached')
            self.attached = True
            return 1
        elif (hash == Hashes.SKILL_W_IS_UP):
            logging.info('w status: skill up')
            self.attached = False
            return 2
        elif (hash == Hashes.SKILL_W_IS_CASTING):
            logging.info('w status: casting')
            self.attached = False
            return 3
        else:
            logging.info('w status: cooldown')
            self.attached = False
            return 4

    def __attach_to_buddy(self):
        coords = TEAM_ALLY_4
        if (self.buddyId == 1):
            coords = TEAM_ALLY_1
        elif (self.buddyId == 2):
            coords = TEAM_ALLY_2
        elif (self.buddyId == 3):
            coords = TEAM_ALLY_3

        try:
            mouse.move_mouse(coords)
        except:
            return
        time.sleep(Buffers.BUFFER_MOUSE_MOVEMENT)
        keyboard.press_ingame('w')
        logging.info('attached to ally {}'.format(self.buddyId))
        time.sleep(Buffers.BUFFER_ABILITY_CASTED)

    # itera pela string de prioridade e pressiona ctrl + tecla para cada skill, em ordem de prioridade
    def __level_up(priority: str):        
        for char in priority:
            keyboard.pressHoldRelease_ingame('ctrl', char)
            time.sleep(Buffers.BUFFER_SKILL_LEVELING)

    # função executada para comandar o bot
    def play(self):

        # img_p = ImageProcessing(1600, 900)
        # img_p.get_box_hash(CH_W_UL[0], CH_W_UL[1], CH_W_LR[0], CH_W_LR[1])
        w_status = self.__current_w_status()
        if (self.attached == False):
            logging.info('all alone :(')
            self.__attach_to_buddy()

        # upa skills prioridade para upar skills é R > E > W > Q
        #self.__level_up('rewq')
