palavra = 'paralelepipedo'
for letra in palavra:
    # troca o end de \n por , (imprime na mesma linha)
    print(letra, end=',')
print('fim')

aprovados = ['Rafaela', 'Pedro', 'Renato', 'Maria']
for aluno in aprovados:
    print(aluno)

# pegando indice alem do elemento
for posicao, aluno in enumerate(aprovados):
    print(posicao + 1, aluno)

dias_semana = ('domingo', 'segunda', 'terca',
               'quarta', 'quinta', 'sexta', 'sabado')
for dia in dias_semana:
    print(f'hoje é {dia}')

for letra in set('muito legal'):  # set n garante ordem
    print(letra)

for numero in {1, 2, 3, 4, 5, 6}:
    print(numero)
