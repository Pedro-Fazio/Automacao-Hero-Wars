import Configuracoes.rotina as Rotina
import Componentes_Hero_Wars.Atrio_Animico.atrio_animico as Atrio_Animico
import Componentes_Hero_Wars.Dirigivel.dirigivel as Dirigivel

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
    print('Não feito ainda.')


def grande_arena():
    print('Não feito ainda.')


def vidente_astral():
    print('Não feito ainda.')


def presentes():
    print('Não feito ainda.')


def dirigivel():
    print("\nVamos começar configurando as coordenadas do Dirigivel")
    Dirigivel.configurar_coordenadas()


def terralem():
    print('Não feito ainda.')


def masmorra():
    print('Não feito ainda.')


def atrio_animico():
    print("\nVamos começar configurando as coordenadas do Atrio Animico")
    Atrio_Animico.configurar_coordenadas()


def torre():
    print('Não feito ainda.')


def mensagens():
    print('Não feito ainda.')


def eventos_especiais():
    print('Não feito ainda.')


def missoes_diarias():
    print('Não feito ainda.')