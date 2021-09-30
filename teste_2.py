#utf-8
# def retrn():
#     return['a', 'b']

# x, y = retrn()
# print(x)
# print(y)

# print('abc'['=':40:'='])

lista = [2, 2, 3, 15, 16, 16, 16, 15, 3, 2, 2]

# maior = 0
# for item in lista:
#     if item > maior:
#         maior = item

# i = maior  
lista = [2, 2, 3, 15, 16, 16, 16, 15, 3, 2, 2]
p = ' ' * 32    
for i in range(int(max(lista))):
    print(p, end= '')
    for j in lista:
        if j >= (int(max(lista)) -i):
            print('#', end = '')
        else:
            print(' ', end = '')
    print('')
input('É isso.')

print(f'x {"sim":^33} x')
print(f'x {"aiushdiuahsd":^33} x')

import testa