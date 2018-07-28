from Graph import Graph

G = Graph(["a","b","c"],[("a","b"),("b","c")])
print G.AdjacencyMatrix()

H = Graph(["d","e","f"], [("a","b"),("e","f")])

print H.AdjacencyMatrix()
