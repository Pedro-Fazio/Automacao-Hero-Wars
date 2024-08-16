import Util.funcoes_suporte as FS

def coletar_mensagens(coord_x, coord_y, tempo):
    # Clica em Mensagens
    FS.mover_e_clicar(coord_x[0], coord_y[0], tempo[0])

    # Clica em Coletar Tudo
    FS.mover_e_clicar(coord_x[1], coord_y[1], tempo[1])

    # Clica em Mostrar Tudo
    FS.mover_e_clicar(coord_x[2], coord_y[2], tempo[2])

    # Clica em Coletar Tudo
    FS.mover_e_clicar(coord_x[3], coord_y[3], tempo[3])

    for _ in range(15):
        _coletar_mensagem(coord_x, coord_y, tempo)

    # Clica no X das Mensagens
    FS.mover_e_clicar(coord_x[6], coord_y[6], tempo[6])


def _coletar_mensagem(coord_x, coord_y, tempo):
    # Clica na mensagem
    FS.mover_e_clicar(coord_x[4], coord_y[4], tempo[4])

    # Clica em Coletar
    FS.mover_e_clicar(coord_x[5], coord_y[5], tempo[5])