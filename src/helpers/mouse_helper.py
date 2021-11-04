import time
import win32api, win32con, win32gui
import helpers.util as ut

class mouse_helper:

    def left_click():
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    def right_click():
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
        time.sleep(.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)

    def move_mouse(coord):
        try:
            window_pos = ut.get_window_pos()
        except:
            raise Exception

        coord = (coord[0] + window_pos[0], coord[1] + window_pos[1])
        win32api.SetCursorPos(coord)

    # pega posição do mouse dentro da janela ativa
    def get_coords():
        try:
            window_pos = ut.get_window_pos()
        except:
            raise Exception

        mouse_x, mouse_y = win32gui.GetCursorPos()
        x, y = (mouse_x - window_pos[0]), (mouse_y - window_pos[1])

        print('x: {} y: {}'.format(x, y))
