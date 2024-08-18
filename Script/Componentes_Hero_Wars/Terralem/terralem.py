import Util.funcoes_suporte as FS
import os

def pegar_recompensas(coord_x, coord_y, tempo):
    # Clica em Terralém
    FS.mover_e_clicar(coord_x[0], coord_y[0], tempo[0])

    _abrir_bau(coord_x, coord_y, tempo)

    # Clica no próximo chefe
    FS.mover_e_clicar(coord_x[5], coord_y[5], tempo[5])

    _abrir_bau(coord_x, coord_y, tempo)

    # Clica no próximo chefe
    FS.mover_e_clicar(coord_x[6], coord_y[6], tempo[6])

    _abrir_bau(coord_x, coord_y, tempo)

    # Clica no X do Terralém
    FS.mover_e_clicar(coord_x[7], coord_y[7], tempo[7])


def _abrir_bau(coord_x, coord_y, tempo):
    # Clica em Abrir Baús
    FS.mover_e_clicar(coord_x[1], coord_y[1], tempo[1])

    # Clica em Abrir
    FS.mover_e_clicar(coord_x[2], coord_y[2], tempo[2])

    # Clica no X do janela do baú aberto
    FS.mover_e_clicar(coord_x[3], coord_y[3], tempo[3])

    # Clica no X da janela Abrir Baús
    FS.mover_e_clicar(coord_x[4], coord_y[4], tempo[4])


def configurar_coordenadas():
    caminho_pasta = 'Configuracoes/Coordenadas/Coordenadas_Teste'
    caminho_arquivo = f'{caminho_pasta}/Terralem.txt'
    time_sleeps = ['2', '2', '3', '1', '1', '1', '1', '1']

    # Cria o diretório se ele não existir
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)

    coordenadas_x = []
    coordenadas_y = []

    print("\nClique em Terralém")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique em Abrir Baús")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique em Abrir")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique no X do janela do baú aberto")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique no X da janela Abrir Baús")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique no próximo chefe (Vadjar)")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique no outro próximo chefe (Ilyssa)")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique no X do Terralém")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    # Escreve as coordenadas em um arquivo
    with open(caminho_arquivo, 'w') as arquivo:
        for i in range(len(coordenadas_x)):
            arquivo.write(f"{coordenadas_x[i]}, {coordenadas_y[i]}, {time_sleeps[i]}\n")

    print("Coordenadas foram salvas em", caminho_arquivo)