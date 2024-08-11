import Util.funcoes_suporte as FS

def coletar_diarias():
    # Clica em Missões Diárias
    FS.mover_e_clicar(3050, 390, 1)

    for _ in range(20):
        _coletar_recompensa()

    # Clicar no X de Missões Diárias
    FS.mover_e_clicar(4020, 490, 1)

def _coletar_recompensa():
    # Clica em Concluída
    FS.mover_e_clicar(3890, 600, 1)