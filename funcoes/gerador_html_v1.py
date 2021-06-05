#!/usr/local/bin/python3
def tag_bloco(texto, classe='success'):
    return f'<div class="{classe}">{texto}</div>'


if __name__ == '__main__':
    # Testes (assertions)
    # assert compara a saida da func com o que passamos
    # se for true n faz nada
    # se for false chama AssertionError
    assert tag_bloco('incluido com sucesso') == \
        '<div class="success">incluido com sucesso</div>'
    assert tag_bloco('impossivel excluir', 'error') == \
        '<div class="error">impossivel excluir</div>'
    print(tag_bloco('bloco'))
