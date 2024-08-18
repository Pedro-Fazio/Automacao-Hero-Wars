import pyautogui
import Configuracoes.menu as Menu

def main():
    #abrir_navegador(510, 1050)
    Menu.menu()


def abrir_navegador(coordenadaX, coordenadaY):
    pyautogui.click(coordenadaX, coordenadaY)


# Chamada da main para iniciar o código
if __name__ == "__main__":
    main()