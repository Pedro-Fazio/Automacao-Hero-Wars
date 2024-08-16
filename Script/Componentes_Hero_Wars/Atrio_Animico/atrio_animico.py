import Util.funcoes_suporte as FS

def resgatar_recompensa(coord_x, coord_y, tempo):
    # Clica no Átrio Anímico
    FS.mover_e_clicar(coord_x[0], coord_y[0], tempo[0])

    # Clica em Resgatar
    FS.mover_e_clicar(coord_x[1], coord_y[1], tempo[1])

    # Clica em Invocar
    FS.mover_e_clicar(coord_x[2], coord_y[2], tempo[2])

    # Clica na tela para pular animação de invocação
    FS.mover_e_clicar(coord_x[3], coord_y[3], tempo[3])

    # Clica em Ótimo!
    FS.mover_e_clicar(coord_x[4], coord_y[4], tempo[4])

    # Clica no X do Átrio Anímico
    FS.mover_e_clicar(coord_x[5], coord_y[5], tempo[5])