class No:
    def __init__(self, value):
        self.value = value
        self.proximo = None
        self.anterior = None

    def mostra_no(self):
        print(self.value)


class ListaDuplamenteEncadeada():
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def insere_inicio(self, value):
        novo = No(value)
        if self.__is_empty():
            self.ultimo = novo
        else:
            self.primeiro.anterior = novo
        novo.proximo = self.primeiro
        self.primeiro = novo

    def insere_final(self, value):
        novo = No(value)
        if self.__is_empty():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo
            novo.anterior = self.ultimo
        self.ultimo = novo

    def excluir_inicio(self):
        temp = self.primeiro
        if self.primeiro.proximo is None:
            self.ultimo = None
        else:
            self.primeiro.proximo.anterior = None
        self.primeiro = self.primeiro.proximo
        return temp

    def excluir_final(self):
        temp = self.ultimo
        if self.primeiro.proximo is None:
            self.ultimo = None
        else:
            self.ultimo.anterior.proximo = None
        self.ultimo = self.ultimo.anterior
        return temp

    def excluir_posicao(self, value):
        atual = self.primeiro
        while atual.value != value:
            atual = atual.proximo
            if atual is None:
                return None
        if atual == self.primeiro:
            self.primeiro = atual.proximo
        else:
            atual.anterior.proximo = atual.proximo

        if atual == self.ultimo:
            self.ultimo = atual.anterior
        else:
            atual.proximo.anterior = atual.anterior
        return atual

    def mostrar_frente(self):
        atual = self.primeiro
        while atual is not None:
            atual.mostra_no()
            atual = atual.proximo

    def mostrar_tras(self):
        atual = self.ultimo
        while atual is not None:
            atual.mostra_no()
            atual = atual.anterior

    def __is_empty(self):
        return self.primeiro is None


if __name__ == '__main__':
    lista = ListaDuplamenteEncadeada()
    lista.insere_inicio(1)
    lista.insere_inicio(2)
    lista.insere_inicio(3)
    lista.insere_inicio(4)
    lista.insere_inicio(5)

    lista.insere_final(1)
    lista.insere_final(2)
    lista.insere_final(3)

    print(lista.mostrar_frente())
    print("--------------------")
    print(lista.mostrar_tras())

    lista.excluir_inicio()
    lista.excluir_final()

    print(lista.mostrar_frente())
    print("--------------------")
    print(lista.mostrar_tras())
