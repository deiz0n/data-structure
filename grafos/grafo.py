from grafos.vertice import Vertice
from grafos.adjacente import Adjacente
from pilha.pilha import Pilha


class Grafo:
    arad = Vertice('Arad')
    zerind = Vertice('Zerind')
    oradea = Vertice('Oradea')
    sibiu = Vertice('Sibiu')
    timisoara = Vertice('Temisoara')
    lugoj = Vertice('Lugoj')
    mehadia = Vertice('Mehadia')
    dobreta = Vertice('Dobreta')
    craiova = Vertice('Craiova')
    rimnicu = Vertice('Rimncu')
    fagares = Vertice('Fagares')
    pitesti = Vertice('Pitesti')
    bucharest = Vertice('Bucharest')
    giurgiu = Vertice('Giurgiu')

    arad.adiciona_adjacente(Adjacente(zerind, 75))
    arad.adiciona_adjacente(Adjacente(sibiu, 140))
    arad.adiciona_adjacente(Adjacente(timisoara, 118))

    zerind.adiciona_adjacente(Adjacente(arad, 75))
    zerind.adiciona_adjacente(Adjacente(oradea, 71))

    oradea.adiciona_adjacente(Adjacente(zerind, 71))
    oradea.adiciona_adjacente(Adjacente(sibiu, 151))

    sibiu.adiciona_adjacente(Adjacente(oradea, 151))
    sibiu.adiciona_adjacente(Adjacente(arad, 140))
    sibiu.adiciona_adjacente(Adjacente(fagares, 99))
    sibiu.adiciona_adjacente(Adjacente(rimnicu, 80))

    timisoara.adiciona_adjacente(Adjacente(arad, 118))
    timisoara.adiciona_adjacente(Adjacente(arad, 111))

    lugoj.adiciona_adjacente(Adjacente(timisoara, 111))
    lugoj.adiciona_adjacente(Adjacente(mehadia, 70))

    mehadia.adiciona_adjacente(Adjacente(lugoj, 70))
    mehadia.adiciona_adjacente(Adjacente(dobreta, 75))

    dobreta.adiciona_adjacente(Adjacente(mehadia, 75))
    dobreta.adiciona_adjacente(Adjacente(craiova, 120))

    craiova.adiciona_adjacente(Adjacente(dobreta, 120))
    craiova.adiciona_adjacente(Adjacente(pitesti, 138))
    craiova.adiciona_adjacente(Adjacente(rimnicu, 146))

    rimnicu.adiciona_adjacente(Adjacente(craiova, 146))
    rimnicu.adiciona_adjacente(Adjacente(sibiu, 80))
    rimnicu.adiciona_adjacente(Adjacente(pitesti, 97))

    fagares.adiciona_adjacente(Adjacente(sibiu, 99))
    fagares.adiciona_adjacente(Adjacente(bucharest, 211))

    pitesti.adiciona_adjacente(Adjacente(rimnicu, 97))
    pitesti.adiciona_adjacente(Adjacente(craiova, 138))
    pitesti.adiciona_adjacente(Adjacente(bucharest, 101))

    bucharest.adiciona_adjacente(Adjacente(fagares, 211))
    bucharest.adiciona_adjacente(Adjacente(pitesti, 101))
    bucharest.adiciona_adjacente(Adjacente(giurgiu, 90))

    class BuscaProfundidade:
        def __init__(self, inicio):
            self.inicio = inicio
            self.inicio.visitado = True
            self.pilha = Pilha(20)
            self.pilha.empilhar(inicio)

        def buscar(self):
            topo = self.pilha.ver_topo()
            print('Topo : {}'.format(topo.rotulo))
            for adjacente in topo.adjacentes:
                print(
                    'Topo é: {}. {} já foi visitado? {}'
                    .format(topo.rotulo,
                            adjacente.vertice.rotulo,
                            adjacente.vertice.visitado)
                )
                if adjacente.vertice.visitado is False:
                    adjacente.vertice.visitado = True
                    self.pilha.empilhar(adjacente.vertice)
                    print('Empilhou: {}'.format(adjacente.vertice.rotulo))
                    self.buscar()
            print('Desempilhou: {}'.format(self.pilha.desempilhar().rotulo))
            print()



