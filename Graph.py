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
    
    
    
