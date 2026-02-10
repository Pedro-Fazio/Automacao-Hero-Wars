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
import Componentes_Hero_Wars.Missoes_Guilda.missoes_guilda as Missoes_Guilda
import time

# --- LISTA DE TAREFAS (Global para ser usada no menu e na execução) ---
LISTA_TAREFAS = [
    'Arena',
    'Grande Arena',
    'Vidente Astral',
    'Presentes',
    'Dirigivel',
    'Terralem',
    'Atrio Animico',
    'Torre',
    'Masmorra',
    'Mensagens',
    'Eventos Especiais',
    'Missoes Diarias',
    'Missoes Guilda'
]


def monitorar_tarefa(nome_tarefa, funcao_executavel):
    """Executa uma tarefa e cronometra o tempo gasto."""
    print(f"\n[INFO] Iniciando tarefa: {nome_tarefa.upper()}")
    # print(f"Timer: Executando...", end="", flush=True) 
    
    inicio = time.time()
    
    # Executa a função da tarefa (ex: arena(), masmorra())
    try:
        funcao_executavel()
    except Exception as e:
        print(f"\n[ERRO] Falha ao executar {nome_tarefa}: {e}")
    
    fim = time.time()
    duracao = fim - inicio
    
    # O \r faz voltar para o inicio da linha, substituindo o texto anterior se houver
    print(f"[OK] {nome_tarefa.upper()} finalizada em {duracao:.2f} segundos.")
    return duracao


def menu():
    print('\nEscolha uma das opções:\n1 - Criar rotina\n2 - Escolher rotina\n' +
    '3 - Fazer tarefa especifica\n4 - Configurar coordenadas\n5 - Verificar coordenadas')
    escolha = input('Opção escolhida: ').strip()

    if escolha == "1":
        Rotina.cria_rotina(LISTA_TAREFAS)
    elif escolha == "2":
        dadosRotina = Rotina.escolhe_rotina()
        executa_rotina(dadosRotina)
    elif escolha == "3":
        Rotina.mostrar_tarefas(LISTA_TAREFAS)
        escolha = input('Tarefa escolhida: ').strip()
        executa_tarefa(escolha)
    elif escolha == "4":
        Gerenciador_Coordenadas.configurar_coordenadas()
    elif escolha == "5":
        Gerenciador_Coordenadas.verificar_coordenadas()
    else:
        print("Opção inválida. Tente novamente.")


def executa_rotina(dadosRotina):
    # Remove linhas vazias
    dadosFiltrados = [item for item in dadosRotina if item]
    
    tempo_total = 0
    print(f"\n{'='*40}")
    print(f"INICIANDO ROTINA COM {len(dadosFiltrados)} TAREFAS")
    print(f"{'='*40}")

    for dado in dadosFiltrados:
        tempo_total += executa_tarefa(dado)

    minutos = int(tempo_total // 60)
    segundos = int(tempo_total % 60)

    print(f"\n{'='*40}")
    print(f"ROTINA COMPLETA FINALIZADA")
    print(f"Tempo Total: {minutos}m {segundos}s ({tempo_total:.2f}s)")
    print(f"{'='*40}\n")


def executa_tarefa(tarefa_index_str):
    """
    Recebe o index da tarefa (string '0', '1', etc), descobre o nome
    e executa com monitoramento de tempo.
    """
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
        '11': missoes_diarias,
        '12': missoes_guilda
    }

    funcao = switch.get(tarefa_index_str)

    if funcao:
        # Pega o nome da lista global usando o index
        try:
            nome_da_tarefa = LISTA_TAREFAS[int(tarefa_index_str)]
        except:
            nome_da_tarefa = "Tarefa Desconhecida"

        # Chama o monitorador e retorna o tempo gasto
        return monitorar_tarefa(nome_da_tarefa, funcao)
    else:
        print(f"Tarefa {tarefa_index_str} não encontrada.")
        return 0



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
    #Masmorra.percorrer_masmorra(coord_x, coord_y, tempo)
    Masmorra.percorrer_masmorra_teste_calibrador()

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
    
def missoes_guilda():
    coord_x, coord_y, tempo = Gerenciador_Coordenadas.pegar_coordenadas('Missoes_Guilda.txt')
    Missoes_Guilda.coletar_missoes_guilda(coord_x, coord_y, tempo)