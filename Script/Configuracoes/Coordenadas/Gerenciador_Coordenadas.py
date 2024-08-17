import Componentes_Hero_Wars.Atrio_Animico.atrio_animico as Atrio_Animico
import Util.funcoes_suporte as FS
import os

def pegar_coordenadas(nome_arquivo):
    caminhoArquivo = f'Configuracoes/Coordenadas/Arquivos_Coordenadas/{nome_arquivo}'

    coord_x = []
    coord_y = []
    tempo = []

    with open(caminhoArquivo, 'r') as arquivo:
        for linha in arquivo:
            valores = linha.strip().split(', ')
            if len(valores) == 3:
                coord_x.append(int(valores[0]))
                coord_y.append(int(valores[1]))
                tempo.append(int(valores[2]))

    return coord_x, coord_y, tempo


def configurar_coordenadas():
    print("\nVamos começar configurando as coordenadas do Atrio Animico")
    Atrio_Animico.configurar_atrio_animico()


