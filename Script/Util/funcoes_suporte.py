import pyautogui as PY
import time
from pynput.mouse import Listener
import threading
from pynput import keyboard

mouse_clicked = False
click_x = 0
click_y = 0

def clicar_e_aguardar_proximo(x_atual, y_atual, tempo_limite, x_proximo, y_proximo, cor_rgb, offset_x=0, offset_y=0):
    mover_e_clicar(x_atual, y_atual, 0)
    aguardar_cor_aparecer(x_proximo + offset_x, y_proximo + offset_y, cor_rgb, timeout_segundos=tempo_limite)

def mover_e_clicar(coordenadaX, coordenadaY, timeSleep):
    PY.moveTo(coordenadaX, coordenadaY, duration=0.1)
    PY.click(coordenadaX, coordenadaY, duration=0.2)
    time.sleep(timeSleep)

def desenhar_linha():
    print('\n-'*30 + '\n')

def fechar_com_esc(qntd_escs):
    for _ in range(qntd_escs):
        PY.press('esc')
        time.sleep(0.1)

def aguardar_cor_aparecer(x, y, cor_rgb, timeout_segundos=10, tolerancia=20):
    inicio = time.time()
    print(f" [dim]Aguardando cor {cor_rgb} na posição ({x}, {y})...[/]")
    
    while (time.time() - inicio) < timeout_segundos:
        if PY.pixelMatchesColor(x, y, cor_rgb, tolerance=tolerancia):
            return True
        else:
            time.sleep(0.2)
        
    print(f" [bold yellow][ALERTA] Cor não encontrada após {timeout_segundos}s. Continuando o fluxo...[/]")
    return False

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