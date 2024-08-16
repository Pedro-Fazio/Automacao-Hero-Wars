import Util.funcoes_suporte as FS

def pegar_recompensas(coord_x, coord_y, tempo):
    # Clica em Terralém
    FS.mover_e_clicar(coord_x[0], coord_y[0], tempo[0])

    _abrir_bau()

    # Clica no próximo chefe
    FS.mover_e_clicar(coord_x[5], coord_y[5], tempo[5])

    _abrir_bau()

    # Clica no próximo chefe
    FS.mover_e_clicar(coord_x[6], coord_y[6], tempo[6])

    _abrir_bau()

    # Clica no X do Terralém
    FS.mover_e_clicar(coord_x[7], coord_y[7], tempo[7])


def _abrir_bau(coord_x, coord_y, tempo):
    # Clica em Abrir Baús
    FS.mover_e_clicar(coord_x[1], coord_y[1], tempo[1])

    # Clica em Abrir
    FS.mover_e_clicar(coord_x[2], coord_y[2], tempo[2])

    # Clica no X do janela do baú aberto
    FS.mover_e_clicar(coord_x[3], coord_y[3], tempo[3])

    # Clica no X da janela Abrir Baús
    FS.mover_e_clicar(coord_x[4], coord_y[4], tempo[4])