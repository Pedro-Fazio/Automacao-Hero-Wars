import pyautogui
import time
from pynput.mouse import Listener
import threading

mouse_clicked = False
click_x = 0
click_y = 0


def mover_e_clicar(coordenadaX, coordenadaY, timeSleep):
    pyautogui.moveTo(coordenadaX, coordenadaY, duration=1)
    pyautogui.click(coordenadaX, coordenadaY, duration=1)
    time.sleep(timeSleep)


def desenhar_linha():
    print('\n------------------------------------------------------------' +
        '----------------------------------------------------------------\n')


def captura_clique_coordenadas():
    global mouse_clicked, click_x, click_y
    try:
        start_mouse_listener()
        while True:
            x, y = pyautogui.position()
            posicao = f'X: {str(x).rjust(4)} Y: {str(y).rjust(4)}'
            print(posicao, end='')
            print('\b' * len(posicao), end='', flush=True)
            
            if mouse_clicked:
                mouse_clicked = False
                parar_mouse_listener()
                print("\n")
                return click_x, click_y

            # Pausa curta para evitar sobrecarga de CPU
            time.sleep(0.01)
    except KeyboardInterrupt:
        print('\nPrograma interrompido.')

# Função chamada quando o mouse é clicado
def on_click(pressed):
    global mouse_clicked, click_x, click_y
    if pressed:
        click_x, click_y = pyautogui.position()
        mouse_clicked = True

# Função para iniciar o listener
def start_mouse_listener():
    global listener
    listener = Listener(on_click=on_click)
    listener.start()

# Função para parar o listener
def parar_mouse_listener():
    if listener.is_alive():
        listener.stop()

# Iniciar o Listener em uma thread separada
listener_thread = threading.Thread(target=start_mouse_listener)
# Define como thread daemon para encerrar com o programa principal
listener_thread.daemon = True
