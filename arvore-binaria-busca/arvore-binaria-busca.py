class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def mostra_np(self):
        print(self.valor)

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        novo = No(valor)
        if self.raiz is None:
            self.raiz = novo
        else:
            atual = self.raiz

            while True:
                pai = atual
                # Adiciona à esquerda
                if valor < atual.valor:
                    atual = atual.esquerda
                    if atual is None:
                        pai.esquerda = novo
                        return
                # Adiciona à direita
                else:
                    atual = atual.direita
                    if atual is None:
                        pai.direita = novo
                        return


    def __is_empty(self, novo):
        if self.raiz is None:
            self.raiz = novo

if __name__ == "__main__":
    arvore = ArvoreBinariaBusca()

    arvore.inserir(53)
    arvore.inserir(30)
    arvore.inserir(14)
    arvore.inserir(39)
    arvore.inserir(9)
    arvore.inserir(23)
    arvore.inserir(34)
    arvore.inserir(49)
    arvore.inserir(72)
    arvore.inserir(61)
    arvore.inserir(84)
    arvore.inserir(79)

    print(arvore.raiz.esquerda.valor)
    print(arvore.raiz.direita.valor)


