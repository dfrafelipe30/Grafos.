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

##    def vecinos(self):
##        d = {}
##	for u in self.nodos:
##	    x = []
##	    for v in self.nodos:
##	        if ((u,v) in self.lados or (v,u) in self.lados):
##		    x.append(v)
##            d[u] = x
##	return d

    def IsBipartite(self):
        dic = {}
        for k in self.lados:
            if(k[0] not in dicc):
                dicc[k[0]] = k[1]
            elif(k[0] in dicc):
                dicc[k[0]].append(k[1])
        visitidos = set()
        cola = [self.nodos[0]]
        while(cola):
            vertex = cola.pop(0)
            for w in dic[vertex]:
                if(w not in visitados):
                    visitados.add(w)
                    cola.append(w)
                else:
                    for z in permutations(dic[w]):
                        if(z in self.lados):
                            return False
        return True
    def Separacion(self):
        X = []
        Y = []
        for i in self.v:
            if(i in X and i not in Y):
                Y = Y + self.neighbors(i)
            elif(i not in X and i in Y):
                X = X + self.neighbors(i)
            else:
                X.append(i)
                Y = Y + self.neighbors(i)
        return (X,Y)
    
    def isEmparejado(self,emparejamiento,nodo):
        for i in emparejamiento:
            if( nodo in i):
                return True
        return False
    
    def Vecinos (self, u): #Retorna una lista de los vertices vecinos a 'u'
        neigh = []
        for i in self.e:
            if u in i:
                if i[0] == u: #Si u estÃ¡ en la primera posiciÃ³n de la tupla...
                    neigh.append(i[1])
                elif i[1] == u: #Si u estÃ¡ en la segunda posiciÃ³n de la tupla...
                    neigh.append(i[0])
        return neigh

    def aumentador(self,S,Empar,NNx):# S todos los elementos de X.
        T = set()
        emparejamiento = Empar
        for i in S:
            vecinos = self.Vecinos(i)
            for j in vecinos:
                if(not(self.isEmparejado(emparejamiento,j))):
                    for t in emparejamiento:
                        if(i in t):
                            emparejamiento.pop(emparejamiento.index(t))
                    emparejamiento.append((i,j))
                    S.remove(i)
                    return self.aumentador(S,emparejamiento,NNx)
                else:
                    for k in emparejamiento:
                        if(j == k[0] and k[1] not in S):
                            S.append(k[1])
                            
                        elif(j == k[1] and k[0] not in S):
                            S.append(k[0])
                            
                    T.add(j)
        cubrimiento = T|(set(NNx) - set(S))
        return (emparejamiento,cubrimiento)
    def CaminoAumentador(self):
        if(self.IsBipartite()):    
            X,Y = self.Separacion()
            NNx = list(set(X))
            NNx.sort()
            Nx = list(set(X))
            Nx.sort()
            Nx.pop(0)
            E,C = self.aumentador(Nx,[self.e[0]],NNx)
            return (E,C)
        else:
            print "ERROR"
