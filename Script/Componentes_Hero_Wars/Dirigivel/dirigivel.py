import Util.funcoes_suporte as FS
import os

def pegar_recompensa_valquiria(coord_x, coord_y, tempo):
    # Clica no Dirigível
    FS.mover_e_clicar(coord_x[0], coord_y[0], tempo[0])

    # Clica no baú do Benefício Valquíria
    FS.mover_e_clicar(coord_x[1], coord_y[1], tempo[1])

    # Clica em Coletar
    FS.mover_e_clicar(coord_x[2], coord_y[2], tempo[2])

    # Clica no X do Benefício da Valquíria
    FS.mover_e_clicar(coord_x[3], coord_y[3], tempo[3])

    # Clica no X do Dirigível
    FS.mover_e_clicar(coord_x[4], coord_y[4], tempo[4])


def configurar_coordenadas():
    caminho_pasta = 'Configuracoes/Coordenadas/Coordenadas_Teste'
    caminho_arquivo = f'{caminho_pasta}/Dirigivel.txt'
    time_sleeps = ['3', '2', '2', '1', '1']

    # Cria o diretório se ele não existir
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)

    coordenadas_x = []
    coordenadas_y = []

    print("\nClique no Dirigível")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique no baú do Benefício Valquíria")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique em Coletar")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique no X do Benefício da Valquíria")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique no X do Dirigível")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    # Escreve as coordenadas em um arquivo
    with open(caminho_arquivo, 'w') as arquivo:
        for i in range(len(coordenadas_x)):
            arquivo.write(f"{coordenadas_x[i]}, {coordenadas_y[i]}, {time_sleeps[i]}\n")

    print("Coordenadas foram salvas em", caminho_arquivo)