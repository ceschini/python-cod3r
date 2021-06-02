# generators geram numeros sob demanda, consumindo menos memoria q a lista
generator = (i ** 2 for i in range(10) if i % 2 == 0)

for numero in generator:
    print(numero)
