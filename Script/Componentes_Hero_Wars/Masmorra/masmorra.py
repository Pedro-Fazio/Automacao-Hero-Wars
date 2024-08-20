import Util.funcoes_suporte as FS
import os

def percorrer_masmorra(coord_x, coord_y, tempo):
    # Clica em Guilda
    FS.mover_e_clicar(coord_x[0], coord_y[0], tempo[0])

    # Clica em Ilha da Guilda
    FS.mover_e_clicar(coord_x[1], coord_y[1], tempo[1])

    # Clica em Masmorra
    FS.mover_e_clicar(coord_x[2], coord_y[2], tempo[2])

    # Clica na cartinha das Provas do Oráculo
    FS.mover_e_clicar(coord_x[3], coord_y[3], tempo[3])

    # Clica em Confirmar para recompensa nivel 100
    FS.mover_e_clicar(coord_x[4], coord_y[4], tempo[4])

    # Clica em Confirmar para recompensa nivel 1000
    FS.mover_e_clicar(coord_x[5], coord_y[5], tempo[5])

    # Clica em Confirmar para recompensa nivel 2000
    FS.mover_e_clicar(coord_x[6], coord_y[6], tempo[6])

    # Clica no X das Provas do Oráculo
    FS.mover_e_clicar(coord_x[7], coord_y[7], tempo[7])

    # Clica em Para a Batalha!
    FS.mover_e_clicar(coord_x[8], coord_y[8], tempo[8])

    # Clica em Aceitar o Destino!
    FS.mover_e_clicar(coord_x[9], coord_y[9], tempo[9])

    for _ in range(3):
        batalhar(coord_x, coord_y, tempo)

    batalhar_escolhendo_adversario(coord_x, coord_y, tempo)
    batalhar(coord_x, coord_y, tempo)
    batalhar_escolhendo_adversario(coord_x, coord_y, tempo)

    for _ in range(2):
        batalhar(coord_x, coord_y, tempo)

    batalhar_escolhendo_adversario_variacao(coord_x, coord_y, tempo)
    batalhar_variacao(coord_x, coord_y, tempo)

    for _ in range(3):
        batalhar(coord_x, coord_y, tempo)

    batalhar_escolhendo_adversario(coord_x, coord_y, tempo)

    # Clica no X da Masmorra
    FS.mover_e_clicar(coord_x[20], coord_y[20], tempo[20])

    # Clica no X da Ilha da Guilda
    FS.mover_e_clicar(coord_x[21], coord_y[21], tempo[21])

    # Clica em Para a Cidade
    FS.mover_e_clicar(coord_x[22], coord_y[22], tempo[22])


def batalhar(coord_x, coord_y, tempo):
    # Clica em Para a Batalha!
    FS.mover_e_clicar(coord_x[10], coord_y[10], tempo[10])

    # Clica em Aceitar o Destino!
    FS.mover_e_clicar(coord_x[11], coord_y[11], tempo[11])


def batalhar_escolhendo_adversario(coord_x, coord_y, tempo):
    # Clica em Para a Batalha!
    FS.mover_e_clicar(coord_x[12], coord_y[12], tempo[12])

    # Clica para lutar contra a primeira equipe
    FS.mover_e_clicar(coord_x[13], coord_y[13], tempo[13])

    # Clica em Aceitar o Destino!
    FS.mover_e_clicar(coord_x[14], coord_y[14], tempo[14])


def batalhar_escolhendo_adversario_variacao(coord_x, coord_y, tempo):
    # Clica em Para a Batalha!
    FS.mover_e_clicar(coord_x[15], coord_y[15], tempo[15])

    # Clica para lutar contra a primeira equipe
    FS.mover_e_clicar(coord_x[16], coord_y[16], tempo[16])

    # Clica em Aceitar o Destino!
    FS.mover_e_clicar(coord_x[17], coord_y[17], tempo[17])


def batalhar_variacao(coord_x, coord_y, tempo):
    # Clica em Para a Batalha!
    FS.mover_e_clicar(coord_x[18], coord_y[18], tempo[18])

    # Clica em Aceitar o Destino!
    FS.mover_e_clicar(coord_x[19], coord_y[19], tempo[19])


def configurar_coordenadas():
    caminho_pasta = 'Configuracoes/Coordenadas/Coordenadas_Teste'
    caminho_arquivo = f'{caminho_pasta}/Masmorra.txt'
    time_sleeps = ['10', '1', '2', '1', '0', '0', '1', '1', '1',
                '2', '4', '2', '2', '4', '2', '2', '4', '2', '4', '3', '3', '3']

    # Cria o diretório se ele não existir
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)

    coordenadas_x = []
    coordenadas_y = []

    print("\nClique em Guilda")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique em Ilha da Guilda")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique em Masmorra")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique na cartinha das Provas do Oráculo")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique em Confirmar para recompensa nivel 100")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique em Confirmar para recompensa nivel 1000")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique em Confirmar para recompensa nivel 2000")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique no X das Provas do Oráculo")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique em Para a Batalha!")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique em Aceitar o Destino!")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique em Para a Batalha!")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique em Aceitar o Destino!")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)


    print('Agora vá completando a masmorra até a minha próxima orientação.')
    for _ in range(4):
        x, y = FS.captura_clique_coordenadas()


    print("\nClique em Para a Batalha!")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique para lutar contra a primeira equipe")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique em Aceitar o Destino!")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)


    print('Agora vá completando a masmorra até a minha próxima orientação.')
    for _ in range(9):
        x, y = FS.captura_clique_coordenadas()


    print("\nClique em Para a Batalha!")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique para lutar contra a primeira equipe")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique em Aceitar o Destino!")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique em Para a Batalha!")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique em Aceitar o Destino!")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)


    print('Agora vá completando a masmorra até a minha próxima orientação.')
    for _ in range(9):
        x, y = FS.captura_clique_coordenadas()


    print("\nClique no X da Masmorra")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique no X da Ilha da Guilda")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique em Para a Cidade")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    # Escreve as coordenadas em um arquivo
    with open(caminho_arquivo, 'w') as arquivo:
        for i in range(len(coordenadas_x)):
            arquivo.write(f"{coordenadas_x[i]}, {coordenadas_y[i]}, {time_sleeps[i]}\n")

    print("Coordenadas foram salvas em", caminho_arquivo)