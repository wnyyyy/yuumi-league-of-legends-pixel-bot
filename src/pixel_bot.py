import psutil
import win32gui, win32com.client
from helpers.keyboard import keyboard_helper as keyboard

# classe da engine
class PixelBot:
    def __init__(self, yuumi):
        self.yuumi = yuumi

    # foca janela do jogo
    def __set_window_active(self):
        window = win32gui.FindWindow(None, "League of Legends")
        win32gui.BringWindowToTop(window)
        win32gui.SetActiveWindow(window)
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        win32gui.SetForegroundWindow(window)

    # retorna true se janela do jogo está ativa
    def __is_window_active(self):
        window = win32gui.FindWindow(None, "League of Legends")
        active_window = win32gui.GetActiveWindow()
        return window == active_window

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
        
    # primeira ação do bot ao entrar na partida
    def game_init(self):
        self.__set_window_active()
        self.__lock_camera()
        self.yuumi.buy_items()
    
    # loop que faz o bot agir enquanto o jogo estiver aberto
    def play_game(self):
        while self.__is_ingame():
            if (self.__is_window_active):
                self.yuumi.play()
            
