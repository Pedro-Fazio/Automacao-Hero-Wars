import pyautogui
import Util.funcoes_suporte as FS

pyautogui.PAUSE = 1

#Aumentar isso: 780, 210
def presentear():
    # Clica em presentes
    FS.mover_e_clicar(3910, 1060, 2)

    # Clica em enviar
    FS.mover_e_clicar(3450, 875, 2)

    # Enviar os presentes
    FS.mover_e_clicar(3625, 810, 2)

    # Fecha tela de envio dos presentes
    FS.mover_e_clicar(4010, 475, 2)

    # Fechar tela de presentes
    FS.mover_e_clicar(3990, 540, 2)