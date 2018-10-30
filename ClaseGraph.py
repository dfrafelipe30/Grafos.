#-*- coding: utf -8 -*-
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

    def distancia(self,u,v):
        #devuelve la distancia entre los nodos u y v del grafo G.
        #Si alguno de los dos nodos no existe devuelve Error.
        #Si la distancia es infinita devuelve -1.

        assert u in self.nodos,\
               "ERROR, revise los nodos ingresados. "
        assert v in self.nodos,\
               "ERROR, revise los nodos ingresados. "
            

        r = {u}
        s = set()
        
        #Diccionario de distancias desde u hasta todos los nodos del grafo
        d = {u:0}
        for n in self.nodos:
            d[n] = 0

                
        while(len(r) != 0):
            #nodo: primer elemento en r
            for nodo in r:
                #Vertice es z, posible vecino de nodo
                for vertice in self.nodos:
                    if(vertice not in r|s):
                        if((nodo,vertice) in self.lados or (vertice,nodo) in self.lados):
                            #Si vertice es un vecino de nodo se agrega a r
                            r = r|{vertice}
                            d[vertice] = d[nodo] + 1
                        else:
                            #En el caso de que vertice no sea alcanzable desde u
                            d[vertice] = -1
                            
            #quitamos el primer elemento de r y se lo ponemos a s               
            r.remove(nodo)
            s = s.union({nodo})

        return (d[v])

    def eccentricidad(self,u):
        assert u in self.nodos,\
               "ERROR, revise el nodo ingresado."

        distancias = []
        #Creamos la lista de todas las distancias
        for v in self.nodos:
            distancias.append(self.distancia(u,v))

        #Busqueda lineal de la distancia máxima
        dmax = distancias[0]
        for d in distancias:
            if d == -1:
                return -1
            elif d > dmax :
                dmax = d

        return dmax

    def diametro(self):
        distancias = []
        for v in self.nodos:    
            if self.eccentricidad(v) == -1:
                #En el caso que el diametro sea infinito
                return -1
            distancias.append(self.eccentricidad(v))
        #Busqueda lineal de las distancias
        dmax = distancias[0]
        for d in distancias:
            if d > dmax:
               dmax = d

        return dmax
        
    def radio(self):
        #E: Eccentricidades
        E = []
        for v in self.nodos:    
            if self.eccentricidad(v) == -1:
                #En el caso que el radio sea infinito
                return -1
            E.append(self.eccentricidad(v))
        #Busqueda lineal de la eccentricidad mínima
        eMin = E[0]
        for e in E:
            if e < eMin:
                eMin = e
        return eMin        

    def conectado(self):
        aux = self.nodos[0]
        for nodoActual in self.nodos:
            if(self.distancia(aux,nodoActual) == -1):
                return False
        return True
    def esArbol(self):
        if(self.conectado() and len(self.lados) == len(self.nodos) - 1):
            return True
        else:
            return False
    def Euleriano(self):
        aux = self.AdjacencyMatrix()
        for i in aux:
            suma = 0
            for j in i:
                suma = suma + j
            if(suma % 2 == 1):
                return False
        return True

    def vecinos(self):
        d = {}
	for u in self.nodos:
	    x = []
	    for v in self.nodos:
	        if ((u,v) in self.lados or (v,u) in self.lados):
		    x.append(v)
            d[u] = x
	return d
        
