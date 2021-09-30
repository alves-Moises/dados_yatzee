

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






def print_escolha():
    print('Digite sua escolha:')
    print('# [1] 1')
    print('# [2] 2')
    print('# [3] 3')
    print('# [4] 4')
    print('# [5] 5')
    print('# [6] 6')


def registra_pontuacao(lista, jogador):
    print_escolha()
    print(jogador)
