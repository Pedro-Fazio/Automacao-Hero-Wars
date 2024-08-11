import Util.funcoes_suporte as FS

def percorrer_masmorra():
    # Clica em Guilda
    FS.mover_e_clicar(2825, 1025, 10)

    # Clica em Ilha da Guilda
    FS.mover_e_clicar(3750, 935, 1)

    # Clica em Masmorra
    FS.mover_e_clicar(3190, 690, 2)

    # Clica na cartinha das Provas do Oráculo
    FS.mover_e_clicar(2800, 410, 1)

    # Clica em Confirmar para recompensa nivel 100
    FS.mover_e_clicar(4025, 710, 1)

    # Clica em Confirmar para recompensa nivel 1000
    FS.mover_e_clicar(4025, 810, 1)

    # Clica em Confirmar para recompensa nivel 2000
    FS.mover_e_clicar(4025, 915, 1)

    # Clica no X das Provas do Oráculo
    FS.mover_e_clicar(4125, 475, 1)

    # Clica em Para a Batalha!
    FS.mover_e_clicar(3875, 625, 1)

    for _ in range(3):
        batalhar()

    batalhar_escolhendo_adversario()
    batalhar()
    batalhar_escolhendo_adversario()

    for _ in range(2):
        batalhar()

    batalhar_escolhendo_adversario_variacao()
    batalhar_variacao()

    for _ in range(3):
        batalhar()

    batalhar_escolhendo_adversario()

    # Clica no X da Masmorra
    FS.mover_e_clicar(4440, 400, 3)

    # Clica no X da Ilha da Guilda
    FS.mover_e_clicar(4450, 400, 3)

    # Clica em Para a Cidade
    FS.mover_e_clicar(2825, 1025, 1)


def batalhar():
    # Clica em Para a Batalha!
    FS.mover_e_clicar(3625, 625, 2)

    # Clica em Aceitar o Destino!
    FS.mover_e_clicar(3685, 940, 3)


def batalhar_escolhendo_adversario():
    # Clica em Para a Batalha!
    FS.mover_e_clicar(3625, 625, 2)

    # Clica para lutar contra a primeira equipe
    FS.mover_e_clicar(3375, 935, 2)

    # Clica em Aceitar o Destino!
    FS.mover_e_clicar(3685, 940, 3)


def batalhar_escolhendo_adversario_variacao():
    # Clica em Para a Batalha!
    FS.mover_e_clicar(3875, 625, 2)

    # Clica para lutar contra a primeira equipe
    FS.mover_e_clicar(3375, 935, 2)

    # Clica em Aceitar o Destino!
    FS.mover_e_clicar(3685, 940, 3)


def batalhar_variacao():
    # Clica em Para a Batalha!
    FS.mover_e_clicar(3875, 625, 2)

    # Clica em Aceitar o Destino!
    FS.mover_e_clicar(3685, 935, 3)
