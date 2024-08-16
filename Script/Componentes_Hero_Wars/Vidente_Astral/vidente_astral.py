import Util.funcoes_suporte as FS

def completar_uma_vez(coord_x, coord_y, tempo):
    # Clica na Guilda
    FS.mover_e_clicar(coord_x[0], coord_y[0], tempo[0])

    # Clica em Asgard
    FS.mover_e_clicar(coord_x[1], coord_y[1], tempo[1])

    # Clica no Vidente Astral
    FS.mover_e_clicar(coord_x[2], coord_y[2], tempo[2])

    # Clica em Abrir
    FS.mover_e_clicar(coord_x[3], coord_y[3], tempo[3])

    # Clica no X da abertura do item
    FS.mover_e_clicar(coord_x[4], coord_y[4], tempo[4])

    # Clica no X do Vidente Astral
    FS.mover_e_clicar(coord_x[5], coord_y[5], tempo[5])

    # Clica no X de Asgard
    FS.mover_e_clicar(coord_x[6], coord_y[6], tempo[6])

    # Clica em Para a Cidade
    FS.mover_e_clicar(coord_x[7], coord_y[7], tempo[7])