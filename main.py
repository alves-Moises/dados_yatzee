#author: alves-Moises

import random as r
import verifa_acerto as vA
from time import sleep

def lin():
    print('=-' * 25)

#verifica se há campos vazios
def jogando_func(jogador):
    valid = False
    for value in jogador.values():
        valid += bool(value == -1)
    return bool(valid)

def comb_func():
    comb = {
                '1':            -1,
                '2':            -1,
                '3':            -1,
                '4':            -1,
                '5':            -1,
                '6':            -1,
                'pp':           -1,  # 4 iguais
                '23x':          -1,  # par e trinca
                'es':           -1,  # 1-5 
                'ytz':          -1,  # Yatze! 
                'yy':           -1,   # 11111111111
                'chance':       -1
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

def imprime_dados(dados):
    print('#' * 50)
    for i in range(len(dados)): 
        msg = f'dado n{i}: {dados[i]}'
        print('#', ' ' * (21 - int(len(msg)/2-1)), msg, ' ' * (21 - int(len(msg)/2-1)), '#')
    print('#' * 50)

#continuar jogada
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

#pegar os valores para nova rolagem dos dados
def nova_lista(lista):
    # imprime_dados(lista)
    print('Digite as posicoes que deseja manter: (ex: 1 2 3)')
    valid = False
    posicoes = [0]

    while not (valid):
        valid = True
        if posicoes != [0]:
            print('Digite posições válidas')

        posicoes = input().split()
        for valor in posicoes:
            #valores não inteiros
            if not (valid_int_bool(valor)):
                valid = False

            #inteiros fora dos parâmetros
            elif not (0 <= int(valor) < len(lista)):
                valid = False

    #nova lista
    temp_list = []
    for i in sorted(posicoes):
        temp_list.append(lista[int(i)])

    return temp_list   

#funcao principalE
def main():
    lista_jogadores = []
    info_jogadores = {}
    dados_qtd = 5

    msg = 'Dados, rolagem, jogos '
    print("=" * 50)
    print("=" * (25 - int(len(msg)/2)-1), msg, "=" * (25 - int(len(msg)/2)-1))
    print("=" * 50)

    #listar_jogadores
    print('Digite a quantidade de jogadores: ')
    qtd_jogadores = valid_int()

    #informacoes jogadores
    lista_jogadores, info_jogadores = define_jogadores(qtd_jogadores)
   
    jogar = True
    while jogar:
           
        lin()
        for nome in lista_jogadores:
            role = True
            list_dados = []
            i = 0 

            while i < 3 and role == True:
                lin()

                msg = f'jogada de {nome}'
                print("=" * (25 - int(len(msg)/2)-1), msg, "=" * (25 - int(len(msg)/2)-1))
                vA.print_pontuacao(info_jogadores[nome])

                print(f'Jogada {i + 1}')
                resultado = sorted(roll(dados_qtd, list_dados))
                imprime_dados(resultado)

                lin()
                if not (i >= 2):    
                    print('[0] Encerrar jogada')
                    print('[1] Continuar jogando os dados')
                    print('Sua escolha: ', end='')
                    if not(valida_jogar()):
                        role = False
                    else:
                        list_dados = nova_lista(resultado)

                i += 1

            #atualiza informacoes de pontuacao
            info_jogadores[nome] = vA.registra_pontuacao(resultado, info_jogadores[nome])
            lin()
            print('-> Jogada encerrada...')
            lin()
            sleep(1)

        #verifica se há campos vazios
        jogar = jogando_func(info_jogadores[lista_jogadores[0]])

    #======== fim de jogo ============

    #======= tabelas de pontuacao ========
    print(f'{"Resultado:":^50}')
    for name in lista_jogadores:
        vA.print_pontuacao(info_jogadores[name])
    lin()

    #======= resultado geral ===========
    print(f'{"Somatório:":^50}')
    dict_pontuacao = {}
    for nome in lista_jogadores:
        soma = 0
        for value in info_jogadores[nome].values():
            soma += value
        dict_pontuacao[nome] = soma
        print('#' * 55)
        print('#', f'{"Nome:":^10}', f'{nome:^10}', ' ' * 10, f'{"Pontuacao: ":^10}', f'{dict_pontuacao[nome]:^10}', '#')
    lin()


#inicio e recomeço
continua = True
while continua:
    main()
    
    valid = False
    print('Você gostaria de jogar novamente? [1] sim [2] nao')
    while not valid:
        x = valid_int()
        if not (x in [1, 2]):
            print('Digite um valor válido.')
        else:
            valid = True
    
    #finalizar jogo
    if x == 2:
        continua = False
        lin()
        lin()
        lin()
lin()
print('Obrigado por jogar!')
lin()
print(f'{"Autor: Moisés Alves":^50}')
print(f'{"Github: alves-Moises":^50}')
lin()
        
        