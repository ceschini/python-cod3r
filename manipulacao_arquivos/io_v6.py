#!/usr/local/bin/python3

with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:  # w = modo de escrita
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            # printar dentro do arquivo
            print('Nome: {} Idade: {}'.format(*pessoa), file=saida)

if arquivo.closed:
    print('arquivo foi fechado')

if saida.closed:
    print('arquivo de saida foi fechado')
