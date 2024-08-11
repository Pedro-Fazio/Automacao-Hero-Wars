import pyautogui
import Componentes_Hero_Wars.Arena.arena as Arena
import Componentes_Hero_Wars.Vidente_Astral.vidente_astral as Vidente_Astral
import Componentes_Hero_Wars.Presentes.presentes as Presentes
import Componentes_Hero_Wars.Dirigivel.dirigivel as Dirigivel
import Componentes_Hero_Wars.Grande_Arena.grande_arena as Grande_Arena
import Componentes_Hero_Wars.Terralem.terralem as Terralem
import Componentes_Hero_Wars.Masmorra.masmorra as Masmorra
import Componentes_Hero_Wars.Atrio_Animico.atrio_animico as Atrio_Animico
import Componentes_Hero_Wars.Torre.torre as Torre

def main():
    #abrir_navegador(510, 1050)
    #arena()
    menu()

    # presentes()
    # vidente_astral()
    # dirigivel()
    # grande_arena()
    # terralem()
    # masmorra()
    # atrio_animico()
    # torre()


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


def terralem():
    Terralem.pegar_recompensas()


def masmorra():
    Masmorra.percorrer_masmorra()


def atrio_animico():
    Atrio_Animico.resgatar_recompensa()


def torre():
    Torre.completar_torre()



# Chamada da main para iniciar o código
if __name__ == "__main__":
    main()