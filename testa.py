dicionario = {'a': 1, 'b': 2, 'c': 3}

for item in dicionario:
    print(item)
    print(dicionario[item])
print()

continua = True
while continua:
    print('continuando')
    
    valid = False
    print('Você gostaria de jogar novamente? [1] sim [2] nao')
    while not valid:
        x = int(input())
        if not (x in [1, 2]):
            print('Digite um valor válido.')
        else:
            valid = True
    
    if x == 2:
        continua = False
        
        