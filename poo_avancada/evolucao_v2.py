#!/usr/local/bin/python3
class Humano:
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    # metodo de instancia recebe self como primeiro param
    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self

    # metodo estatico n recebe params
    # eh igual ao metodo de modulo, mas de um classe
    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    # metodo de classe recebe a classe como primeiro param
    @classmethod
    def is_evoluido(cls):  # polimorfismo, cls pode ser multiplas classes
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):
    especie = Humano.especies()[-2]


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == '__main__':
    jose = HomoSapiens('José')
    grokn = Neanderthal('Grokn')
    print(
        f'Evolução (a partir da classe): {", ".join(HomoSapiens.especies())}')
    print(f'Evolução (a partir da instancia): {", ".join(jose.especies())}')
    print(f'Homo Sapiens evoluído? {HomoSapiens.is_evoluido()}')
    print(f'Neanderthal evoluído? {Neanderthal.is_evoluido()}')
    print(f'José evoluido? {jose.is_evoluido()}')
    print(f'Grokn evoluido? {grokn.is_evoluido()}')
