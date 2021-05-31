# pep8 constants = UPPERCASE
PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')
textos = [
    'João gosta de futebol e política',
    'A praia foi divertida',
]

for texto in textos:
    found = False
    # dividindo as palavras por espaco em branco (padrao split)
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possui pelo menos uma palavra probibida:', palavra)
            found = True
            break

    if not found:
        print('Texto autorizado:', texto)
