import pyautogui
import time

def mover_e_clicar(coordenadaX, coordenadaY, timeSleep):
    pyautogui.moveTo(coordenadaX, coordenadaY, duration = 1)
    pyautogui.click(coordenadaX, coordenadaY, duration = 1)
    time.sleep(timeSleep)