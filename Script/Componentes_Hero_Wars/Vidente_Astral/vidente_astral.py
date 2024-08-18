import Util.funcoes_suporte as FS
import os

def completar_uma_vez(coord_x, coord_y, tempo):
    # Clica na Guilda
    FS.mover_e_clicar(coord_x[0], coord_y[0], tempo[0])

    # Clica em Asgard
    FS.mover_e_clicar(coord_x[1], coord_y[1], tempo[1])

    # Clica no Vidente Astral
    FS.mover_e_clicar(coord_x[2], coord_y[2], tempo[2])

    # Clica em Abrir
    FS.mover_e_clicar(coord_x[3], coord_y[3], tempo[3])

    # Clica no X da abertura do item
    FS.mover_e_clicar(coord_x[4], coord_y[4], tempo[4])

    # Clica no X do Vidente Astral
    FS.mover_e_clicar(coord_x[5], coord_y[5], tempo[5])

    # Clica no X de Asgard
    FS.mover_e_clicar(coord_x[6], coord_y[6], tempo[6])

    # Clica em Para a Cidade
    FS.mover_e_clicar(coord_x[7], coord_y[7], tempo[7])


def configurar_coordenadas():
    caminho_pasta = 'Configuracoes/Coordenadas/Coordenadas_Teste'
    caminho_arquivo = f'{caminho_pasta}/Vidente_Astral.txt'
    time_sleeps = ['10', '3', '3', '5', '1', '1', '1', '3']

    # Cria o diretório se ele não existir
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)

    coordenadas_x = []
    coordenadas_y = []

    print("\nClique na Guilda")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique em Asgard")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique no Vidente Astral")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique em Abrir")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique no X da abertura do item")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique no X do Vidente Astral")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique no X de Asgard")
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