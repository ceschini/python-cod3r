#!/usr/local/bin/python3
from functools import reduce

pessoas = [
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Arthur', 'idade': 26},
    {'nome': 'Rebeca', 'idade': 6},
    {'nome': 'Tiago', 'idade': 19},
    {'nome': 'Gabriela', 'idade': 17},
]
#             reduce(lambda acumulador, seq: funcao, lista, val_inicial)
soma_idades = reduce(lambda idades, p: idades + p['idade'], pessoas, 0)
print('a soma das idades das pessoas eh: ', soma_idades)
