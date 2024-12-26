import numpy as np

class FilaCircular:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numeros_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=object)

    def __fila_vazia(self):
        return self.numeros_elementos == 0

    def __fila_cheia(self):
        return self.numeros_elementos == self.capacidade

    def enfileirar(self, valor):
        if self.__fila_cheia():
            print('Queue is full')
            return

        if self.final == self.capacidade - 1:
            self.final = -1
        self.final += 1
        self.valores[self.final] = valor
        self.numeros_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia():
            print('Queue is empty')
            return

        temp = self.valores[self.inicio]
        self.inicio += 1
        if self.inicio == self.capacidade - 1:
            self.inicio = 0
        self.numeros_elementos =-1
        return temp

    def primeiro(self):
        if self.__fila_vazia():
            return -1
        return self.valores[self.inicio]