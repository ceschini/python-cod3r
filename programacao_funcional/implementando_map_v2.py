#!/usr/local/bin/python3
# implementacao simplificada do map
def mapear(funcao, lista):
    return (funcao(elemento) for elemento in lista)  # retorna um generator


if __name__ == '__main__':
    # print(list(mapear(lambda x: x ** 2, [2, 3, 4])))
    resultado = mapear(lambda x: x ** 2, [2, 3, 4])
    print(tuple(resultado))
