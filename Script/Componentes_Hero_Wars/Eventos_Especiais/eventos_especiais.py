import Util.funcoes_suporte as FS

def coletar_recompensas_imutaveis(coord_x, coord_y, tempo):
    # Clica em Eventos Especiais
    FS.mover_e_clicar(coord_x[0], coord_y[0], tempo[0])

    # Clica em Promoção de Visual
    FS.mover_e_clicar(coord_x[1], coord_y[1], tempo[1])

    # Clica em Coletar
    FS.mover_e_clicar(coord_x[2], coord_y[2], tempo[2])

    # Clica no X de Eventos Especiais
    FS.mover_e_clicar(coord_x[3], coord_y[3], tempo[3])