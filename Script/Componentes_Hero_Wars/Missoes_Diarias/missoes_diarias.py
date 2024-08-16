import Util.funcoes_suporte as FS

def coletar_diarias(coord_x, coord_y, tempo):
    # Clica em Missões Diárias
    FS.mover_e_clicar(coord_x[0], coord_y[0], tempo[0])

    for _ in range(20):
        _coletar_recompensa(coord_x, coord_y, tempo)

    # Clicar no X de Missões Diárias
    FS.mover_e_clicar(coord_x[2], coord_y[2], tempo[2])


def _coletar_recompensa(coord_x, coord_y, tempo):
    # Clica em Concluída
    FS.mover_e_clicar(coord_x[1], coord_y[1], tempo[1])