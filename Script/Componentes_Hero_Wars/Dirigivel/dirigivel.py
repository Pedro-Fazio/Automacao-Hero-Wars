import Util.funcoes_suporte as FS

def pegar_recompensa_valquiria(coord_x, coord_y, tempo):
    # Clica no Dirigível
    FS.mover_e_clicar(coord_x[0], coord_y[0], tempo[0])

    # Clica no baú do Benefício Valquíria
    FS.mover_e_clicar(coord_x[1], coord_y[1], tempo[1])

    # Clica em Coletar
    FS.mover_e_clicar(coord_x[2], coord_y[2], tempo[2])

    # Clica no X do Benefício da Valquíria
    FS.mover_e_clicar(coord_x[3], coord_y[3], tempo[3])

    # Clica no X do Dirigível
    FS.mover_e_clicar(coord_x[4], coord_y[4], tempo[4])