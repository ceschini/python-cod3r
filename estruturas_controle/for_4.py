# for i in range(1, 11):
#     if i == 6:
#         break
#     print(i)
# nao vai cair no else por causa do break
# else:
#     print('fim')

from random import randint


def sortear_dado():
    return randint(1, 6)  # numero random de 1 ate 6


for i in range(1, 7):
    if i % 2 == 1:
        continue

    if sortear_dado() == i:
        print('acertou!', i)
        break
else:  # so cai no else se n executa break
    print('nao acertou o numero!')
