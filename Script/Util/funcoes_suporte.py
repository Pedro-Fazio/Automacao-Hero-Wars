import pyautogui
import time

def mover_e_clicar(coord_x, coord_y, timeSleep):
    pyautogui.moveTo(coord_x, coord_y, duration = 1)
    pyautogui.click(coord_x, coord_y, duration = 1)
    time.sleep(timeSleep)