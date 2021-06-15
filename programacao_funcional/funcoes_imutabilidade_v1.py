#!/usr/local/bin/python3
from functools import reduce
from operator import add

valores = [30, 10, 25, 70, 100, 94]

print(sorted(valores))  # numeros ordenados crescente
print(valores)  # lista original permanece imutavel

# valores.sort()
# print(valores)  # mudou a lista original

print(min(valores))  # retorna menor valor
print(max(valores))  # retorna maior valor
print(sum(valores))
print(reduce(add, valores))  # msm coisa que o sum mas com reduce
print(list(reversed(valores)))  # reverte valores da lista
print(valores)  # imutabilidade
