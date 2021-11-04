import win32gui, win32com.client

class Util:

    # pega posiçao da janela focada na tela
    def get_window_pos(self):
        window = win32gui.GetForegroundWindow()
        try:
            window_pos_x, window_pos_y, *etc = win32gui.GetWindowRect(window)
        finally:
            return (window_pos_x, window_pos_y)

    # foca janela do jogo
    def set_window_active(self):
        window = win32gui.FindWindow(None, "League of Legends (TM) Client")
        win32gui.BringWindowToTop(window)
        win32gui.SetActiveWindow(window)
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        win32gui.SetForegroundWindow(window)