#!/usr/local/bin/python3
def fibonacci(sequencia=[0, 1]):
    # uso de mutaveis como valor default (armadilha)
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


if __name__ == '__main__':
    inicio = fibonacci()
    print(inicio, id(inicio))
    print(fibonacci(inicio))
    # default mutavel = usa o mesmo espaco de memoria para todas instancias
    restart = fibonacci()
    print(restart, id(restart))
    assert restart == [0, 1, 1]  # lista esperada
