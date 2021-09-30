
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
#printa tabela de pontuacoes
def print_escolha():
    print('Digite sua escolha:')
    print('# [1]   1')
    print('# [2]   2')
    print('# [3]   3')
    print('# [4]   4')
    print('# [5]   5')
    print('# [6]   6')
    print('# [t]   Trinca')
    print('# [pp]  pôker')
    print('# [23x] 2x-3x')
    print('# [es]  escada')
    print('# [ec]  cheia')
    print('# [ytz] yatzee 1 (111)')
    print('# [yy]  yazzee 2')
    print('# [0]   chance')
    print('Sua escolha: ', end='')
#atualizar_pontuacao
def registra_pontuacao(lista, jogador):
    print_escolha()
