#! /usr/local/bin/python3
from math import pi
import sys  # receber argumentos na call do script


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    # argv = lista com parametros recebidos
    raio = sys.argv[1]
    area = circulo(raio)
    print('Área do círculo:', area)
