import numpy as np

class Vetor:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)
        
    def imprime(self):
        if self.ultima_posicao == -1:
            print("Vetor is empty")
        else:
            for i in range(self.ultima_posicao+1):
                print(i, ' - ', self.valores[i])
                
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            return "Vector is full"
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor
            
    def bsucar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i
        return -1
            
    def excluir(self, valor):
        posicao = self.bsucar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            
            self.ultima_posicao += 1
            
array = Vetor(3)

array.insere(1)
array.insere(2)

print(array.bsucar(2))
