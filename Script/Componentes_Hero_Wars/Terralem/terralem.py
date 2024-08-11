import Util.funcoes_suporte as FS

def pegar_recompensas():
    # Clica em Terralém
    FS.mover_e_clicar(3890, 530, 3)

    _abrir_bau()

    # Clica no próximo chefe
    FS.mover_e_clicar(3125, 1000, 3)

    _abrir_bau()

    # Clica no próximo chefe
    FS.mover_e_clicar(3125, 1000, 3)

    _abrir_bau()

    # Clica no X do Terralém
    FS.mover_e_clicar(4450, 400, 3)

def _abrir_bau():
    # Clica em Abrir Baús
    FS.mover_e_clicar(3250, 760, 3)

    # Clica em Abrir
    FS.mover_e_clicar(3625, 850, 3)

    # Clica no X do janela do baú aberto
    FS.mover_e_clicar(3625, 880, 3)

    # Clica no X da janela Abrir Baús
    FS.mover_e_clicar(4450, 445, 3)