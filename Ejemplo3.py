#-*- coding: utf -8 -*-
from weightedGraph import weightedGraph
from ClaseGraph import Graph
#Grafos con pesos
#w = weightedGraph(['a','b','c','d'],[(('a','b'),10),(('b','c'),5),(('c','d'),4),(('d','a'),8),(('d','b'),3)])
h = weightedGraph(['a','b','c','d','e'],[(('a','d'),10),(('a','e'),10),(('b','d'),10),(('b','e'),10),(('c','d'),10),(('c','e'),10)])
#print w.MatrizDePesos()
h.algoritmoHungaro()

#Grafos normales
g = Graph(['a','b','c','d'],[('a','b'),('b','c'),('c','d'),('d','a')])

