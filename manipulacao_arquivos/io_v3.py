#!/usr/local/bin/python3
arquivo = open('pessoas.csv')

# python vai usar streaming
# isso eh, vai ler do arquivo por demanda do for
for registro in arquivo:
    # strip() tira espacos em branco e quebras de linha
    print('Nome: {} Idade: {}'.format(*registro.strip().split(',')))
arquivo.close()
