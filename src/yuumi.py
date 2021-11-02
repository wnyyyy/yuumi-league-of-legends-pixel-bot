import time
from helpers.keyboard import keyboard_helper as keyboard

# classe que contém as funcionalidades do bot
class Yuumi:
    
    # itera pela string de prioridade e pressiona ctrl + tecla para cada skill, em ordem de prioridade
    def __level_up(priority: str):        
        for char in priority:
            keyboard.pressHoldRelease_ingame('ctrl', char)
            time.sleep(.05)

    # função executada para comandar o bot
    def play(self):

        # upa skills prioridade para upar skills é R > E > W > Q
        self.__level_up('rewq')

        # timer para adicionar tempo mínimo entre as ações
        time.sleep(.5)
