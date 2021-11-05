import time
import logging
from coordinates import *
from enums import Hashes, Buffers
from helpers.image_processing import ImageProcessing
from helpers.keyboard import keyboard_helper as keyboard
from helpers.mouse_helper import mouse_helper as mouse

# classe que contém as funcionalidades do bot
class Yuumi:

    def __init__(self, buddy_coord):
        self.attached = False
        self.buddy_coord = buddy_coord
        self.playing_side = 'b'
        self.img_p = ImageProcessing(1600, 900)
        self.mana = 100

    def __update_my_mana(self):
        black_amount = self.img_p.get_pixels_amount(YUUMI_MANA_BAR_L_COORD[0], YUUMI_MANA_BAR_L_COORD[1], YUUMI_MANA_BAR_R_COORD[0], YUUMI_MANA_BAR_R_COORD[1], Hashes.EMPTY_PIXEL_BAR)
        total = YUUMI_MANA_BAR_R_COORD[0] - YUUMI_MANA_BAR_L_COORD[0]
        #print('total: {total}, black amount: {black_amount}'.format(total=total, black_amount=black_amount))

    def __current_w_status(self):
        try:
            hash = self.img_p.get_box_hash(YUUMI_W_UL_COORD[0], YUUMI_W_UL_COORD[1], YUUMI_W_LR_COORD[0], YUUMI_W_LR_COORD[1])
        except:
            logging.warning('Falha ao calcular hash')
            return 0
        if (hash == Hashes.SKILL_W_IS_ATTACHED):
            logging.info('w status: attached')
            return 1
        elif (hash == Hashes.SKILL_W_IS_UP):
            logging.info('w status: skill up')
            return 2
        elif (hash == Hashes.SKILL_W_IS_CASTING):
            logging.info('w status: casting')
            return 3
        else:
            logging.info('w status: cooldown')
            return 4

    def __attach_to_buddy(self):
        try:
            mouse.move_mouse(self.buddy_coord)
        except:
            return
        time.sleep(Buffers.BUFFER_MOUSE_MOVEMENT)
        keyboard.press_ingame('w')
        logging.info('attached to ally {}'.format(self.buddy_coord))
        time.sleep(Buffers.BUFFER_ABILITY_CASTED)

    # itera pela string de prioridade e pressiona ctrl + tecla para cada skill, em ordem de prioridade
    def __level_up(priority: str):        
        for char in priority:
            keyboard.pressHoldRelease_ingame('ctrl', char)
            time.sleep(Buffers.BUFFER_SKILL_LEVELING)
            
    def __attempt_ultimate():
        pass
    
    def __attempt_healing():
        pass
    
    def __use_trinket():
        keyboard.press_ingame('4')            

    # função executada para comandar o bot
    def play(self):

        self.__update_my_mana()
        w_status = self.__current_w_status()
        if (w_status == 1):
            self.attached == True
        elif (self.attached == False and w_status == 2):
            logging.info('all alone :( ... attaching...')
            self.__attach_to_buddy()
        else:
            logging.info('oh noes.. RUNNN!!!!!')
            #self.__run_to_base()

        if (self.attached):
            #self.__attempt_ultimate()
            #self.__attempt_healing()
            self.__use_trinket()
            pass
            

        # upa skills prioridade para upar skills é R > E > W > Q
        #self.__level_up('rewq')
 