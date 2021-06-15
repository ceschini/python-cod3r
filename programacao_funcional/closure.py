#!/usr/local/bin/python3
def multiplicar(x):
    # closure, a funcao conhece o seu contexto interno e externo
    def calcular(y):
        return x * y
    return calcular


if __name__ == '__main__':
    dobro = multiplicar(2)
    triplo = multiplicar(3)
    print(dobro)
    print(f'O triplo de 3 é {triplo(3)}')
    print(f'O dobro de 7 é {dobro(7)}')
