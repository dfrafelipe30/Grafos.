from Graph import Graph

G = Graph(["a","b","c"],[("a","b"),("b","c")])
print G.AdjacencyMatrix()

J = Graph(["a","b","c","d"],[("a","b"),("b","c"),("c","d")])
print J.AdjacencyMatrix()

K =Graph(["e","f","g","h"],[("e","g"),("g","f"),("f","h")])
print K.AdjacencyMatrix()


#Grafo que  genera error.
#H = Graph(["d","e","f"], [("a","b"),("e","f")])
#print H.AdjacencyMatrix()
