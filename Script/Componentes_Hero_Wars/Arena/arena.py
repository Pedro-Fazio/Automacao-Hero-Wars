import Util.funcoes_suporte as FS

def batalhar(coord_x, coord_y, tempo):
    # Clica na Arena
    FS.mover_e_clicar(coord_x[0], coord_y[0], tempo[0])

    for _ in range(5):
        _lutar_uma_vez(coord_x, coord_y, tempo)

    # Clica no X da Arena
    FS.mover_e_clicar(coord_x[4], coord_y[4], tempo[4])



def _lutar_uma_vez(coord_x, coord_y, tempo):
    # Clica para atacar o primeiro jogador
    FS.mover_e_clicar(coord_x[1], coord_y[1], tempo[1])

    # Clica em Para a Batalha!
    FS.mover_e_clicar(coord_x[2], coord_y[2], tempo[2])

    # Clica em OK
    FS.mover_e_clicar(coord_x[3], coord_y[3], tempo[3])
