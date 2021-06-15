#!/usr/local/bin/python3
from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

# portugues do brasil
setlocale(LC_ALL, 'pt_BR')
# deu problema por causa do meu ubuntu
# nao vou mexer nos pacotes pra n estragar nada aqui
print(month_name[1])
