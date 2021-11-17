import time
import logging
import helpers.util as ut
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
        self.mana = -1
        self.ally_health = -1

    def __update_my_mana(self):
        black_amount = self.img_p.get_pixels_amount(YUUMI_MANA_BAR_L_COORD[0], YUUMI_MANA_BAR_L_COORD[1], YUUMI_MANA_BAR_R_COORD[0], YUUMI_MANA_BAR_R_COORD[1], Hashes.EMPTY_PIXEL_BAR, 2)
        #interpolação com valores x 0 113 e 266 para y 0 50 e 100
        self.mana = round(104 - (-0.00043*black_amount**2 + 0.49162*black_amount))
        self.mana = ut.clamp(self.mana, 0, 100)
        #print('mana: ' + str(self.mana))

    def __update_ally_health(self):
        old = self.ally_health
        black_amount = self.img_p.get_pixels_amount(ALLY_ADC_HEALTH_L_COORD[0], ALLY_ADC_HEALTH_L_COORD[1], ALLY_ADC_HEALTH_R_COORD[0], ALLY_ADC_HEALTH_R_COORD[1], Hashes.EMPTY_PIXEL_BAR_ALLY, 3)
        self.ally_health =  round(100 + (black_amount * 100 / (ALLY_ADC_HEALTH_L_COORD[0] - ALLY_ADC_HEALTH_R_COORD[0] - 2)))
        # print('ally health: ' + str(self.ally_health))
        if (old - self.ally_health > 40):
            self.__attempt_ultimate()
            print('ult')
        pass

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

    def __level_up(self):   
        priority = "rewq"     
        for char in priority:
            keyboard.pressHoldRelease_ingame('ctrl', char)
            time.sleep(Buffers.BUFFER_SKILL_LEVELING)
            
    def __attempt_ultimate(self):
        pass
    
    def __attempt_healing(self):
        if (self.mana > 95) or (self.mana > 40 and self.ally_health < 75) or (self.ally_health < 30):
            keyboard.press_ingame('e')
    
    def __use_trinket():
        keyboard.press_ingame('4')            

    # função executada para comandar o bot
    def play(self):

        ms = mouse.get_coords()
        #self.img_p.get_box_hash(ms[0], ms[1], ms[0]+1, ms[1]+1)
        #print(self.img_p.get_pixels_amount(ALLY_ADC_HEALTH_L_COORD[0], ALLY_ADC_HEALTH_L_COORD[1], ALLY_ADC_HEALTH_R_COORD[0], ALLY_ADC_HEALTH_R_COORD[1], Hashes.EMPTY_PIXEL_BAR_ALLY, 3))
        self.__update_my_mana()
        self.__update_ally_health()
        w_status = self.__current_w_status()
        if (w_status == 1):
            self.attached = True
        elif (w_status == 2):
            self.attached = False
            logging.info('all alone :( ... attaching...')
            self.__attach_to_buddy()
        else:
            logging.info('oh noes.. RUNNN!!!!!')
            #self.__run_to_base()

        if (self.attached):
            #self.__attempt_ultimate()
            self.__attempt_healing()
            #self.__use_trinket()
            pass            

        # upa skills prioridade para upar skills é R > E > W > Q
        self.__level_up()
 