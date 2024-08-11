import Util.funcoes_suporte as FS

def resgatar_recompensa():
    # Clica no Átrio Anímico
    FS.mover_e_clicar(3695, 500, 3)

    # Clica em Resgatar
    FS.mover_e_clicar(4410, 500, 1)

    # Clica em Invocar
    FS.mover_e_clicar(3625, 1060, 1)

    # Clica na tela para pular animação de invocação
    FS.mover_e_clicar(3625, 1060, 2)

    # Clica em Ótimo!
    FS.mover_e_clicar(3500, 1100, 2)

    # Clica no X do Átrio Anímico
    FS.mover_e_clicar(4450, 400, 1)