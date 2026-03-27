# 🤖 Hero Wars: Dominion Era - Advanced Automation Engine

Um bot de automação de alto desempenho desenvolvido em Python para o jogo *Hero Wars* (Desktop/Web). 

Diferente de scripts de macro tradicionais (que dependem de tempos de espera estáticos e cegos), este projeto utiliza uma **Arquitetura Assíncrona de Escalonamento Guloso (Greedy Scheduling)** e **Verificação Dinâmica de Pixels** para maximizar a eficiência, reduzindo o tempo ocioso da máquina a zero.

## 🚀 Principais Funcionalidades e Arquitetura

* **⚡ Intercalação Inteligente de Cooldown (Assíncrona):** O bot não espera de braços cruzados. Durante os 47 segundos de recarga obrigatória entre as lutas da Arena, a engine entra em modo de escalonamento dinâmico, executando tarefas menores (Vidente Astral, Presentes, Torre, etc.) e retornando cirurgicamente para a Arena no exato momento em que o combate é liberado.
* **👁️ Verificação Visual Dinâmica (Pixel Matching):** Substituição de `time.sleep()` rígidos por funções de "Cão de Guarda" (Watchdog) que monitoram a tela em tempo real. O bot detecta transições de botões (ex: botões de "Atacar" ou "Coletar" ficando verdes) para avançar milissegundos após a liberação do jogo, derrubando o tempo total de rotinas longas como a Masmorra.
* **🧩 Particionamento Inteligente de Tarefas:** Tarefas extensas (como a Masmorra) são divididas logicamente pelo motor principal. O bot pode entrar na Masmorra, executar o modo Automático, sair para a Cidade para cumprir uma luta pendente da Arena, e retornar para o modo Manual da Masmorra de forma autônoma, sem perder o estado da aplicação.
* **🖥️ Interface Rica de Linha de Comando (CLI):** UI de terminal desenvolvida com a biblioteca `rich`, fornecendo feedback em tempo real, painéis informativos, temporizadores formatados e barras de progresso profissionais para monitoramento da rotina.
* **📍 Gerenciador de Coordenadas Nativo:** Ferramenta embutida que utiliza "Hooks" globais do mouse (`pynput`) para mapear coordenadas da tela (X, Y) e calibrar tempos, salvando a configuração automaticamente em arquivos de texto sem a necessidade de softwares externos.

## 🛠️ Tecnologias Utilizadas

* **Python 3.10+**
* **PyAutoGUI:** Controle de interface (Mouse/Teclado) e Captura de Tela.
* **Pynput:** Escuta global de eventos físicos do mouse para mapeamento.
* **Rich:** Renderização avançada de componentes no terminal.
* **Threading:** Gerenciamento de timeouts, inputs de interrupção seguros e painéis assíncronos.

## 📁 Estrutura do Projeto

```text
📦 Automacao-Hero-Wars
 ┣ 📂 Componentes_Hero_Wars/      # Módulos isolados de cada tarefa (Lego)
 ┃ ┣ 📂 Arena
 ┃ ┣ 📂 Masmorra
 ┃ ┣ 📂 Torre
 ┃ ┗ ...
 ┣ 📂 Configuracoes/
 ┃ ┣ 📂 Coordenadas/              # Arquivos .txt contendo (X, Y, Tempo) gerados pelo usuário
 ┃ ┣ 📜 interface.py              # Motor visual do terminal (Rich)
 ┃ ┗ 📜 rotina.py                 # Lógica de seleção de tarefas e filas
 ┣ 📂 Util/
 ┃ ┗ 📜 funcoes_suporte.py        # Core Engine: Cliques humanizados, Pixel Matching, Crop Tool
 ┣ 📜 menu.py                     # Ponto de Entrada (Main Loop e Escalonador)
 ┗ 📜 requirements.txt            # Contrato de dependências
