import pyautogui
import time
from pynput.mouse import Listener
import threading
import sys
import os
import socket
from pynput import keyboard

mouse_clicked = False
click_x = 0
click_y = 0


def mover_e_clicar(coordenadaX, coordenadaY, timeSleep):
    pyautogui.moveTo(coordenadaX, coordenadaY, duration=1)
    pyautogui.click(coordenadaX, coordenadaY, duration=1)
    time.sleep(timeSleep)


def desenhar_linha():
    print('\n-'*30 + '\n')


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




def on_release(key):
    """Função disparada quando uma tecla é solta."""
    global dados_capturados, esperando_input
    
    # Usaremos a tecla F8 para capturar (pode mudar se quiser)
    if key == keyboard.Key.f8 and esperando_input:
        x, y = pyautogui.position()
        r, g, b = obter_cor_pixel(x, y)
        
        print(f"\n[CAPTURADO] Posição: ({x}, {y}) | Cor RGB: ({r}, {g}, {b})")
        
        dados_capturados = {
            "x": x,
            "y": y,
            "rgb": [r, g, b]
        }
        # Retorna False para parar o listener (sair do modo de espera)
        return False

def capturar_posicao_cor():
    """Inicia o listener do teclado e espera o usuário apertar F8."""
    global dados_capturados, esperando_input
    dados_capturados = None
    esperando_input = True
    
    print("\n>>> Posicione o mouse sobre o alvo e aperte 'F8' para capturar...")
    
    # Inicia o listener de forma bloqueante (o código para aqui até apertar F8)
    with keyboard.Listener(on_release=on_release) as listener:
        listener.join()
        
    return dados_capturados

def obter_cor_pixel(x, y):
    """Retorna a cor RGB do pixel na posição x, y."""
    try:
        # pyautogui.pixel retorna uma tupla (R, G, B)
        return pyautogui.pixel(x, y)
    except Exception as e:
        print(f"Erro ao capturar pixel: {e}")
        return (0, 0, 0)
