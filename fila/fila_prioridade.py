import numpy as np

class FilaPrioridade():

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.numeros_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def __fila_vazia(self):
        return self.numeros_elementos == 0

    def __fila_cheia(self):
        return self.numeros_elementos == self.capacidade

    def enfileirar(self, valor):
        if self.__fila_cheia():
            print("Queue is full")
            return

        if self.numeros_elementos == 0:
            self.valores[self.numeros_elementos] = valor
            self.numeros_elementos += 1
        else:
            x = self.numeros_elementos - 1
            while x >= 0:
                if valor > self.valores[x]:
                    self.valores[x+1] = self.valores[x]
                else:
                    break
            self.valores[x+1] = valor
            self.numeros_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia():
            print("Queue is empty")
            return

        valor = self.valores[self.numeros_elementos - 1]
        self.numeros_elementos = -1
        return valor

    def primeiro(self):
        if self.__fila_vazia():
            return -1
        return self.valores[self.numeros_elementos - 1]


queue = FilaPrioridade(5)



queue.enfileirar(10)
queue.enfileirar(8)
queue.enfileirar(6)
queue.enfileirar(4)
queue.enfileirar(2)

queue.desenfileirar()

print(queue.primeiro())