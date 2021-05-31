#!/usr/local/bin/python3
# sequencia tem param padrao
def fibonacci(quantidade, sequencia=(0, 1)):
    # importante: condicao de parada
    if len(sequencia) == quantidade:
        return sequencia
        # concatenando a tupla sequencia
        # com uma tupla que tenha a soma (prox valor)
    return fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))


if __name__ == '__main__':
    # listar os 20 primeiros numeros
    for fib in fibonacci(20):
        print(fib)
