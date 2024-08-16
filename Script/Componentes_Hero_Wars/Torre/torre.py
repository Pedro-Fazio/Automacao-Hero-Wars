import Util.funcoes_suporte as FS

def completar_torre(coord_x, coord_y, tempo):
    # Clica na Torre
    FS.mover_e_clicar(coord_x[0], coord_y[0], tempo[0])

    # Clica em Conclusão Instantânea
    FS.mover_e_clicar(coord_x[1], coord_y[1], tempo[1])

    # Clica em Escolher Baús
    FS.mover_e_clicar(coord_x[2], coord_y[2], tempo[2])

    for _ in range(10):
        _coletar_recompensa(coord_x, coord_y, tempo)

    for _ in range(2):
        coletar_recompensa_alternativo(coord_x, coord_y, tempo)

    for _ in range(2):
        _coletar_recompensa(coord_x, coord_y, tempo)
    
    # Clica no baú principal
    FS.mover_e_clicar(coord_x[9], coord_y[9], tempo[9])

    # Clica em Abrir
    FS.mover_e_clicar(coord_x[10], coord_y[10], tempo[10])

    # Clica no X do baú principal
    FS.mover_e_clicar(coord_x[11], coord_y[11], tempo[11])

    # Clica no ícone de caveira
    FS.mover_e_clicar(coord_x[12], coord_y[12], tempo[12])

    # Clica em Troque moedas de crânio
    FS.mover_e_clicar(coord_x[13], coord_y[13], tempo[13])

    # Clica em Pontos de Torre
    FS.mover_e_clicar(coord_x[14], coord_y[14], tempo[14])

    # Clica em Coletar Tudo
    FS.mover_e_clicar(coord_x[15], coord_y[15], tempo[15])

    # Clica no X dos Pontos de Torre
    FS.mover_e_clicar(coord_x[16], coord_y[16], tempo[16])

    # Clica no X da Torre
    FS.mover_e_clicar(coord_x[17], coord_y[17], tempo[17])


def _coletar_recompensa(coord_x, coord_y, tempo):
    # Clica no baú
    FS.mover_e_clicar(coord_x[3], coord_y[3], tempo[3])

    # Clica em Abrir
    FS.mover_e_clicar(coord_x[4], coord_y[4], tempo[4])

    # Clica em Continuar
    FS.mover_e_clicar(coord_x[5], coord_y[5], tempo[5])


def coletar_recompensa_alternativo(coord_x, coord_y, tempo):
    # Clica no baú
    FS.mover_e_clicar(coord_x[6], coord_y[6], tempo[6])

    # Clica em Abrir
    FS.mover_e_clicar(coord_x[7], coord_y[7], tempo[7])

    # Clica em Continuar
    FS.mover_e_clicar(coord_x[8], coord_y[8], tempo[8])
