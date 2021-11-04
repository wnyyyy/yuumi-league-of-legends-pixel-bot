import time
import win32api, win32con, win32gui

class mouse_helper:

    def left_click(self):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    def right_click(self):
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
        time.sleep(.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)

    def move_mouse(self, coord):
        win32api.SetCursorPos(coord)
    
    def move_click_left_mouse(self, coord):
        self.move_mouse(coord)
        time.sleep(.1)
        self.left_click()
        
    def move_click_right_mouse(self, coord):
        self.move_mouse(coord)
        time.sleep(.1)
        self.right_click()

    def get_coords(self):
        window = win32gui.GetForegroundWindow()
        
        try:
            window_pos_x, window_pos_y, *etc = win32gui.GetWindowRect(window)

        #pega posição do mouse dentro da janela ativa
        finally:
            mouse_x, mouse_y = win32gui.GetCursorPos()
            x, y = (mouse_x - window_pos_x), (mouse_y - window_pos_y)

            print('x: {} y: {}'.format(x, y))
