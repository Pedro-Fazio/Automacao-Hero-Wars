import Util.funcoes_suporte as FS

def completar_torre():
    # Clica na Torre
    FS.mover_e_clicar(4060, 560, 3)

    # Clica em Conclusão Instantânea
    FS.mover_e_clicar(3625, 745, 2)

    # Clica em Escolher Baús
    FS.mover_e_clicar(3410, 925, 2)

    for _ in range(10):
        _coletar_recompensa()

    for _ in range(2):
        coletar_recompensa_alternativo()

    for _ in range(2):
        _coletar_recompensa()
    
    FS.mover_e_clicar(4000, 790, 1)

    FS.mover_e_clicar(3300, 860, 1)

    FS.mover_e_clicar(4450, 460, 1)

    FS.mover_e_clicar(2810, 400, 1)

    FS.mover_e_clicar(3625, 870, 1)

    FS.mover_e_clicar(3140, 1090, 1)

    FS.mover_e_clicar(3625, 1040, 1)

    FS.mover_e_clicar(3925, 450, 1)

    FS.mover_e_clicar(4440, 400, 1)


def _coletar_recompensa():
    # Clica no baú
    FS.mover_e_clicar(3875, 810, 1)

    # Clica em Abrir
    FS.mover_e_clicar(3300, 860, 1)

    # Clica em Continuar
    FS.mover_e_clicar(4060, 1040, 1)

def coletar_recompensa_alternativo():
    # Clica no baú
    FS.mover_e_clicar(3410, 790, 1)

    # Clica em Abrir
    FS.mover_e_clicar(3300, 860, 1)

    # Clica em Continuar
    FS.mover_e_clicar(4060, 1040, 1)
