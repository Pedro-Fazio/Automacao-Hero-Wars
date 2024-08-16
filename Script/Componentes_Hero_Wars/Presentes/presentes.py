import Util.funcoes_suporte as FS

#Aumentar isso: 780, 210
def presentear(coord_x, coord_y, tempo):
    # Clica em Presentes
    FS.mover_e_clicar(coord_x[0], coord_y[0], tempo[0])

    # Clica em Enviar
    FS.mover_e_clicar(coord_x[1], coord_y[1], tempo[1])

    # Envia os presentes
    FS.mover_e_clicar(coord_x[2], coord_y[2], tempo[2])

    # Fecha tela de envio dos presentes
    FS.mover_e_clicar(coord_x[3], coord_y[3], tempo[3])

    # Fecha tela de Presentes
    FS.mover_e_clicar(coord_x[4], coord_y[4], tempo[4])