#!/usr/local/bin/python3
from datetime import datetime, timedelta


# criando uma excessao nossa, filha de exception
class TarefaNaoEncontrada(Exception):
    pass


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):  # a classe agr eh iteravel
        return self.tarefas.__iter__()

    # sobrecarga do operador '+='
    # projeto += tarefa
    def __iadd__(self, tarefa):
        tarefa.dono = self
        self._add_tarefa(tarefa)
        return self

    def _add_tarefa(self, tarefa, **kwargs):
        self.tarefas.append(tarefa)

    def _add_nova_tarefa(self, descricao, **kwargs):
        self.tarefas.append(Tarefa(descricao, kwargs.get('vencimento', None)))

    def add(self, tarefa, vencimento=None, **kwargs):
        funcao_escolhida = self._add_tarefa if isinstance(tarefa, Tarefa) \
            else self._add_nova_tarefa
        kwargs['vencimento'] = vencimento
        funcao_escolhida(tarefa, **kwargs)

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        try:
            # possivel index error
            return [tarefa for tarefa in self.tarefas
                    if tarefa.descricao == descricao][0]
        except IndexError as e:
            # raise = lanca erro
            raise TarefaNaoEncontrada(str(e))

    def __str__(self):
        return f'{self.nome} - {len(self.pendentes())} tarefa(s) pendente(s)'


class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
            status.append('(concluída)')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('(vencida)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'(vence em {dias} dias)')
        return f'{self.descricao}' + ' '.join(status)


# heranca -> class filho(pai)
class TarefaRecorrente(Tarefa):
    def __init__(self, descricao, vencimento, dias=7):
        super().__init__(descricao, vencimento)
        self.dias = dias
        self.dono = None

    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        nova_tarefa = TarefaRecorrente(
            self.descricao, novo_vencimento, self.dias)
        if self.dono:
            self.dono += nova_tarefa
        return nova_tarefa


def main():
    casa = Projeto('deveres de casa')
    casa.add('passar roupa', datetime.now())
    casa.add('lavar prato')
    casa += TarefaRecorrente('trocar lencois', datetime.now(), 7)
    casa.procurar('trocar lencois').concluir()
    print(casa)

    try:
        casa.procurar('lavar prato - erro').concluir()
    except TarefaNaoEncontrada as e:
        print(f'a causa do erro foi {str(e)}')

    casa.procurar('lavar prato').concluir()
    for tarefa in casa:
        print(f'- {tarefa}')
    print(casa)


if __name__ == '__main__':
    main()
