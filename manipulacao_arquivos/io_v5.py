#!/usr/local/bin/python3

# with abre um recurso e fecha quando o bloco eh finalizado
with open('pessoas.csv') as arquivo:
    for registro in arquivo:
        print('Nome: {} Idade: {}'.format(*registro.strip().split(',')))

if arquivo.closed:
    print('arquivo foi fechado')
