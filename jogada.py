

def escolha_num(lista, jogador, escolha):
    jogador[escolha] = lista.count(int(escolha)) * int(escolha)
    return jogador

#4 iguais
def poker(lista, jogador, escolha):
    ''