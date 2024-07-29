import pyautogui
import Componentes_Hero_Wars.Arena.arena as Arena
import Componentes_Hero_Wars.Vidente_Astral.vidente_astral as Vidente_Astral

def main():
    abrir_navegador(510, 1050)
    vidente_astral()


def abrir_navegador(coord_x, coord_y):
    pyautogui.click(coord_x, coord_y)


def jogar_arena():
    Arena.jogar_completo()

def vidente_astral():
    Vidente_Astral.completar_uma_vez()



# Chamada da main para iniciar o código
if __name__ == "__main__":
    main()