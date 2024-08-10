import Util.funcoes_suporte as FS

def pega_recompensa_valquiria():
    # Clica no Dirigível
    FS.mover_e_clicar(3500, 500, 3)

    # Clica no baú do Benefício Valquíria
    FS.mover_e_clicar(3625, 575, 2)

    # Clica em Coletar
    FS.mover_e_clicar(3625, 875, 2)

    # Clica no X do Benefício da Valquíria
    FS.mover_e_clicar(4450, 400, 1)

    # Clica no X do Dirigível
    FS.mover_e_clicar(4455, 400, 1)