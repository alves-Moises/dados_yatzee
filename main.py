#author: alves-Moises

import random as r

def comb_func():
    comb = {
                '1':        -1,
                '2':        -1,
                '3':        -1,
                '4':        -1,
                '5':        -1,
                '6':        -1,
                'Par':      -1,
                'Trinca':   -1,
                'small':    -1,
                'big':      -1,
                'poker':    -1,
                'Yatzee_1': -1,
                'Yatzee_2': -1
            }
    return comb

def info_jogadores(qtd):
    info = {}
    nomes = []
    for i in range(qtd):
        print(f'Digite o nome do jogador {i + 1}: ', end = '')
        nome = input()
        nomes.append(nome)
        info[nome] = comb_func()
    return[nomes, info]

    
#validacao de valor inteiro
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

#valodacao retorno booleano
def valid_int_bool(valores):
    valid = False
    try:
        int(valores)
    except ValueError:
        print('erro em ', valores)
    else:
        valid = True 
    return valid


#Rollagem de dados
def roll(dices, dices_list = []):
    while len(dices_list) < int(dices):
        dices_list.append(r.randint(1, 6))
    return dices_list

def nova_lista(lista):
    print('Digite as posições que deseja manter: (ex: 1 2 3)')
    valid = False
    posicoes = [0]

    while not (valid or (max(posicoes) > len(lista))):
        if posicoes != [0]:
            print('Digite posições válidas')


        posicoes = input().split()
        valid = True

        for valor in posicoes:
            if not valid_int_bool(valor):
                valid = False


    return posicoes   


#funcao principal
def main():
    msg = 'Dados, rolagem, jogos '
    print("=" * 50)
    print("=" * (25 - int(len(msg)/2)-1), msg, "=" * (25 - int(len(msg)/2)-1))
    print("=" * 50)

    #listar_jogadores
    print('Digite a quantidade de jogadores: ')
    qtd_jogadores = valid_int()

   
    lista_jogadores, info_jogadores = info_jogadores(qtd_jogadores)
    print(info_jogadores)
    # Leitura de valores

    print('\nDigite a quantidade de dados: ')
    dados_qtd = valid_int()

    #
    jogar = True
    while jogar:
        partida = True
        list_dados = []
        i = 0    
        for nome in lista_jogadores:
            while i < 3:
                print(f'Jogada de {nome}')
                print(f'Jogada {i + 1}')
                resultado = roll(dados_qtd, list_dados)
                
                for j in range(len(resultado)): 
                    print(f'Dado n{j}: ', resultado[j])

                #resultado ordenado
                print('#' * 50)
                print(sorted(resultado))

                list_dados = nova_lista(resultado)
                


                i += 1
            print("Fim da jogada. Gostaria de continar? \n[1] Sim [2] Não     ", end = '')

        partida = jogar()

        
main()

