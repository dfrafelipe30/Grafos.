#-*- coding: utf -8 -*-
from ClaseGraph import Graph
#Ejemplos para algoritmo BFS

#Ejemplo 1 (el ejemplo visto en clase

G = Graph(["u","a","d","e","b","c"],[("u","a"),("a","d"),("d","e"),\
                                     ('u','b'),('b','c'),('c','e'),\
                                     ('a','c'),('b','d')])

#print G.distancia('u','e')

#Ejemplo 2 (K es C4 pero el nodo e está aislado)
K = Graph(['a','b','c','d','e'],[('a','b'),('b','c'),('c','d'),('a','d')])
#print K.distancia('a','d')
#print K.eccentricidad('e')
#print G.diametro()
#print K.diametro()
print G.radio()
print K.radio()
