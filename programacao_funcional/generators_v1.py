#!/usr/local/bin/python3
# generators tem retorno parcial
# eles sabem qual foi o ultimo e qual será o proximo retorno
# lazy evaluation: soh executa quando necessario (next)
# generators guardam o estado interno, sabem onde parou
def cores_arco_iris():
    yield 'vermelho'  # cada next chamará um yield
    yield 'laranja'
    yield 'amarelo'
    yield 'verde'
    yield 'azul'
    yield 'indigo'
    yield 'violeta'


if __name__ == '__main__':
    generator = cores_arco_iris()
    print(type(generator))
    while True:  # soh para na excessao StopIteration
        print(next(generator))
