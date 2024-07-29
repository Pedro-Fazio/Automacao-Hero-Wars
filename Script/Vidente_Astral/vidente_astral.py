import pyautogui
import time

pyautogui.PAUSE = 1

def completar_uma_vez():
    pyautogui.moveTo(2260, 820, duration=2)
    pyautogui.click(2260, 820)

    pyautogui.moveTo(2600, 730, duration=2)
    pyautogui.click(2600, 730)
    time.sleep(5)