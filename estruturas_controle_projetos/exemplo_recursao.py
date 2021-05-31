def imprimir(maximo, atual):
    if atual >= maximo:  # ! condicao de parada
        return  # sai do metodo sem retornar nada
    print(atual)
    imprimir(maximo, atual + 1)


imprimir(10, 1)
