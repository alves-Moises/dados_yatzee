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
            't',
            'p',
            '23x',
            'es',
            'ec',
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
                print('Pontuacao atualizada.')
            else: 
                print('Essa combinacao já está pontuada.')
        else:
            print('Por favor, digite um valor válido')
            registra_pontuacao(lista, jogador)
    return escolha
            
#printa tabela de pontuacoes
def print_escolha(jogador):
    print('#'*50)
    print('#', f'{"COMANDO":^10}',  '#',    f"{'COMBINACAO':^10}",  '#', f'{"PONTUACAO":^10}',                                                      '#')  
    print('#', f'{"[1]":^10}',      '#',    f"{'1':^10}",           '#', f'{jogador["1"]:^10}'      if (jogador["1"] != -1)     else f'{0:^10}',    '#')
    print('#', f'{"[2]":^10}',      '#',    f"{'2':^10}",           '#', f'{jogador["2"]:^10}'      if (jogador["2"] != -1)     else f'{0:^10}',    '#')
    print('#', f'{"[3]":^10}',      '#',    f"{'3':^10}",           '#', f'{jogador["3"]:^10}'      if (jogador["3"] != -1)     else f'{0:^10}',    '#')
    print('#', f'{"[4]":^10}',      '#',    f"{'4':^10}",           '#', f'{jogador["4"]:^10}'      if (jogador["4"] != -1)     else f'{0:^10}',    '#')
    print('#', f'{"[5]":^10}',      '#',    f"{'5':^10}",           '#', f'{jogador["5"]:^10}'      if (jogador["5"] != -1)     else f'{0:^10}',    '#')    
    print('#', f'{"[6]":^10}',      '#',    f"{'6':^10}",           '#', f'{jogador["6"]:^10}'      if (jogador["6"] != -1)     else f'{0:^10}',    '#')   
    print('#', f'{"[pp]":^10}',     '#',    f"{'poker':^10}",       '#', f'{jogador["pp"]:^10}'     if (jogador["pp"] != -1)    else f'{0:^10}',    '#')
    print('#', f'{"[23x]":^10}',    '#',    f"{'2x-3x':^10}",       '#', f'{jogador["23x"]:^10}'    if (jogador["23x"] != -1)   else f'{0:^10}',    '#')
    print('#', f'{"[es]":^10}',     '#',    f"{'escada':^10}",      '#', f'{jogador["es"]:^10}'     if (jogador["es"] != -1)    else f'{0:^10}',    '#')
    print('#', f'{"[ytz]":^10}',    '#',    f"{'yatzee 1':^10}",    '#', f'{jogador["ytz"]:^10}'    if (jogador["ytz"] != -1)   else f'{0:^10}',    '#')
    print('#', f'{"[yy]":^10}',     '#',    f"{'yazzee 2':^10}",    '#', f'{jogador["yy"]:^10}'     if (jogador["yy"] != -1)    else f'{0:^10}',    '#')
    print('#', f'{"[0]":^10}',      '#',    f"{'chance':^10}",      '#', f'{jogador["0"]:^10}'      if (jogador["chance"] != -1) else f'{0:^10}',   '#')
    print('#' * 50)
    print('Sua escolha: ',  end='')
       
#printa pontuacao
def print_pontuacao(jogador):
    print('#'*50)
    print(f"#{'Sua pontuação:':^50}#")
    print('#',    f"{'COMBINACAO':^10}",  '#', f'{"PONTUACAO":^20}',                                                          '#')  
    print('#',    f"{'1':^10}",           '#', f'{jogador["1"]:^20}'          if (jogador["1"] != -1) else f'{0:^20}',        '#')
    print('#',    f"{'2':^10}",           '#', f'{jogador["2"]:^20}'          if (jogador["2"] != -1) else f'{0:^20}',        '#')
    print('#',    f"{'4':^10}",           '#', f'{jogador["4"]:^20}'          if (jogador["4"] != -1) else f'{0:^20}',        '#')
    print('#',    f"{'3':^10}",           '#', f'{jogador["3"]:^20}'          if (jogador["3"] != -1) else f'{0:^20}',        '#')
    print('#',    f"{'5':^10}",           '#', f'{jogador["5"]:^20}'          if (jogador["5"] != -1) else f'{0:^20}',        '#')    
    print('#',    f"{'6':^10}",           '#', f'{jogador["6"]:^20}'          if (jogador["6"] != -1) else f'{0:^20}',        '#')     
    print('#',    f"{'poker':^10}",       '#', f'{jogador["poker"]:^20}'      if (jogador["poker"] != -1) else f'{0:^20}',    '#')
    print('#',    f"{'2x-3x':^10}",       '#', f'{jogador["2x-3x"]:^20}'      if (jogador["2x-3x"] != -1) else f'{0:^20}',    '#')
    print('#',    f"{'escada':^10}",      '#', f'{jogador["escada"]:^20}'     if (jogador["escada"] != -1) else f'{0:^20}',   '#')
    print('#',    f"{'yatzee 1':^10}",    '#', f'{jogador["yatzee_1"]:^20}'   if (jogador["yatzee_1"] != -1) else f'{0:^20}', '#')
    print('#',    f"{'yazzee 2':^10}",    '#', f'{jogador["yatzee_2"]:^20}'   if (jogador["yatzee_2"] != -1) else f'{0:^20}', '#')
    print('#',    f"{'chance':^10}",      '#', f'{jogador["chance"]:^20}'     if (jogador["chance"] != -1) else f'{0:^20}',   '#')
    print('#' * 50)

#atualizar_pontuacao
def registra_pontuacao(lista, jogador):
    print('Lista para adicionar: ')
    print_escolha(jogador)
    escolha = escolhe_combo(lista, jogador)

    #adiciona pontuacao
    if escolha in ['1', '2', '3', '4', '5', '6']:
        nova_pontuacao = jgd.escolha_num(lista, jogador, escolha)
    elif escolha == 'poker':
        nova_pontuacao = jgd.poker(lista)
    
    print_pontuacao(jogador)
    return nova_pontuacao