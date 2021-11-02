import psutil

class PixelBot:
    def __init__(self, yuumi):
        self.yuumi = yuumi

    def __is_ingame():
        for proc in psutil.process_iter():
            try:
                if 'League of Legends' in proc.name():
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False
        
    def game_init(self):
        self.yuumi.buy_items()
    
    def play_game(self):
        while self.__is_ingame():
            self.yuumi.play()
