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
        #Este metodo crea una lista de listas que representa
        #la matriz de adyacencia del grafo.
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
        #Este metodo confirma si el grafo por parametro es isomorfo al grafo al cual
        #pertenece este metodo

        
        contador = 0
        #El primer if verifica si la cantidad de lados y de vertices son iguales
        if(len(self.nodos)==len(grafo.nodos) and len(self.lados) == len(grafo.lados)):
            for i in self.AdjacencyMatrix():
                permutaciones = []
                #Se verifica renglon por renglon de la matriz si permutando
                #los elementos de un renglon se puede obtener el mismo renglon de
                #la otra matriz
                for p in permutations(i):
                    permutaciones.append(p)
                if(not(tuple(grafo.AdjacencyMatrix()[contador]) in permutaciones)):
                    return False
                else:
                    contador = contador + 1
            return True
        else:
            return False
        
    
    
