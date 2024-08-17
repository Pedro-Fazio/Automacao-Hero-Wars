import pyautogui
import time
from pynput.mouse import Listener
import threading

# Variável para monitorar se houve clique do mouse
mouse_clicked = False
click_x = 0
click_y = 0

# Função para mover o mouse e clicar
def mover_e_clicar(coordenadaX, coordenadaY, timeSleep):
    pyautogui.moveTo(coordenadaX, coordenadaY, duration=1)
    pyautogui.click(coordenadaX, coordenadaY, duration=1)
    time.sleep(timeSleep)


# Função para capturar as coordenadas quando o mouse é clicado
def captura_clique_coordenadas():
    global mouse_clicked, click_x, click_y
    try:
        start_mouse_listener()  # Inicia o listener
        while True:
            x, y = pyautogui.position()
            posicao = f'X: {str(x).rjust(4)} Y: {str(y).rjust(4)}'
            print(posicao, end='')
            print('\b' * len(posicao), end='', flush=True)
            
            if mouse_clicked:  # Se o clique foi detectado
                mouse_clicked = False
                stop_mouse_listener()
                print("\n")
                return click_x, click_y  # Retorna as coordenadas ao capturar o clique

            time.sleep(0.1)  # Pausa curta para evitar sobrecarga de CPU
    except KeyboardInterrupt:
        print('\nPrograma interrompido.')

# Função chamada quando o mouse é clicado
def on_click(x, y, button, pressed):
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
def stop_mouse_listener():
    if listener.is_alive():
        listener.stop()

# Iniciar o Listener em uma thread separada
listener_thread = threading.Thread(target=start_mouse_listener)
listener_thread.daemon = True  # Define como thread daemon para encerrar com o programa principal
