
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

def escolha_num(lista, jogador, escolha):
    jogador[escolha] = lista.count(int(escolha)) * int(escolha)
    return jogador

#4 iguais
def poker(lista, jogador, escolha):
    ''