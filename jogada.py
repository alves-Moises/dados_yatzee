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
        jogador['pp'] = 40
        print('Poker atualizado!')
    else:
        jogador['pp'] = 0
        print('Poker zerado!')
    sleep(1)
    return jogador

#2x 3x
def vinte_tres(lista, jogador):
    jgd = sorted(lista)
    #par e trinca
    if (jgd[0] == jgd[1] == jgd[2]) != (jgd[3] == jgd[4]):
        jogador['23x'] = 40
        print('23x Atualiado!')
    
    #trinca e par
    elif (jgd[0] == jgd[1] != jgd[2] == jgd[3] == jgd[4]):
        jogador['23x'] = 40
        print('23x Atualiado!')

    #nao pontua
    else:
        jogador['23x'] = 0
        print('23x zerado!')
    
    sleep(1)
    return jogador

#escada 1 a 5 ou 1 a 6
def es(lista, jogador):
    jgd = sorted(lista)
    valid = True
    #verifica sequencia
    for i in range(4): valid = (valid) and (jgd[i] + 1 == jgd [i + 1])
    jogador['es'] = 25 if valid else 0
    print('Escada atualizada!')
    return jogador

#yatze 2222
def ytz(lista, jogador):
    if  lista[0] == lista[1] == lista[2] == lista[3] == lista[4]:
        jogador['ytz'] = 50
        print('Yatzee atualizado.')
    else:
        jogador['ytz'] = 0
        print('Yatzee zerado.')
    return jogador

#yatzee 111
def yy(lista, jogador):
    if  lista[0] == lista[1] == lista[2] == lista[3] == lista[4] == 1:
        jogador['ytz'] = 50
        print('Yatzee atualizado.')
    else:
        jogador['ytz'] = 0
        print('Yatzee zerado.')
    return jogador

#chance
def chance(lista, jogador):
    soma = 0
    for value in lista:
        soma += value
        
    jogador['0'] = soma
    return jogador
                