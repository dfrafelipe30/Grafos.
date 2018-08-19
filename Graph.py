from itertools import permutations 
import logging

class Graph(object):
    def __init__(self,nodos,lados):
        for lado in lados:
            for nodo in lado:
                assert nodo in nodos ,\
                       'El lado debe ser un lado valido'
        self.nodos =  nodos
        self.lados = lados

    def AdjacencyMatrix(self):
        MatrizDeAdjacencia = []
        for nodoA in self.nodos:
            temp = []
            for nodoB in self.nodos:
                if((nodoA,nodoB) in self.lados or (nodoB,nodoA) in self.lados):
                    temp.append(1)
                else:
                    temp.append(0)
            MatrizDeAdjacencia.append(temp)
        return MatrizDeAdjacencia

    def IsIsomorphTo(self,grafo):
        contador = 0
        if(len(self.nodos)==len(grafo.nodos) and len(self.lados) == len(grafo.lados)):
            for i in self.AdjacencyMatrix():
                permutaciones = []
                for p in permutations(i):
                    permutaciones.append(p)
                if(not(tuple(grafo.AdjacencyMatrix()[contador]) in permutaciones)):
                    return False
                else:
                    contador = contador + 1
            return True
        else:
            return False
    
    
    
