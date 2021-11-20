import time
import logging
import helpers.util as ut
from helpers.image_processing import ImageProcessing
from helpers.keyboard import keyboard_helper as keyboard
from helpers.mouse_helper import mouse_helper as mouse
from constants.buffers import *
from constants.coordinates import *
from constants.hashes import *
from constants.items import *

# classe que contém as funcionalidades do bot
class Yuumi:

    def __init__(self, buddy_coord):
        self.attached = False
        self.buddy_coord = buddy_coord
        self.playing_side = 'x'
        self.img_p = ImageProcessing(1600, 900)
        self.mana = -1
        self.ally_health = -1
        self.curr_lvl = 0
        self.items = []

    def __update_my_mana(self):
        black_amount = self.img_p.get_pixels_amount(Coords.YUUMI_MANA_BAR_L_COORD[0], Coords.YUUMI_MANA_BAR_L_COORD[1], Coords.YUUMI_MANA_BAR_R_COORD[0], Coords.YUUMI_MANA_BAR_R_COORD[1], Hashes.EMPTY_PIXEL_BAR, 2)
        #interpolação com valores x 0 113 e 266 para y 0 50 e 100
        self.mana = round(104 - (-0.00043*black_amount**2 + 0.49162*black_amount))
        self.mana = ut.clamp(self.mana, 0, 100)
        #print('mana: ' + str(self.mana))

    def __update_ally_health(self):
        old = self.ally_health
        black_amount = self.img_p.get_pixels_amount(Coords.ALLY_ADC_HEALTH_L_COORD[0], Coords.ALLY_ADC_HEALTH_L_COORD[1], Coords.ALLY_ADC_HEALTH_R_COORD[0], Coords.ALLY_ADC_HEALTH_R_COORD[1], Hashes.EMPTY_PIXEL_BAR_ALLY, 3)
        self.ally_health =  round(100 + (black_amount * 100 / (Coords.ALLY_ADC_HEALTH_L_COORD[0] - Coords.ALLY_ADC_HEALTH_R_COORD[0] - 2)))
        # print('ally health: ' + str(self.ally_health))
        if (old - self.ally_health > 40):
            self.__attempt_ultimate()
            print('ult')

    def __update_level(self):
        hash = self.img_p.get_box_hash(Coords.YUUMI_LVL_UL[0],Coords.YUUMI_LVL_UL[1], Coords.YUUMI_LVL_LR[0], Coords.YUUMI_LVL_LR[1])
        lvl = self.curr_lvl
        try:
            lvl = Hashes.LevelBoxHashDict[hash]
        except:
             return
        if (self.curr_lvl != lvl):
            priority = "rewq"
            time.sleep(Buffers.BUFFER_SKILL_LEVELING)
            for char in priority:
                keyboard.pressHoldRelease_ingame('ctrl', char)
            self.curr_lvl = lvl
        

    def __current_w_status(self):
        try:
            hash = self.img_p.get_box_hash(Coords.YUUMI_W_UL_COORD[0], Coords.YUUMI_W_UL_COORD[1], Coords.YUUMI_W_LR_COORD[0], Coords.YUUMI_W_LR_COORD[1])
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
            
    def __attempt_ultimate(self):
        pass
    
    def __attempt_healing(self):
        if (self.mana > 95) or (self.mana > 40 and self.ally_health < 75) or (self.ally_health < 30):
            keyboard.press_ingame('e')
    
    def __use_trinket(self):
        keyboard.press_ingame('4')

    def __is_in_base(self):
        hash = self.img_p.get_box_hash(Coords.YUUMI_GOLD_BAR_UL[0],Coords.YUUMI_GOLD_BAR_UL[1], Coords.YUUMI_GOLD_BAR_LR[0], Coords.YUUMI_GOLD_BAR_LR[1])
        return (hash == Hashes.GOLD_BAR_SHOP_AVAILABLE)

    def __buy_items(self):
        to_buy = [
            Items.GUME_DO_LADRAO_ARCANO,
            Items.REGENERADOR_DE_PEDRA_LUNAR,
            Items.PUTRIFICADOR_QUIMTECH,
            Items.CAJADO_AQUAFLUXO,
            Items.TURIBULO_ARDENTE,
            Items.REDENCAO
        ]
        keyboard.press_ingame('p')
        time.sleep(Buffers.BUFFER_MOUSE_MOVEMENT)
        try:
            mouse.move_mouse(Coords.SHOP_SEARCH_BAR)
        except:
            return
        time.sleep(Buffers.BUFFER_MOUSE_MOVEMENT)
        mouse.left_click()
        time.sleep(Buffers.BUFFER_MOUSE_MOVEMENT)
        for item in to_buy:
            if (self.items.__contains__(item) == False):
                keyboard.type_text(item)
            break


    # função executada para comandar o bot
    def play(self):

        #print("side: " + self.playing_side)
        #ms = mouse.get_coords()
        #self.img_p.get_box_hash(ms[0], ms[1], ms[0]+1, ms[1]+1)
        #hs = self.img_p.get_box_hash(Coords.SHOP_BUY_BUTTON_UL[0],Coords.SHOP_BUY_BUTTON_UL[1], Coords.SHOP_BUY_BUTTON_LR[0], Coords.SHOP_BUY_BUTTON_LR[1])
        #print(hs)
        #print(self.img_p.get_pixels_amount(ALLY_ADC_HEALTH_L_COORD[0], ALLY_ADC_HEALTH_L_COORD[1], ALLY_ADC_HEALTH_R_COORD[0], ALLY_ADC_HEALTH_R_COORD[1], Hashes.EMPTY_PIXEL_BAR_ALLY, 3))
        self.__update_my_mana()
        self.__update_ally_health()
        #self.__update_level()
        if (self.__is_in_base()):
            self.__buy_items()
        w_status = -6
        #w_status = self.__current_w_status()
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