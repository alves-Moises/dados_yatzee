#author: alves-Moises

import random as r

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

#Rollagem de dados
def roll(dices, dices_list = []):
    while len(dices_list) < dices:
        dices_list.append(r.randint(1, 6))
    return dices_list

def nova_lista(lista):
    print('Digite as posições que deseja manter: (ex: 1 2 3)')
    valid = False
    while not valid:
        posicoes = input().split(' ')
        for i in posicoes:
            valid_int()


#funcao principal
def main():
    msg = 'Dados, rolagem, jogos '
    print("=" * 50)
    print("=" * (25 - int(len(msg)/2)-1), msg, "=" * (25 - int(len(msg)/2)-1))
    print("=" * 50)

    print('\nDigite a quantidade de dados: ')
    dados_qtd = valid_int()

    jogar = True
    while jogar:
        partida = True
        list_dados = []
        i = 0    
        while i < 3:
            print(f'Jogada {i + 1}')
            resultado = roll(dados_qtd, list_dados)
            for i in resultado: print('Resultado parcial: ', i)
            print('#' * 50)
            print(sorted(resultado))
            list_dados = nova_lista(resultado)
            


            i += 1
        

        
main()

