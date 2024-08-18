import Util.funcoes_suporte as FS
import os

def batalhar(coord_x, coord_y, tempo):
    # Clica na Arena
    FS.mover_e_clicar(coord_x[0], coord_y[0], tempo[0])

    for _ in range(5):
        _lutar_uma_vez(coord_x, coord_y, tempo)

    # Clica no X da Arena
    FS.mover_e_clicar(coord_x[4], coord_y[4], tempo[4])



def _lutar_uma_vez(coord_x, coord_y, tempo):
    # Clica para atacar o primeiro jogador
    FS.mover_e_clicar(coord_x[1], coord_y[1], tempo[1])

    # Clica em Para a Batalha!
    FS.mover_e_clicar(coord_x[2], coord_y[2], tempo[2])

    # Clica em OK
    FS.mover_e_clicar(coord_x[3], coord_y[3], tempo[3])


def configurar_coordenadas():
    caminho_pasta = 'Configuracoes/Coordenadas/Coordenadas_Teste'
    caminho_arquivo = f'{caminho_pasta}/Arena.txt'
    time_sleeps = ['3', '2', '130', '1', '1']

    # Cria o diretório se ele não existir
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)

    coordenadas_x = []
    coordenadas_y = []

    print("\nClique na Arena")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique para atacar o primeiro jogador")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique em Para a Batalha!")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nEspere a luta terminar e então clique em OK")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique no X da Arena")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    # Escreve as coordenadas em um arquivo
    with open(caminho_arquivo, 'w') as arquivo:
        for i in range(len(coordenadas_x)):
            arquivo.write(f"{coordenadas_x[i]}, {coordenadas_y[i]}, {time_sleeps[i]}\n")

    print("Coordenadas foram salvas em", caminho_arquivo)
