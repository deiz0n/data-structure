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
        self.ligacoes = []

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
                        self.ligacoes.append(str(pai.valor) + "->" + str(novo.valor))
                        return
                # Adiciona à direita
                else:
                    atual = atual.direita
                    if atual is None:
                        pai.direita = novo
                        self.ligacoes.append(str(pai.valor) + "->" + str(novo.valor))
                        return


    def pesquisar(self,valor):
        atual = self.raiz
        while atual.valor != valor:
            if valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita
            if atual is None:
                return None
        return atual

    # Raiz, esquerda e direita
    def pre_ordem(self,no):
        if no is not None:
            print(no.valor)
            self.pre_ordem(no.esquerda)
            self.pre_ordem(no.direita)

    # Esquerda, raiz e direita
    def em_ordem(self, no):
        if no is not None:
            self.em_ordem(no.esquerda)
            print(no.valor)
            self.pre_ordem(no.direita)

    # Esquerda, direita e raiz
    def pos_ordem(self, no):
        if no is not None:
            self.pos_ordem(no.esquerda)
            self.pos_ordem(no.direita)
            print(no.valor)

    #Excluir um nó folha
    def excluir(self, valor):
        if self.raiz is None:
            print("A árvore está vazia")
            return

        atual = self.raiz
        pai = self.raiz
        e_esquerda = True
        while atual.valor != valor:
            pai = atual
            #Esquerda
            if valor < atual.valor:
                e_esquerda = True
                atual = atual.esquerda
            #Direita
            else:
                e_esquerda = False
                atual = atual.direita
            if atual is None:
                return False

        # O nó a ser apagado é uma folha
        if atual.esquerda is None and atual.direita is None:
            if atual == self.raiz:
                self.raiz = None
            elif e_esquerda is True:
                pai.esquerda = None
            else:
                pai.direita = None

        # O nó a ser apagado não possui filho na direita
        elif atual.direita is None:
            if atual == self.raiz:
                self.raiz = atual.esquerda
            elif e_esquerda is True:
                pai.esquerda = atual.esquerda
            else:
                pai.direita = atual.esquerda
        # O nó a ser apagado não possui filho na direita
        elif atual.esquerda is None:
            if atual == atual.raiz:
                self.raiz = atual.direita
            elif e_esquerda is True:
                pai.esquerda = atual.direita
            else:
                pai.direita = atual.direita

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

    print(arvore.pesquisar(18))
    print(arvore.pos_ordem(arvore.raiz))

    print(arvore.excluir(18))
    print("----")
    print(arvore.pos_ordem(arvore.raiz))
