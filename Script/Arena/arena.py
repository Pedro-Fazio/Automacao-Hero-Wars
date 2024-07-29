import pyautogui
import time

pyautogui.PAUSE = 1

def jogar_completo():
    coord_x = 1
    coord_y = 1
    pyautogui.click(coord_x, coord_y)
    time.sleep(1)