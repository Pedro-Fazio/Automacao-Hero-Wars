import Util.funcoes_suporte as FS

def batalhar():
    # Clica na Arena
    FS.mover_e_clicar(4000, 770, 3)

    rotina1()
    rotina1()
    rotina1()
    rotina1()
    rotina1()

    # Clica no X da Arena
    FS.mover_e_clicar(4140, 450, 1)



def rotina1():
    # Clica para atacar o primeiro jogador
    FS.mover_e_clicar(3240, 825, 2)

    # Clica em Para a Batalha!
    FS.mover_e_clicar(4080, 1075, 130)

    # Clica em OK
    FS.mover_e_clicar(3640, 1000, 2)
