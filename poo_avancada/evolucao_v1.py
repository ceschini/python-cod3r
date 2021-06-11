#!/usr/local/bin/python3
class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self


if __name__ == '__main__':
    jose = Humano('José')
    # quando retorna self da pra encadear
    grokn = Humano('Grokn').das_cavernas()
    # grokn.das_cavernas()
    # ou
    # Humano.das_cavernas(grokn)
    print(f'Humano.especie: {Humano.especie}')
    print(f'jose.especie: {jose.especie}')
    print(f'grokn.especie: {grokn.especie}')
