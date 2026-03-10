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
import Configuracoes.interface as interface
import sys
import pyautogui as PY

LISTA_TAREFAS = [
    'Arena', 'Grande Arena', 'Vidente Astral', 'Presentes',
    'Dirigivel', 'Terralem', 'Atrio Animico', 'Torre',
    'Masmorra', 'Mensagens', 'Eventos Especiais', 
    'Missoes Diarias', 'Missoes Guilda'
]

def monitorar_tarefa(nome_tarefa, funcao_executavel, inicio_rotina_global=None, tempo_acumulado_inicial=0.0, mostrar_ok_final=True):
    """
    Executa a tarefa mostrando um spinner profissional e o tempo rodando.
    Possui suporte para pausar e retomar tempos (Cronômetro Acumulativo).
    """
    inicio_tarefa = time.time()
    evento_parar = threading.Event()

    with interface.console.status(f"[bold cyan]Preparando {nome_tarefa}...[/]", spinner="bouncingBar") as status:
        
        def _atualizar_status():
            while not evento_parar.is_set():
                agora = time.time()
                
                # O tempo total é o que já passou ANTES + o que está passando AGORA
                tempo_tarefa = tempo_acumulado_inicial + (agora - inicio_tarefa)
                str_tarefa = interface.formatar_tempo(tempo_tarefa)
                
                msg = f"[bold cyan]Executando {nome_tarefa}[/]: {str_tarefa}"
                
                if inicio_rotina_global:
                    str_total = interface.formatar_tempo(agora - inicio_rotina_global)
                    msg += f" | [magenta]Tempo Total: {str_total}[/]"
                
                status.update(msg)
                time.sleep(0.5)

        t = threading.Thread(target=_atualizar_status)
        t.start()
        
        try:
            funcao_executavel()
        except Exception as e:
            interface.console.print(f"\n[bold red]ERRO ao executar {nome_tarefa}:[/] {e}")
        finally:
            evento_parar.set()
            t.join() 
    
    # Calcula a duração exata desta sessão e soma com o histórico
    duracao_sessao = time.time() - inicio_tarefa
    duracao_total = tempo_acumulado_inicial + duracao_sessao
    
    # Só exibe o check verde se a tarefa acabou de verdade
    if mostrar_ok_final:
        interface.console.print(f"[bold green]✔ {nome_tarefa.upper()}[/] finalizada em {duracao_total:.2f}s.")
        
    return duracao_total

def menu():
    while True:
        interface.desenhar_cabecalho()
        interface.desenhar_menu_principal()

        resposta_usuario = [None] 

        def capturar_input():
            resposta_usuario[0] = interface.console.input('\n[bold yellow]Opção (20s para encerrar): [/]').strip()

        # Criamos a "Thread Fantasma"
        thread_espera = threading.Thread(target=capturar_input)
        thread_espera.daemon = True # Thread morre se o programa principal fechar
        thread_espera.start()
        thread_espera.join(timeout=20.0)

        # Verifica se deu o timeout e encerra o programa
        if thread_espera.is_alive():
            PY.press('0')
            interface.console.print("\n\n[bold red]⏳ Tempo limite atingido (20 segundos). O bot será encerrado...[/]")
            PY.press('enter')
            return

        # Se passou direto pelo if, significa que o usuário digitou algo a tempo
        escolha = resposta_usuario[0]

        if escolha == "1":
            Rotina.cria_rotina(LISTA_TAREFAS)
        elif escolha == "2":
            dadosRotina = Rotina.escolhe_rotina()
            if dadosRotina:
                executa_rotina(dadosRotina)
        elif escolha == "3":
            Rotina.mostrar_tarefas(LISTA_TAREFAS)
            try:
                idx = interface.console.input('[bold yellow]Número da Tarefa: [/]').strip()
                executa_tarefa(idx)
            except ValueError:
                interface.console.print("[red]Entrada inválida.[/red]")
        elif escolha == "4":
            Gerenciador_Coordenadas.configurar_coordenadas()
        elif escolha == "5":
            Gerenciador_Coordenadas.verificar_coordenadas()
        elif escolha == "6":
            Funcoes_Suporte.capturar_posicao_cor()
        elif escolha == "0":
            interface.console.print("[bold red]Encerrando os motores...[/]")
            break
        else:
            interface.console.print("[red]Opção inválida.[/red]")
            time.sleep(1)

def executa_rotina(dadosRotina):
    dadosFiltrados = [item for item in dadosRotina if item]
    qtd_tarefas = len(dadosFiltrados)
    
    print("\n")
    interface.mostrar_painel_info(
        "GERENCIADOR DE ROTINA", 
        f"Iniciando sequência com [bold white]{qtd_tarefas}[/] tarefas.", 
        cor="magenta"
    )
    
    inicio_rotina = time.time()
    tem_arena = '0' in dadosFiltrados
    tarefas_pendentes = [t for t in dadosFiltrados if t != '0']
    
    ordem_prioridade = ['8', '2', '5', '4', '7', '6', '1', '3', '10', '9', '11', '12']
    tarefas_pendentes.sort(key=lambda x: ordem_prioridade.index(x) if x in ordem_prioridade else 99)

    # === MODO ASSÍNCRONO ARENA ===
    if tem_arena:
        interface.console.print("\n[bold yellow]⚡ MODO INTERCALAÇÃO ATIVADO[/] - Arena detectada. Organizando fila...")
        coord_x, coord_y, tempo_arena = Gerenciador_Coordenadas.pegar_coordenadas('Arena.txt')
        cooldown_alvo = float(tempo_arena[5])
        
        tempo_acumulado_arena = 0.0 
        
        for luta in range(5):
            interface.console.print(f"\n[bold blue]--- Arena: Luta {luta+1}/5 ---[/]")
            
            tempo_acumulado_arena = monitorar_tarefa(
                "Arena (Ataque)", 
                lambda: Arena.fazer_uma_luta_e_sair(coord_x, coord_y, tempo_arena, pular_tempo=1),
                inicio_rotina_global=inicio_rotina,
                tempo_acumulado_inicial=tempo_acumulado_arena,
                mostrar_ok_final=False
            )
            
            if luta < 4:
                inicio_cooldown = time.time()
                
                # Executa a tarefa secundária
                if tarefas_pendentes:
                    proxima_tarefa = tarefas_pendentes.pop(0)
                    nome_proxima = LISTA_TAREFAS[int(proxima_tarefa)]

                    interface.console.print(f" [dim]-> Aproveitando Cooldown para:[/] [bold]{nome_proxima}[/]")
                    executa_tarefa(proxima_tarefa, inicio_rotina_global=inicio_rotina)
                else:
                    interface.console.print(" [dim]-> Nenhuma tarefa extra pendente. Aguardando...[/]")
                
                tempo_gasto_recheio = time.time() - inicio_cooldown
                tempo_restante = cooldown_alvo - tempo_gasto_recheio
                
                if tempo_restante > 0:
                    interface.console.print(f" [dim]-> Pausa para completar o cooldown da Arena...[/]")
                    interface.exibir_countdown(tempo_restante, "⏳ Cooldown da Arena")
                    tempo_acumulado_arena += tempo_restante    
                else:
                    interface.console.print(f" [bold red]-> O tempo superou o cooldown. Voltando para a Arena![/]")

        interface.console.print(f"[bold green]✔ ARENA[/] finalizada. Tempo exclusivo da tarefa: {tempo_acumulado_arena:.2f}s.")

    # === MODO NORMAL ===
    if tarefas_pendentes:
        if tem_arena:
            interface.console.print("\n[bold yellow]🚩 FINALIZANDO FILA[/] - Executando tarefas restantes...")
            
        for tarefa in tarefas_pendentes:
            nome_tarefa = LISTA_TAREFAS[int(tarefa)]
            interface.console.print(f"\n[bold blue]--- Executando: {nome_tarefa} ---[/]")
            executa_tarefa(tarefa, inicio_rotina_global=inicio_rotina)

    # === FINALIZAÇÃO ===
    tempo_total = time.time() - inicio_rotina
    str_total = interface.formatar_tempo(tempo_total)

    print("\n")
    interface.mostrar_painel_info(
        "ROTINA FINALIZADA", 
        f"Todas as tarefas foram concluídas.\nTempo Total: [bold green]{str_total}[/] ({tempo_total:.2f}s)", 
        cor="green"
    )

def executa_tarefa(tarefa_index_str, inicio_rotina_global=None):
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

        return monitorar_tarefa(nome_da_tarefa, funcao, inicio_rotina_global)
    else:
        interface.console.print(f"[red]Tarefa {tarefa_index_str} não encontrada.[/red]")
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
    
def missoes_guilda():
    coord_x, coord_y, tempo = Gerenciador_Coordenadas.pegar_coordenadas('Missoes_Guilda.txt')
    Missoes_Guilda.coletar_missoes_guilda(coord_x, coord_y, tempo)

if __name__ == "__main__":
    menu()