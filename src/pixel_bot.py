import psutil

# classe da engine
class PixelBot:
    def __init__(self, yuumi):
        self.yuumi = yuumi

    # checa se processo do jogo existe
    def __is_ingame():
        for proc in psutil.process_iter():
            try:
                if 'League of Legends' in proc.name():
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False
        
    # primeira ação do bot ao entrar na partida
    def game_init(self):
        self.yuumi.buy_items()
    
    # loop que faz o bot agir enquanto o jogo estiver aberto
    def play_game(self):
        while self.__is_ingame():
            self.yuumi.play()
