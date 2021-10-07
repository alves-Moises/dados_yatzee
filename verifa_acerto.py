from time import sleep
import jogada as jgd
#valida inteiro
def valid_int():
    valid = False
    while not valid:
        try:
            x = int(input())
        except:
            print('Digite um valor válido.')
        else:
            valid = True
    return x

def escolha_lista():
    lista = [
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',
            'pp',
            '23x',
            'es',
            'ytz',
            'yy',
            '0'
        ]
    return lista

#escolher onde aplicar a pontuação
def escolhe_combo(lista, jogador):
    valid =  False
    while not valid:
        escolha = input()
        if escolha.lower() in escolha_lista():
            if (jogador[escolha] == -1):
                valid = True
                print('-> Atualizando pontuacao...')
                sleep(1)
            else: 
                print('Essa combinacao já está pontuada.')
        else:
            print('Por favor, digite um valor válido')
    return escolha

#printa tabela de pontuacoes
def print_escolha(jogador):
    print('#'*50)
    print('#', f'{"COMANDO":^10}',  '#',    f"{'COMBINACAO':^10}",  '#', f'{"PONTUACAO":^10}',                                                        '#')  
    print('#', f'{"[1]":^10}',      '#',    f"{'1':^10}",           '#', f'{jogador["1"]:^10}'      if (jogador["1"] != -1)     else f'{"-":^10}',    '#')
    print('#', f'{"[2]":^10}',      '#',    f"{'2':^10}",           '#', f'{jogador["2"]:^10}'      if (jogador["2"] != -1)     else f'{"-":^10}',    '#')
    print('#', f'{"[3]":^10}',      '#',    f"{'3':^10}",           '#', f'{jogador["3"]:^10}'      if (jogador["3"] != -1)     else f'{"-":^10}',    '#')
    print('#', f'{"[4]":^10}',      '#',    f"{'4':^10}",           '#', f'{jogador["4"]:^10}'      if (jogador["4"] != -1)     else f'{"-":^10}',    '#')
    print('#', f'{"[5]":^10}',      '#',    f"{'5':^10}",           '#', f'{jogador["5"]:^10}'      if (jogador["5"] != -1)     else f'{"-":^10}',    '#')    
    print('#', f'{"[6]":^10}',      '#',    f"{'6':^10}",           '#', f'{jogador["6"]:^10}'      if (jogador["6"] != -1)     else f'{"-":^10}',    '#')   
    print('#', f'{"[pp]":^10}',     '#',    f"{'poker':^10}",       '#', f'{jogador["pp"]:^10}'     if (jogador["pp"] != -1)    else f'{"-":^10}',    '#')
    print('#', f'{"[23x]":^10}',    '#',    f"{'2x-3x':^10}",       '#', f'{jogador["23x"]:^10}'    if (jogador["23x"] != -1)   else f'{"-":^10}',    '#')
    print('#', f'{"[es]":^10}',     '#',    f"{'escada':^10}",      '#', f'{jogador["es"]:^10}'     if (jogador["es"] != -1)    else f'{"-":^10}',    '#')
    print('#', f'{"[ytz]":^10}',    '#',    f"{'yatzee 1':^10}",    '#', f'{jogador["ytz"]:^10}'    if (jogador["ytz"] != -1)   else f'{"-":^10}',    '#')
    print('#', f'{"[yy]":^10}',     '#',    f"{'yazzee 2':^10}",    '#', f'{jogador["yy"]:^10}'     if (jogador["yy"] != -1)    else f'{"-":^10}',    '#')
    print('#', f'{"[0]":^10}',      '#',    f"{'chance':^10}",      '#', f'{jogador["0"]:^10}'      if (jogador["0"] != -1) else f'{"-":^10}',   '#')
    print('#' * 50)
    print('Escolha uma combinacao para atualizar: ',  end='')
       
#printa pontuacao
def print_pontuacao(jogador):
    print('#'*50)
    print(f"#{'Sua pontuação:':^50}#")
    print('#',    f"{'COMBINACAO':^10}",  '#', f'{"PONTUACAO":^20}',                                                            '#')  
    print('#',    f"{'1':^10}",           '#', f'{jogador["1"]:^20}'          if (jogador["1"] != -1) else f'{"-":^20}',        '#')
    print('#',    f"{'2':^10}",           '#', f'{jogador["2"]:^20}'          if (jogador["2"] != -1) else f'{"-":^20}',        '#')
    print('#',    f"{'3':^10}",           '#', f'{jogador["3"]:^20}'          if (jogador["3"] != -1) else f'{"-":^20}',        '#')
    print('#',    f"{'4':^10}",           '#', f'{jogador["4"]:^20}'          if (jogador["4"] != -1) else f'{"-":^20}',        '#')
    print('#',    f"{'5':^10}",           '#', f'{jogador["5"]:^20}'          if (jogador["5"] != -1) else f'{"-":^20}',        '#')    
    print('#',    f"{'6':^10}",           '#', f'{jogador["6"]:^20}'          if (jogador["6"] != -1) else f'{"-":^20}',        '#')     
    print('#',    f"{'poker':^10}",       '#', f'{jogador["pp"]:^20}'         if (jogador["pp"] != -1) else f'{"-":^20}',       '#')
    print('#',    f"{'2x-3x':^10}",       '#', f'{jogador["23x"]:^20}'        if (jogador["23x"] != -1) else f'{"-":^20}',      '#')
    print('#',    f"{'escada':^10}",      '#', f'{jogador["es"]:^20}'         if (jogador["es"] != -1) else f'{"-":^20}',       '#')
    print('#',    f"{'yatzee 1':^10}",    '#', f'{jogador["ytz"]:^20}'        if (jogador["ytz"] != -1) else f'{"-":^20}',      '#')
    print('#',    f"{'yazzee 2':^10}",    '#', f'{jogador["yy"]:^20}'         if (jogador["yy"] != -1) else f'{"-":^20}',       '#')
    print('#',    f"{'chance':^10}",      '#', f'{jogador["0"]:^20}'          if (jogador["0"] != -1) else f'{"-":^20}',        '#')
    print('#' * 50)

#atualizar_pontuacao
def registra_pontuacao(lista, jogador):
    print('Seus dados: ', lista)
    print_escolha(jogador)
    escolha = escolhe_combo(lista, jogador)

    #adiciona pontuacao
    if escolha in ['1', '2', '3', '4', '5', '6']:
        nova_pontuacao = jgd.escolha_num(lista, jogador, escolha)
    elif escolha == 'pp':
        nova_pontuacao = jgd.poker(lista, jogador)
    elif escolha == '23x':
        nova_pontuacao = jgd.vinte_tres(lista, jogador)
    elif escolha == 'es':
        nova_pontuacao = jgd.es(lista, jogador)
    elif escolha == 'ytz':
        nova_pontuacao = jgd.ytz(lista, jogador)
    elif escolha == 'yy':
        nova_pontuacao = jgd.yy(lista, jogador)
    elif escolha =='0':
        nova_pontuacao = jgd.chance(lista, jogador)
    else:
        print('Algum erro com escolha (??)')

    print('...')
    print_pontuacao(jogador)
    sleep(2)
    return nova_pontuacao