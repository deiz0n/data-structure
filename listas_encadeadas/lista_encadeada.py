import numpy as np

class No:
    def __init__(self, value):
        self.value = value
        self.proximo = None

    def mostra_no(self):
        print(self.value)

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def insere_inicio(self, value):
        novo = No(value)
        novo.proximo = self.primeiro
        self.primeiro = novo

    def mostrar(self):
        self.__is_empty()
        atual = self.primeiro
        while atual is not None:
            atual.mostra_no()
            atual = atual.proximo

    def excluir_inicio(self):
        temp = self.primeiro
        self.__is_empty()
        self.primeiro = self.primeiro.proximo
        return temp

    def pesquisar(self, value):
        self.__is_empty()
        atual = self.primeiro
        while atual.value != value:
            if atual.proximo is None:
                print('Value not found')
                return None
            atual = atual.proximo
        return atual

    def excluir_posicao(self, value):
        self.__is_empty()
        atual = self.primeiro
        anterior = self.primeiro
        while atual.value != value:
            if atual.proximo is None:
                return None
            else:
                anteior = atual
                atual = atual.proximo

        if atual == self.primeiro:
            self.primeiro = self.primeiro.proximo
        else:
            anteior.proximo = atual.proximo

    def __is_empty(self):
        if self.primeiro.proximo is None:
            print('List is empty')
            return None

if __name__ == "__main__":
    lista = ListaEncadeada()
    lista.insere_inicio(1)
    lista.insere_inicio(2)
    lista.insere_inicio(3)
    lista.insere_inicio(4)
    lista.insere_inicio(5)

    lista.excluir_posicao(3)
    lista.excluir_posicao(5)
    lista.excluir_posicao(1)


    print(lista.mostrar())

