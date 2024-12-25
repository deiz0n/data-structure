from grafo import Grafo

if __name__ == '__main__':
    grafo = Grafo()

    busca_profundidade = Grafo.BuscaProfundidade(grafo.arad)
    busca_profundidade.buscar()
