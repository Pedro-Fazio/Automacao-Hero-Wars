import Util.funcoes_suporte as FS
import os

def presentear(coord_x, coord_y, tempo):
    # Clica em Presentes
    FS.mover_e_clicar(coord_x[0], coord_y[0], tempo[0])

    # Clica em Enviar
    FS.mover_e_clicar(coord_x[1], coord_y[1], tempo[1])

    # Envia os presentes
    FS.mover_e_clicar(coord_x[2], coord_y[2], tempo[2])

    # Fecha tela de envio dos presentes
    FS.mover_e_clicar(coord_x[3], coord_y[3], tempo[3])

    # Fecha tela de Presentes
    FS.mover_e_clicar(coord_x[4], coord_y[4], tempo[4])


def configurar_coordenadas():
    caminho_pasta = 'Configuracoes/Coordenadas/Coordenadas_Teste'
    caminho_arquivo = f'{caminho_pasta}/Presentes.txt'
    time_sleeps = ['2', '1', '1', '1', '1']

    # Cria o diretório se ele não existir
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)

    coordenadas_x = []
    coordenadas_y = []

    print("\nClique em Presentes")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nClique em Enviar")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nEnvie os presentes")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nFeche tela de envio dos presentes")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    print("\nFeche a tela de Presentes")
    x, y = FS.captura_clique_coordenadas()
    coordenadas_x.append(x)
    coordenadas_y.append(y)

    # Escreve as coordenadas em um arquivo
    with open(caminho_arquivo, 'w') as arquivo:
        for i in range(len(coordenadas_x)):
            arquivo.write(f"{coordenadas_x[i]}, {coordenadas_y[i]}, {time_sleeps[i]}\n")

    print(f"Coordenadas foram salvas em {caminho_arquivo}\n")