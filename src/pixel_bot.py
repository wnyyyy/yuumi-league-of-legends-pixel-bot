from time import sleep
import time
import psutil
import keyboard as py_keyboard
import helpers.util as ut
from enums import Buffers
from helpers.keyboard import keyboard_helper as keyboard

# classe da engine
class PixelBot:
    def __init__(self, yuumi):
        self.yuumi = yuumi
        self.active = False

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
    def __lock_camera():
        keyboard.press_ingame('y')

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
        self.yuumi.buy_items()
    
    # loop que faz o bot agir enquanto o jogo estiver aberto
    def play_game(self):
        while self.__is_ingame():
            time.sleep(Buffers.BUFFER_ACTION_DELAY)
            if (self.active):
                ut.set_window_active()
                time.sleep(Buffers.BUFFER_WINDOW_FOCUSED)
                self.yuumi.play()
            
