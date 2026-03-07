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
import Util.funcoes_suporte as Funcoes_Suporte
import time
import threading
import sys

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

def formatar_tempo(segundos):
    """Converte segundos em MM:SS"""
    m = int(segundos // 60)
    s = int(segundos % 60)
    return f"{m:02d}:{s:02d}"

def monitorar_tarefa(nome_tarefa, funcao_executavel, inicio_rotina_global=None):
    """
    Executa uma tarefa e mostra um timer rodando em tempo real no terminal.
    Se inicio_rotina_global for passado, mostra também o tempo total da rotina.
    """
    print(f"\n>>> Iniciando: {nome_tarefa.upper()}")
    
    inicio_tarefa = time.time()
    evento_parar = threading.Event()

    # --- Função que roda em paralelo (Thread) ---
    def _timer_visual():
        while not evento_parar.is_set():
            agora = time.time()
            tempo_tarefa = agora - inicio_tarefa
            str_tarefa = formatar_tempo(tempo_tarefa)
            
            msg = f"\r   [⏳ EXECUTANDO] {nome_tarefa}: {str_tarefa}"
            
            # Se estiver rodando numa rotina, mostra o tempo total acumulado
            if inicio_rotina_global:
                tempo_total = agora - inicio_rotina_global
                str_total = formatar_tempo(tempo_total)
                msg += f" | 🌍 Tempo Total Rotina: {str_total}"
            
            # Imprime sobrescrevendo a linha (\r) e flush forçado
            sys.stdout.write(msg)
            sys.stdout.flush()
            
            # Atualiza a cada 0.5 segundos (menos que isso pisca demais)
            time.sleep(0.5)

    # Inicia a thread do relógio
    t = threading.Thread(target=_timer_visual)
    t.start()
    
    # Executa a tarefa real (Bot)
    try:
        funcao_executavel()
    except Exception as e:
        print(f"\n[ERRO] Falha ao executar {nome_tarefa}: {e}")
    finally:
        # Garante que o timer pare, mesmo se der erro
        evento_parar.set()
        t.join() # Espera a thread fechar
    
    fim = time.time()
    duracao = fim - inicio_tarefa
    
    # Limpa a linha do timer e mostra o OK final
    # Os espaços em branco no final servem para apagar restos de texto da linha anterior
    print(f"\r[✅ OK] {nome_tarefa.upper()} finalizada em {duracao:.2f}s." + " "*20)
    return duracao

def menu():
    while True: # Loop para o menu não fechar após uma ação
        print('\n' + '='*30)
        print('   HERO WARS BOT')
        print('='*30)
        print('1 - Criar rotina')
        print('2 - Escolher rotina')
        print('3 - Fazer tarefa especifica')
        print('4 - Configurar coordenadas')
        print('5 - Verificar coordenadas')
        print('6 - Verificar cor da posição')
        print('0 - Sair')
        
        escolha = input('\nOpção: ').strip()

        if escolha == "1":
            Rotina.cria_rotina(LISTA_TAREFAS)
        elif escolha == "2":
            dadosRotina = Rotina.escolhe_rotina()
            if dadosRotina:
                executa_rotina(dadosRotina)
        elif escolha == "3":
            Rotina.mostrar_tarefas(LISTA_TAREFAS)
            try:
                idx = input('Número da Tarefa: ').strip()
                executa_tarefa(idx)
            except ValueError:
                print("Entrada inválida.")
        elif escolha == "4":
            Gerenciador_Coordenadas.configurar_coordenadas()
        elif escolha == "5":
            Gerenciador_Coordenadas.verificar_coordenadas()
        elif escolha == "6":
            Funcoes_Suporte.capturar_posicao_cor()
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

def executa_rotina(dadosRotina):
    dadosFiltrados = [item for item in dadosRotina if item]
    
    qtd_tarefas = len(dadosFiltrados)
    print(f"\n{'#'*50}")
    print(f"   INICIANDO ROTINA COM {qtd_tarefas} TAREFAS")
    print(f"{'#'*50}")
    
    inicio_rotina = time.time()
    
    # Separa a Arena do resto das tarefas
    tem_arena = '0' in dadosFiltrados
    tarefas_pendentes = [t for t in dadosFiltrados if t != '0']
    
    # A SUA LISTA DE PRIORIDADES (Do mais demorado para o mais rápido)
    ordem_prioridade = ['8', '7', '2', '5', '4', '6', '1', '3', '10', '9', '11', '12']
    
    # Ordena a lista de tarefas pendentes baseada na régua de prioridade.
    # Tarefas longas ficam no começo [0], tarefas curtas vão pro final da fila.
    tarefas_pendentes.sort(key=lambda x: ordem_prioridade.index(x) if x in ordem_prioridade else 99)

    # === MODO ASSÍNCRONO (INTERCALAÇÃO COM ARENA) ===
    if tem_arena:
        print("\n[MODO INTERCALAÇÃO ATIVADO] Arena detectada. Organizando fila por peso de tempo...")
        coord_x, coord_y, tempo_arena = Gerenciador_Coordenadas.pegar_coordenadas('Arena.txt')
        cooldown_alvo = float(tempo_arena[5]) # Ex: os 47 segundos
        
        for luta in range(5):
            print(f"\n--- Arena: Luta {luta+1}/5 ---")
            
            # Executa a luta e devolve o controle IMEDIATAMENTE (1s)
            Arena.fazer_uma_luta_e_sair(coord_x, coord_y, tempo_arena, pular_tempo=1)
            
            # Gerenciamento do Cooldown (Apenas nas 4 primeiras lutas)
            if luta < 4:
                inicio_cooldown = time.time()
                
                # Se ainda tem tarefas pendentes, puxa A PRIMEIRA da fila (que agora é a mais demorada)
                if tarefas_pendentes:
                    proxima_tarefa = tarefas_pendentes.pop(0)
                    nome_proxima = LISTA_TAREFAS[int(proxima_tarefa)]
                    print(f" -> Aproveitando Cooldown para executar: {nome_proxima}")
                    
                    executa_tarefa(proxima_tarefa, inicio_rotina_global=inicio_rotina)
                else:
                    print(" -> Nenhuma tarefa extra pendente. Apenas aguardando o tempo passar.")
                
                # Matemática do tempo
                tempo_gasto = time.time() - inicio_cooldown
                tempo_restante = cooldown_alvo - tempo_gasto
                
                if tempo_restante > 0:
                    print(f" -> Aguardando {tempo_restante:.1f}s restantes do cooldown da Arena...")
                    time.sleep(tempo_restante)
                else:
                    print(f" -> O tempo da tarefa extra superou o cooldown. Voltando para a Arena imediatamente!")

    # === MODO NORMAL (TAREFAS QUE SOBRARAM) ===
    if tarefas_pendentes:
        if tem_arena:
            print("\n[FINALIZANDO FILA] Executando tarefas que sobraram pós-Arena...")
            
        for tarefa in tarefas_pendentes:
            nome_tarefa = LISTA_TAREFAS[int(tarefa)]
            print(f"\n--- Executando: {nome_tarefa} ---")
            executa_tarefa(tarefa, inicio_rotina_global=inicio_rotina)

    # === FINALIZAÇÃO ===
    tempo_total = time.time() - inicio_rotina
    str_total = formatar_tempo(tempo_total)

    print(f"\n{'#'*50}")
    print(f"   ROTINA FINALIZADA")
    print(f"   Tempo Total: {str_total} ({tempo_total:.2f}s)")
    print(f"{'#'*50}\n")


def executa_tarefa(tarefa_index_str, inicio_rotina_global=None):
    """
    Agora aceita o parametro opcional inicio_rotina_global
    """
    switch = {
        '0': arena, '1': grande_arena, '2': vidente_astral, '3': presentes,
        '4': dirigivel, '5': terralem, '6': atrio_animico, '7': torre,
        '8': masmorra, '9': mensagens, '10': eventos_especiais,
        '11': missoes_diarias, '12': missoes_guilda
    }

    funcao = switch.get(tarefa_index_str)

    if funcao:
        try:
            nome_da_tarefa = LISTA_TAREFAS[int(tarefa_index_str)]
        except:
            nome_da_tarefa = "Tarefa Desconhecida"

        # Passamos o tempo global adiante
        return monitorar_tarefa(nome_da_tarefa, funcao, inicio_rotina_global)
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

if __name__ == "__main__":
    menu()