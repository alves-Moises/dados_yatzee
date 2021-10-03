from time import sleep

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

# 1 ou 2 ou 3 ou 4 ou 5 ou 6
def escolha_num(lista, jogador, escolha):
    jogador[escolha] = lista.count(int(escolha)) * int(escolha)
    print(f'Valor {escolha} atualizado com sucesso.')
    sleep(1)
    return jogador

#4 iguais
def poker(lista, jogador):
    if (lista.count(1) >= 4) or (lista.count(2) >= 4) or (lista.count(3) >= 4) or (lista.count(4) >= 4) or (lista.count(5) >= 4) or (lista.count(6) >= 4):
        jogador['pp'] = 30
    else:
        jogador['pp'] = 0
    print('Poker atualizado!')
    sleep(1)
    return jogador