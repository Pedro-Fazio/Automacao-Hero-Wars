import Util.funcoes_suporte as FS

def percorrer_masmorra(coord_x, coord_y, tempo):
    # Clica em Guilda
    FS.mover_e_clicar(coord_x[0], coord_y[0], tempo[0])

    # Clica em Ilha da Guilda
    FS.mover_e_clicar(coord_x[1], coord_y[1], tempo[1])

    # Clica em Masmorra
    FS.mover_e_clicar(coord_x[2], coord_y[2], tempo[2])

    # Clica na cartinha das Provas do Oráculo
    FS.mover_e_clicar(coord_x[3], coord_y[3], tempo[3])

    # Clica em Confirmar para recompensa nivel 100
    FS.mover_e_clicar(coord_x[4], coord_y[4], tempo[4])

    # Clica em Confirmar para recompensa nivel 1000
    FS.mover_e_clicar(coord_x[5], coord_y[5], tempo[5])

    # Clica em Confirmar para recompensa nivel 2000
    FS.mover_e_clicar(coord_x[6], coord_y[6], tempo[6])

    # Clica no X das Provas do Oráculo
    FS.mover_e_clicar(coord_x[7], coord_y[7], tempo[7])

    # Clica em Para a Batalha!
    FS.mover_e_clicar(coord_x[8], coord_y[8], tempo[8])

    for _ in range(4):
        batalhar(coord_x, coord_y, tempo)

    batalhar_escolhendo_adversario(coord_x, coord_y, tempo)
    batalhar(coord_x, coord_y, tempo)
    batalhar_escolhendo_adversario(coord_x, coord_y, tempo)

    for _ in range(2):
        batalhar(coord_x, coord_y, tempo)

    batalhar_escolhendo_adversario_variacao(coord_x, coord_y, tempo)
    batalhar_variacao(coord_x, coord_y, tempo)

    for _ in range(3):
        batalhar(coord_x, coord_y, tempo)

    batalhar_escolhendo_adversario(coord_x, coord_y, tempo)

    # Clica no X da Masmorra
    FS.mover_e_clicar(coord_x[19], coord_y[19], tempo[19])

    # Clica no X da Ilha da Guilda
    FS.mover_e_clicar(coord_x[20], coord_y[20], tempo[20])

    # Clica em Para a Cidade
    FS.mover_e_clicar(coord_x[21], coord_y[21], tempo[21])


def batalhar(coord_x, coord_y, tempo):
    # Clica em Para a Batalha!
    FS.mover_e_clicar(coord_x[9], coord_y[9], tempo[9])

    # Clica em Aceitar o Destino!
    FS.mover_e_clicar(coord_x[10], coord_y[10], tempo[10])


def batalhar_escolhendo_adversario(coord_x, coord_y, tempo):
    # Clica em Para a Batalha!
    FS.mover_e_clicar(coord_x[11], coord_y[11], tempo[11])

    # Clica para lutar contra a primeira equipe
    FS.mover_e_clicar(coord_x[12], coord_y[12], tempo[12])

    # Clica em Aceitar o Destino!
    FS.mover_e_clicar(coord_x[13], coord_y[13], tempo[13])


def batalhar_escolhendo_adversario_variacao(coord_x, coord_y, tempo):
    # Clica em Para a Batalha!
    FS.mover_e_clicar(coord_x[14], coord_y[14], tempo[14])

    # Clica para lutar contra a primeira equipe
    FS.mover_e_clicar(coord_x[15], coord_y[15], tempo[15])

    # Clica em Aceitar o Destino!
    FS.mover_e_clicar(coord_x[16], coord_y[16], tempo[16])


def batalhar_variacao(coord_x, coord_y, tempo):
    # Clica em Para a Batalha!
    FS.mover_e_clicar(coord_x[17], coord_y[17], tempo[17])

    # Clica em Aceitar o Destino!
    FS.mover_e_clicar(coord_x[18], coord_y[18], tempo[18])
