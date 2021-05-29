#! /usr/local/bin/python3
from math import pi
import sys
import errno


def help():
    print("É necessário informar o raio do círculo")
    print(f"Sintaxe: {sys.argv[0][2:]} <raio>")


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    # argv = lista com parametros recebidos
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)  # encerrando com erro, codigo 1, permissao
    raio = sys.argv[1]
    area = circulo(raio)
    print('Área do círculo:', area)
