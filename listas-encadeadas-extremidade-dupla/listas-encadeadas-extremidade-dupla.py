class No:
    def __init__(self, value):
        self.value = value
        self.proximo = None

    def mostra_no(self):
        print(self.value)

class ListaEncadeadaExtremidadeDupla():
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def insere_inicio(self, value):
        novo = No(value)
        if self.__is_empty():
            self.ultimo = novo
        novo.proximo = self.primeiro
        self.primeiro = novo

    def insere_final(self, value):
        novo = No(value)
        if self.__is_empty():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo
        self.ultimo = novo

    def excluir_inicio(self):
        if self.__is_empty():
            print("List is empty")
            return
        temp = self.primeiro
        if self.primeiro.proximo is None:
            self.ultimo = None
        self.primeiro = self.primeiro.proximo
        return temp

    def mostrar(self):
        if self.__is_empty():
            print("List is empty")
            return
        atual = self.primeiro
        while atual is not None:
            atual.mostra_no()
            atual = atual.proximo

    def __is_empty(self):
        return self.primeiro is None