import Configuracoes.Coordenadas.Gerenciador_Coordenadas as Gerenciador_Coordenadas
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

def menu():
    print('\nEscolha uma das opções:\n1 - Criar rotina\n2 - Escolher rotina\n' +
    '3 - Fazer tarefa especifica\n4 - Configurar coordenadas')
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
        Rotina.cria_rotina(tarefas)
    elif escolha == "2":
        dadosRotina = Rotina.escolhe_rotina()
        executa_rotina(dadosRotina)
    elif escolha == "3":
        Rotina.mostrar_tarefas(tarefas)
        escolha = input('Tarefa escolhida: ').strip()
        executa_tarefa(escolha)
    elif escolha == "4":
        Gerenciador_Coordenadas.configurar_coordenadas()
    else:
        print("Opção inválida. Tente novamente.")

def executa_rotina(dadosRotina):
    dadosFiltrados = [item for item in dadosRotina if item]

    for dado in dadosFiltrados:
        executa_tarefa(dado)


def executa_tarefa(tarefa):
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
    coord_x, coord_y, tempo = Gerenciador_Coordenadas.pegar_coordenadas('Arena.txt')
    Arena.batalhar(coord_x, coord_y, tempo)


def grande_arena():
    coord_x, coord_y, tempo = Gerenciador_Coordenadas.pegar_coordenadas('Grande_Arena.txt')
    Grande_Arena.pegar_recompensa(coord_x, coord_y, tempo)


def vidente_astral():
    coord_x, coord_y, tempo = Gerenciador_Coordenadas.pegar_coordenadas('Vidente_Astral.txt')
    Vidente_Astral.completar_uma_vez(coord_x, coord_y, tempo)


def presentes():
    coord_x, coord_y, tempo = Gerenciador_Coordenadas.pegar_coordenadas('Presentes.txt')
    Presentes.presentear(coord_x, coord_y, tempo)


def dirigivel():
    coord_x, coord_y, tempo = Gerenciador_Coordenadas.pegar_coordenadas('Dirigivel.txt')
    Dirigivel.pegar_recompensa_valquiria(coord_x, coord_y, tempo)


def terralem():
    coord_x, coord_y, tempo = Gerenciador_Coordenadas.pegar_coordenadas('Terralem.txt')
    Terralem.pegar_recompensas(coord_x, coord_y, tempo)


def masmorra():
    coord_x, coord_y, tempo = Gerenciador_Coordenadas.pegar_coordenadas('Masmorra.txt')
    Masmorra.percorrer_masmorra(coord_x, coord_y, tempo)


def atrio_animico():
    coord_x, coord_y, tempo = Gerenciador_Coordenadas.pegar_coordenadas('Atrio_Animico.txt')
    Atrio_Animico.resgatar_recompensa(coord_x, coord_y, tempo)


def torre():
    coord_x, coord_y, tempo = Gerenciador_Coordenadas.pegar_coordenadas('Torre.txt')
    Torre.completar_torre(coord_x, coord_y, tempo)


def mensagens():
    coord_x, coord_y, tempo = Gerenciador_Coordenadas.pegar_coordenadas('Mensagens.txt')
    Mensagens.coletar_mensagens(coord_x, coord_y, tempo)


def eventos_especiais():
    coord_x, coord_y, tempo = Gerenciador_Coordenadas.pegar_coordenadas('Eventos_Especiais.txt')
    Eventos_Especiais.coletar_recompensas_imutaveis(coord_x, coord_y, tempo)


def missoes_diarias():
    coord_x, coord_y, tempo = Gerenciador_Coordenadas.pegar_coordenadas('Missoes_Diarias.txt')
    Missoes_Diarias.coletar_diarias(coord_x, coord_y, tempo)