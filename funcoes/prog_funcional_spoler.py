def executar(funcao):
    if callable(funcao):  # se eh algo que pode ser invocado
        funcao()


def bom_dia():
    print('bom dia!')


def boa_tarde():
    print('boa tarde!')


if __name__ == '__main__':
    executar(bom_dia)
    executar(boa_tarde)
    executar(1)  # nao eh callable
