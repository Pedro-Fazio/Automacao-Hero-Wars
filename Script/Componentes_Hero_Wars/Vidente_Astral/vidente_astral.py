import pyautogui
import time

pyautogui.PAUSE = 1

def completar_uma_vez():
    # pyautogui.moveTo(2260, 820, duration=2)
    # pyautogui.click(2260, 820)
    
    pyautogui.moveTo(2800, 1070, duration=2)
    pyautogui.click(2800, 1070)

    pyautogui.moveTo(2700, 730, duration=2)
    pyautogui.click(2600, 730)
    time.sleep(5)