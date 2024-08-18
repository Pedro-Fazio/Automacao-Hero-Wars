import Util.funcoes_suporte as FS
import os

def resgatar_recompensa(coord_x, coord_y, tempo):
    # Clica no Átrio Anímico
    FS.mover_e_clicar(coord_x[0], coord_y[0], tempo[0])

    # Clica em Resgatar
    FS.mover_e_clicar(coord_x[1], coord_y[1], tempo[1])

    # Clica em Invocar
    FS.mover_e_clicar(coord_x[2], coord_y[2], tempo[2])

    # Clica na tela para pular animação de invocação
    FS.mover_e_clicar(coord_x[3], coord_y[3], tempo[3])

    # Clica em Ótimo!
    FS.mover_e_clicar(coord_x[4], coord_y[4], tempo[4])

    # Clica no X do Átrio Anímico
    FS.mover_e_clicar(coord_x[5], coord_y[5], tempo[5])


def configurar_coordenadas():
    caminho_pasta = 'Configuracoes/Coordenadas/Coordenadas_Teste'
    caminho_arquivo = f'{caminho_pasta}/Atrio_Animico.txt'
    time_sleeps = ['3', '1', '1', '3', '2', '1']

    # Cria o diretório se ele não existir
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)

    coordenadas_x = []
    coordenadas_y = []

    print("\nClique no Átrio Anímico")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique em Resgatar")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique em Invocar")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique na tela para pular animação de invocação")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique em Ótimo!")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique no X do Átrio Anímico")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    # Escreve as coordenadas em um arquivo
    with open(caminho_arquivo, 'w') as arquivo:
        for i in range(len(coordenadas_x)):
            arquivo.write(f"{coordenadas_x[i]}, {coordenadas_y[i]}, {time_sleeps[i]}\n")

    print("Coordenadas foram salvas em", caminho_arquivo)