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
    print('\nEscolha uma das opções:\n1 - Criar rotina\n2 - Escolher rotina\n')
    escolha = input('Opção escolhida: ').strip()

    if escolha == "1":
        Rotina.cria_rotina()
    elif escolha == "2":
        dadosRotina = Rotina.escolhe_rotina()
        executa_rotina(dadosRotina)
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
    Arena.batalhar()


def grande_arena():
    Grande_Arena.pegar_recompensa()


def vidente_astral():
    Vidente_Astral.completar_uma_vez()


def presentes():
    Presentes.presentear()


def dirigivel():
    Dirigivel.pegar_recompensa_valquiria()


def terralem():
    Terralem.pegar_recompensas()


def masmorra():
    Masmorra.percorrer_masmorra()


def atrio_animico():
    Atrio_Animico.resgatar_recompensa()


def torre():
    Torre.completar_torre()





def mensagens():
    Mensagens.coletar_mensagens()


def eventos_especiais():
    Eventos_Especiais.coletar_recompensas_imutaveis()

def missoes_diarias():
    Missoes_Diarias.coletar_diarias()