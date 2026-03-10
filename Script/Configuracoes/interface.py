from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, TextColumn, BarColumn, TaskProgressColumn, TimeRemainingColumn
import time

console = Console()

def formatar_tempo(segundos):
    """Converte segundos em MM:SS"""
    m = int(segundos // 60)
    s = int(segundos % 60)
    return f"{m:02d}:{s:02d}"

def desenhar_cabecalho():
    console.clear()
    painel = Panel(
        "[bold yellow]🤖 HERO WARS BOT[/bold yellow]\n[green]Módulo de Automação Ativo[/green]", 
        expand=False, 
        border_style="blue"
    )
    console.print(painel)

def desenhar_menu_principal():
    tabela = Table(show_header=True, header_style="bold magenta", border_style="blue")
    tabela.add_column("Opção", justify="center", style="cyan")
    tabela.add_column("Ação", style="white")
    
    tabela.add_row("1", "Criar rotina")
    tabela.add_row("2", "Escolher rotina")
    tabela.add_row("3", "Fazer tarefa específica")
    tabela.add_row("4", "Configurar coordenadas")
    tabela.add_row("5", "Verificar coordenadas")
    tabela.add_row("6", "Verificar cor da posição")
    tabela.add_row("0", "[bold red]Sair[/bold red]")
    
    console.print(tabela)

def mostrar_painel_info(titulo, texto, cor="cyan"):
    painel = Panel(texto, title=f"[bold {cor}]{titulo}[/]", border_style=cor, expand=False)
    console.print(painel)

def exibir_countdown(segundos, mensagem="Aguardando"):
    with Progress(
        TextColumn(f"[bold yellow]{mensagem}[/]"),
        BarColumn(bar_width=40, style="yellow", complete_style="green"),
        TaskProgressColumn(),
        TimeRemainingColumn(),
        console=console
    ) as progress:
        
        tarefa = progress.add_task("espera", total=segundos)
        
        # Loop de 0.1s p animação ficar suave
        passos = int(segundos * 10)
        for _ in range(passos):
            time.sleep(0.1)
            progress.update(tarefa, advance=0.1)