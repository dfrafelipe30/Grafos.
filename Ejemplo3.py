#-*- coding: utf -8 -*-
from weightedGraph import weightedGraph
from ClaseGraph import Graph
#Grafos con pesos
#w = weightedGraph(['a','b','c','d'],[(('a','b'),10),(('b','c'),5),(('c','d'),4),(('d','a'),8),(('d','b'),3)])
#h : isomorfo a C4
h = weightedGraph(['a','b','c','d'],[(('a','b'),1),(('b','c'),2),(('c','d'),3),(('d','a'),4)])
#print w.MatrizDePesos()
print h.algoritmoHungaro()

#Grafos normales
g = Graph(['a','b','c','d'],[('a','b'),('b','c'),('c','d'),('d','a')])

