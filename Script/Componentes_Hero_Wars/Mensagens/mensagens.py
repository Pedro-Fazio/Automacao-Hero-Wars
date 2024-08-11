import Util.funcoes_suporte as FS

def coletar_mensagens():
    # Clica em Mensagens
    FS.mover_e_clicar(3030, 450, 1)

    # Clica em Coletar Tudo
    FS.mover_e_clicar(3630, 1020, 1)

    # Clica em Mostrar Tudo
    FS.mover_e_clicar(3630, 970, 5)

    # Clica em Coletar Tudo
    FS.mover_e_clicar(3635, 970, 1)

    for _ in range(10):
        _coletar_mensagem()

    # Clica no X das Mensagens
    FS.mover_e_clicar(4020, 440, 1)

def _coletar_mensagem():
    FS.mover_e_clicar(0, 0, 1)