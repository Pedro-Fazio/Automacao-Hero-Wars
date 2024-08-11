import os

def cria_rotina():
    nomeRotina = input("\nDê um nome para sua rotina: ")
    caminho_pasta = 'Configuracoes/Rotinas'
    caminho = f'{caminho_pasta}/{nomeRotina}.txt'
    tarefasAdicionadas = []
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
    
    # Verifica se a pasta "Rotinas" existe, caso contrário, cria a pasta
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)
    
    with open(caminho, 'w') as arquivo:
        while True:
            print('\n')
            for indice, valor in enumerate(tarefas):
                print(f'Tarefa {indice}: {valor}')
            
            tarefaAdicionada = input('\nAdicione uma tarefa na sua rotina: ').strip()

            if tarefas[int(tarefaAdicionada)] in tarefasAdicionadas:
                print('\nEssa tarefa já foi adicionada, por favor escolha outra tarefa.')
            else:
                tarefasAdicionadas.append(tarefas[int(tarefaAdicionada)])
                arquivo.write(f'{ tarefaAdicionada }\n')
            
                print('\nDeseja adicionar mais tarefas?\n1: Sim\n2: Não\n')
                resposta = input('Opção escolhida: ')
                adicionarMais = resposta == "1"
                if adicionarMais == False:
                    break

    
    print(f'Rotina "{nomeRotina}" criada com sucesso no caminho: {caminho}')


def escolhe_rotina():
    rotinas = pega_rotinas()
    
    print('\n')
    for indice, valor in enumerate(rotinas):
        print(f'Rotina {indice}: {valor}')
    
    escolha = input("Escolha uma das rotinas listadas: ").strip()
    rotinaEscolhida = rotinas[int(escolha)]

    return le_dados_rotina(rotinaEscolhida)


def pega_rotinas():
    caminho_pasta = 'Configuracoes/Rotinas'
    rotinas = [f for f in os.listdir(caminho_pasta) if f.endswith('.txt')]

    return rotinas


def le_dados_rotina(rotinaEscolhida):
    caminhoArquivo = f'Configuracoes/Rotinas/{rotinaEscolhida}'

    with open(caminhoArquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    return [linha.strip() for linha in linhas]  # Remove o caractere de nova linha


