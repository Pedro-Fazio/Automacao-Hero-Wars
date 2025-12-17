import Util.funcoes_suporte as FS
import os
import random


def tabletop(coord_x, coord_y, tempo):
    for _ in range(1000):
        # Clica no Color Tint
        FS.mover_e_clicar(2940, 645, 0)
        
        # Gera coordenadas aleatórias dentro do intervalo
        x = random.randint(2200, 2480)
        y = random.randint(290, 570)

        # Clica na cor
        FS.mover_e_clicar(x, y, 0)
    
        # Clica em Apply
        FS.mover_e_clicar(2290, 760, 0)
    

def coletar_missoes_guilda(coord_x, coord_y, tempo):
    # Clica em Missões Diárias
    FS.mover_e_clicar(coord_x[0], coord_y[0], tempo[0])
    
    # Clica em Missões da Guilda
    FS.mover_e_clicar(coord_x[1], coord_y[1], tempo[1])

    for _ in range(10):
        _coletar_recompensa(coord_x, coord_y, tempo)
        
    # Coletar primeiro baú
    FS.mover_e_clicar(coord_x[3], coord_y[3], tempo[3])
    
    # Coletar segundo baú
    FS.mover_e_clicar(coord_x[4], coord_y[4], tempo[4])
    
    # Coletar terceiro baú
    FS.mover_e_clicar(coord_x[5], coord_y[5], tempo[5])
    
    # Coletar quarto baú
    FS.mover_e_clicar(coord_x[6], coord_y[6], tempo[6])

    # Clicar no X de Missões da Guilda
    FS.mover_e_clicar(coord_x[7], coord_y[7], tempo[7])

    # Clicar no X de Missões Diárias
    FS.mover_e_clicar(coord_x[8], coord_y[8], tempo[8])


def _coletar_recompensa(coord_x, coord_y, tempo):
    # Clica em Concluída
    FS.mover_e_clicar(coord_x[2], coord_y[2], tempo[2])


def configurar_coordenadas():
    caminho_pasta = 'Configuracoes/Coordenadas/Coordenadas_Teste'
    caminho_arquivo = f'{caminho_pasta}/Missoes_Guilda.txt'
    time_sleeps = ['1', '1', '1']

    # Cria o diretório se ele não existir
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)

    coordenadas_x = []
    coordenadas_y = []

    print("\nClique em Missões Diárias")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)
    
    print("\nClique em Missões da Guilda")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique em Concluída")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique no X de Missões da Guilda")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)
    
    print("\nClique no X de Missões Diárias")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    # Escreve as coordenadas em um arquivo
    with open(caminho_arquivo, 'w') as arquivo:
        for i in range(len(coordenadas_x)):
            arquivo.write(f"{coordenadas_x[i]}, {coordenadas_y[i]}, {time_sleeps[i]}\n")

    print("Coordenadas foram salvas em", caminho_arquivo)