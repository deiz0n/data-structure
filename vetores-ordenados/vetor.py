import numpy as np

class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)
        
    def imprime(self):
        if self.ultima_posicao == -1:
            print("Vector is empty")
        else:
            for i in range(self.ultima_posicao+1):
                print(i, " - ", self.valores[i])
                
    def insere(self, value):
        if (self.ultima_posicao == self.capacidade - 1):
            print("Array is full")
            return
           
        posicao = 0; 
        for i in range(self.ultima_posicao+1):
            posicao = i
            if value < self.valores[i]:
                break
            if i == self.ultima_posicao:
                posicao = i + 1
            
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x+1] = self.valores[x]
            x -= 1
            
        self.valores[posicao] = value
        self.ultima_posicao += 1
        
    def pesquisa_linear(self, value):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] > value:
                return -1
            if self.valores[i] == value:
                return i
        return -1        
        
    def pesquisa_binaria(self, value):
        limite_inferior = 0
        limite_superior = self.ultima_posicao
        
        while True:
            posicao_atual = int((limite_inferior + limite_superior) / 2)
            if value == self.valores[posicao_atual]:
                return posicao_atual
            elif limite_inferior > limite_superior:
                return -1
            else:
                if value > self.valores[posicao_atual]:
                    limite_inferior = posicao_atual + 1
                else:
                    limite_superior = posicao_atual - 1
        
    def excluir(self, value):
        posicao = self.pesquisa_linear(value)
        if (posicao == -1):
            return -1
        for i in range(posicao, self.ultima_posicao):
            self.valores[i] = self.valores[i + 1]
            
        self.ultima_posicao -= 1
            
        
        
        
vector = VetorOrdenado(3)

vector.insere(3)
vector.insere(2)
vector.insere(1)

print(vector.imprime())

print("-----")
print(vector.pesquisa_binaria(3))
