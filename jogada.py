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
    print('Digite o valor que você quer: ', end='')
    numero = valid_int()
    if lista.count(numero) >= 4:
        jogador['pp'] = 30
    else:
        jogador['pp'] = 0

    return jogador