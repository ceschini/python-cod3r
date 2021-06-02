#!/usr/local/bin/python3
arquivo = open('pessoas.csv')
dados = arquivo.read()  # lendo *todo* o arquivo e carregando na memoria
arquivo.close()
for registro in dados.splitlines():
    # o * eh um spread operator
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))
