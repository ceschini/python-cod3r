# while True:
#     print('vai demorar muito')

from random import randint

numero_informado = -1
numero_secreto = randint(0, 9)

# se a condicao nao for true, ele nem entra no while
while numero_informado != numero_secreto:
    numero_informado = int(input('chuta um numero ae (0-9): '))

print('numero secreto {} foi encontrado!'.format(numero_secreto))
