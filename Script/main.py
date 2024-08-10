import pyautogui
import Componentes_Hero_Wars.Arena.arena as Arena
import Componentes_Hero_Wars.Vidente_Astral.vidente_astral as Vidente_Astral
import Componentes_Hero_Wars.Presentes.presentes as Presentes
import Componentes_Hero_Wars.Dirigivel.dirigivel as Dirigivel
import Componentes_Hero_Wars.Grande_Arena.grande_arena as Grande_Arena

def main():
    #abrir_navegador(510, 1050)
    #arena()
    menu()

    # presentes()
    # vidente_astral()
    # dirigivel()
    grande_arena()


def menu():
    opcoes = {
        "1 - Jogar Arena": arena,
        "2 - Vidente Astral": vidente_astral,
        "3 - Presentes": presentes
    }

    #escolha = input("Escolha qual tarefa deseja realizar: ").lower()

    #resultado = opcoes.get(escolha)

    #print(resultado)


def abrir_navegador(coord_x, coord_y):
    pyautogui.click(coord_x, coord_y)


def arena():
    Arena.jogar_completo()


def grande_arena():
    Grande_Arena.pegar_recompensa()


def vidente_astral():
    Vidente_Astral.completar_uma_vez()


def presentes():
    Presentes.presentear()


def dirigivel():
    Dirigivel.pegar_recompensa_valquiria()



# Chamada da main para iniciar o código
if __name__ == "__main__":
    main()