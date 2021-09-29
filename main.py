#author: alves-Moises

from math import inf
import random as r

def lin():
    print('=-' * 25)

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
                '2x-3x':    -1,  # par e trinca
                'small':    -1,
                'big':      -1,
                'poker':    -1,  # 4 iguais
                'Yatzee_1': -1,  # Yatze! 
                'Yatzee_2': -1   # 11111111111
            }
    return comb

#definir nomes e atributos dos jogadores
def define_jogadores(qtd):
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

#continuar jogo
def valida_jogar():
    valid = False
    while not valid:
        x = valid_int()
        if x in [0, 1]:
            valid = True
        else:
            print('resposta inválida')
    return(bool(x))

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
    print('Digite os valores que deseja manter: (ex: 1 2 3)')
    valid = False
    posicoes = [0]

    while not (valid):
        if posicoes != [0]:
            print('Digite posições válidas')

        posicoes = input().split()
        valid = True

        for valor in posicoes:
            if not valid_int_bool(valor):
                valid = False


    return posicoes   

#funcao principalE
def main():
    lista_jogadores = []
    info_jogadores = {}

    msg = 'Dados, rolagem, jogos '
    print("=" * 50)
    print("=" * (25 - int(len(msg)/2)-1), msg, "=" * (25 - int(len(msg)/2)-1))
    print("=" * 50)

    #listar_jogadores
    print('Digite a quantidade de jogadores: ')
    qtd_jogadores = valid_int()

    #informacoes jogadores
    lista_jogadores, info_jogadores = define_jogadores(qtd_jogadores)
   
    print('\nDigite a quantidade de dados: ')
    dados_qtd = valid_int()

    jogar = True
    while jogar:
        list_dados = []
        i = 0    
        lin()
        for nome in lista_jogadores:
            lin()
            while i < 3:
                print(f'Jogada de {nome}')
                print(f'Jogada {i + 1}')
                resultado = roll(dados_qtd, list_dados)
                
                for j in range(len(resultado)): 
                    print(f'Dado n{j}: ', resultado[j])

                #resultado ordenado
                print('#' * 50)
                print(sorted(resultado))
                lin()
                print('[0] Encerrar jogada')
                print('[1] Continuar jogando os dados')
                if not(valida_jogar()):
                    break

                #segura os dados
                list_dados = nova_lista(resultado)
                print('dados pra rolar denovo: ', list_dados)
                i += 1
        
main()

