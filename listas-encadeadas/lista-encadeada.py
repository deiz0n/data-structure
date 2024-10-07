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