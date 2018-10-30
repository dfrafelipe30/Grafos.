#-*- coding: utf -8 -*-
from weightedGraph import weightedGraph
from ClaseGraph import Graph
#Grafos con pesos
#g = weightedGraph(['a','b','c','d'],[(('a','b'),10),(('b','c'),5),(('c','d'),4),(('d','a'),8),(('d','b'),3)])

#Grafos normales
g = Graph(['a','b','c','d'],[('a','b'),('b','c'),('c','d'),('d','a')])
print g.vecinos()
#print g.MatrizDePesos()
#x = g.Kruskal()
#print x.lados
