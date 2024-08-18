import Configuracoes.rotina as Rotina
import Componentes_Hero_Wars.Arena.arena as Arena
import Componentes_Hero_Wars.Vidente_Astral.vidente_astral as Vidente_Astral
import Componentes_Hero_Wars.Presentes.presentes as Presentes
import Componentes_Hero_Wars.Dirigivel.dirigivel as Dirigivel
import Componentes_Hero_Wars.Grande_Arena.grande_arena as Grande_Arena
import Componentes_Hero_Wars.Terralem.terralem as Terralem
import Componentes_Hero_Wars.Masmorra.masmorra as Masmorra
import Componentes_Hero_Wars.Atrio_Animico.atrio_animico as Atrio_Animico
import Componentes_Hero_Wars.Torre.torre as Torre
import Componentes_Hero_Wars.Mensagens.mensagens as Mensagens
import Componentes_Hero_Wars.Eventos_Especiais.eventos_especiais as Eventos_Especiais
import Componentes_Hero_Wars.Missoes_Diarias.missoes_diarias as Missoes_Diarias

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
    print('\nEscolha uma das opções:\n1 - Configurar todas as coordenadas' +
    '\n2 - Configurar coordenada especifica')
    escolha = input('Opção escolhida: ').strip()

    tarefas = [    
        'arena',
        'grande_arena',
        'vidente_astral',
        'presentes',
        'dirigivel',
        'terralem',
        'atrio_animico',
        'torre',
        'masmorra',
        'mensagens',
        'eventos_especiais',
        'missoes_diarias'
    ]

    if escolha == "1":
        configurar_coordenadas_completo()
    elif escolha == "2":
        print('\nEscolha uma das tarefas para configurar:')
        Rotina.mostrar_tarefas(tarefas)
        escolha = input('Tarefa escolhida: ').strip()
        configurar_coordenada_especifica(escolha)


def configurar_coordenadas_completo():
    print("\nVamos começar configurando as coordenadas do Atrio Animico")
    Atrio_Animico.configurar_coordenadas()

    print('\n------------------------------------------------------------' +
        '----------------------------------------------------------------')

    print("\nAgora a configuração das coordenadas do Dirigivel")
    Dirigivel.configurar_coordenadas()


def configurar_coordenada_especifica(tarefa):
    switch = {
        '0': arena,
        '1': grande_arena,
        '2': vidente_astral,
        '3': presentes,
        '4': dirigivel,
        '5': terralem,
        '6': atrio_animico,
        '7': torre,
        '8': masmorra,
        '9': mensagens,
        '10': eventos_especiais,
        '11': missoes_diarias
    }

    funcao = switch.get(tarefa)

    if funcao:
        funcao()  # Chama a função associada à escolha

def arena():
    print("\nVamos configurar as coordenadas da Arena")
    #Arena.configurar_coordenadas()


def grande_arena():
    print("\nVamos configurar as coordenadas da Grande Arena")
    Grande_Arena.configurar_coordenadas()


def vidente_astral():
    print("\nVamos configurar as coordenadas do Vidente Astral")
    #Vidente_Astral.configurar_coordenadas()


def presentes():
    print("\nVamos configurar as coordenadas dos Presentes")
    #Presentes.configurar_coordenadas()


def dirigivel():
    print("\nVamos configurar as coordenadas do Dirigivel")
    Dirigivel.configurar_coordenadas()


def terralem():
    print("\nVamos configurar as coordenadas do Terralem")
    #Terralem.configurar_coordenadas()


def masmorra():
    print("\nVamos configurar as coordenadas da Masmorra")
    #Masmorra.configurar_coordenadas()


def atrio_animico():
    print("\nVamos configurar as coordenadas do Atrio Animico")
    Atrio_Animico.configurar_coordenadas()


def torre():
    print("\nVamos configurar as coordenadas da Torre")
    #Torre.configurar_coordenadas()


def mensagens():
    print("\nVamos configurar as coordenadas das Mensagens")
    #Mensagens.configurar_coordenadas()


def eventos_especiais():
    print("\nVamos configurar as coordenadas dos Eventos Especiais")
    Eventos_Especiais.configurar_coordenadas()


def missoes_diarias():
    print("\nVamos configurar as coordenadas das Missões Diárias")
    #Missoes_Diarias.configurar_coordenadas()