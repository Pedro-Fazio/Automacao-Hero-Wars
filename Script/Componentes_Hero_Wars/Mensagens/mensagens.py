import Util.funcoes_suporte as FS
import os

def coletar_mensagens(coord_x, coord_y, tempo):
    # Clica em Mensagens
    FS.mover_e_clicar(coord_x[0], coord_y[0], tempo[0])

    # Clica em Coletar Tudo
    FS.mover_e_clicar(coord_x[1], coord_y[1], tempo[1])

    # Clica em Mostrar Tudo
    FS.mover_e_clicar(coord_x[2], coord_y[2], tempo[2])

    # Clica em Coletar Tudo
    FS.mover_e_clicar(coord_x[3], coord_y[3], tempo[3])

    for _ in range(15):
        _coletar_mensagem(coord_x, coord_y, tempo)

    # Clica no X das Mensagens
    FS.mover_e_clicar(coord_x[6], coord_y[6], tempo[6])


def _coletar_mensagem(coord_x, coord_y, tempo):
    # Clica na mensagem
    FS.mover_e_clicar(coord_x[4], coord_y[4], tempo[4])

    # Clica em Coletar
    FS.mover_e_clicar(coord_x[5], coord_y[5], tempo[5])


def configurar_coordenadas():
    caminho_pasta = 'Configuracoes/Coordenadas/Coordenadas_Teste'
    caminho_arquivo = f'{caminho_pasta}/Mensagens.txt'
    time_sleeps = ['1', '1', '5', '1', '1', '1', '1']

    # Cria o diretório se ele não existir
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)

    coordenadas_x = []
    coordenadas_y = []

    print("\nClique em Mensagens")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique em Coletar Tudo")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique em Mostrar Tudo")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique em Coletar Tudo")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique em uma mensagem qualquer")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique em Coletar")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique no X das Mensagens")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    # Escreve as coordenadas em um arquivo
    with open(caminho_arquivo, 'w') as arquivo:
        for i in range(len(coordenadas_x)):
            arquivo.write(f"{coordenadas_x[i]}, {coordenadas_y[i]}, {time_sleeps[i]}\n")

    print("Coordenadas foram salvas em", caminho_arquivo)