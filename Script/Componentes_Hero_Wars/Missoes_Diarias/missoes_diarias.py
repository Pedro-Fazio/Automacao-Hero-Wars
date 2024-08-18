import Util.funcoes_suporte as FS
import os

def coletar_diarias(coord_x, coord_y, tempo):
    # Clica em Missões Diárias
    FS.mover_e_clicar(coord_x[0], coord_y[0], tempo[0])

    for _ in range(20):
        _coletar_recompensa(coord_x, coord_y, tempo)

    # Clicar no X de Missões Diárias
    FS.mover_e_clicar(coord_x[2], coord_y[2], tempo[2])


def _coletar_recompensa(coord_x, coord_y, tempo):
    # Clica em Concluída
    FS.mover_e_clicar(coord_x[1], coord_y[1], tempo[1])


def configurar_coordenadas():
    caminho_pasta = 'Configuracoes/Coordenadas/Coordenadas_Teste'
    caminho_arquivo = f'{caminho_pasta}/Missoes_Diarias.txt'
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

    print("\nClique em Concluída")
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