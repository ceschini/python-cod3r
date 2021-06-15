#!/usr/local/bin/python3
from functools import reduce
from operator import add

valores = (30, 10, 25, 70, 100, 94)  # tuplas sao imutaveis

print(sorted(valores))  # numeros ordenados crescente
print(valores)  # lista original permanece imutavel

# valores.sort()  # vai dar erro, tuple has no 'sort'
# print(valores)

print(min(valores))  # retorna menor valor
print(max(valores))  # retorna maior valor
print(sum(valores))
print(reduce(add, valores))  # msm coisa que o sum mas com reduce
print(tuple(reversed(valores)))  # reverte valores da lista
print(valores)  # imutabilidade
