import pyautogui as PY
import time
from pynput.mouse import Listener
import threading
from pynput import keyboard

mouse_clicked = False
click_x = 0
click_y = 0

def mover_e_clicar(coordenadaX, coordenadaY, timeSleep):
    PY.moveTo(coordenadaX, coordenadaY, duration=0.2)
    PY.click(coordenadaX, coordenadaY, duration=0.3)
    time.sleep(timeSleep)

def desenhar_linha():
    print('\n-'*30 + '\n')

def fechar_com_esc(qntd_escs):
    for _ in range(qntd_escs):
        PY.press('esc')
        time.sleep(0.1)

def captura_clique_coordenadas():
    global mouse_clicked, click_x, click_y
    try:
        start_mouse_listener()
        while True:
            x, y = PY.position()
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

def on_click(pressed):
    global mouse_clicked, click_x, click_y
    if pressed:
        click_x, click_y = PY.position()
        mouse_clicked = True

def start_mouse_listener():
    global listener
    listener = Listener(on_click=on_click)
    listener.start()

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
    
    # Tecla F8 para capturar
    if key == keyboard.Key.f8 and esperando_input:
        x, y = PY.position()
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
        return PY.pixel(x, y)
    except Exception as e:
        print(f"Erro ao capturar pixel: {e}")
        return (0, 0, 0)
