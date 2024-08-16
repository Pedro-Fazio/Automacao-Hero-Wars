import Util.funcoes_suporte as FS

def pegar_recompensa(coord_x, coord_y, tempo):
    # Clica na Grande Arena
    FS.mover_e_clicar(coord_x[0], coord_y[0], tempo[0])

    # Clica em Resgatar
    FS.mover_e_clicar(coord_x[1], coord_y[1], tempo[1])

    # Clica no X da Grande Arena
    FS.mover_e_clicar(coord_x[2], coord_y[2], tempo[2])

