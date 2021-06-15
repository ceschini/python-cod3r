#!/usr/local/bin/python3

lista_1 = [1, 2, 3]
dobro = map(lambda x: x * 2, lista_1)
print(list(dobro))

lista_2 = [
    {'nome': 'joao', 'idade': 31},
    {'nome': 'maria', 'idade': 12},
    {'nome': 'jose', 'idade': 36},
]

so_nomes = map(lambda p: p['nome'], lista_2)
print(list(so_nomes))

so_idades = map(lambda p: p['idade'], lista_2)
print(list(so_idades))

frases = map(lambda p: f'{p["nome"]} tem {p["idade"]} anos', lista_2)
print(list(frases))
