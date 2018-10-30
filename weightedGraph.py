class weightedGraph(object):
    def __init__(self,nodos,lados):
        self.nodos = nodos
        self.lados = lados

    def MatrizDePesos(self):
        dicc = {}
        for v in self.lados:
            dicc[v[0]] = v[1]
        matriz = []
        for i in self.nodos:
            aux = []
            for j in self.nodos:
                if(dicc.has_key((i,j)) or dicc.has_key((j,i))):
                   if(dicc.has_key((i,j))):
                      aux.append(dicc[(i,j)])
                   else:
                      aux.append(dicc[(j,i)])
                elif(i == j):
                      aux.append(0)
                else:
                      aux.append(-1)
            matriz.append(aux)
        return (matriz)

    def Kruskal(self):
        dicc = {}
        for v in self.lados:
            dicc[v[0]] = v[1]
        minPesos = sorted(dicc.values())
        nodosNuevos = []
        nuevosLados = {}
        comp = [i for i in range(len(self.nodos))]
        d = {}

        #componentes
        for j in range(len(self.nodos)):
            d[comp[j]] = self.nodos[j]
        
        for w in minPesos:
            for l in self.lados:
                if (l[1]==w):
                    x=l[0]

                    #for n in x:
                    if((x[0] not in nodosNuevos) or (x[1] not in nodosNuevos)):
                        if(x[0] not in nodosNuevos and x[1] in nodosNuevos):
                            nodosNuevos.append(x[0])
                            nuevosLados[l[0]] = l[1]
                        elif(x[1] not in nodosNuevos and x[0] in nodosNuevos):
                            nodosNuevos.append(x[1])
                            nuevosLados[l[0]] = l[1]
                        elif(x[1] not in nodosNuevos and x[0] not in nodosNuevos):
                            nodosNuevos.append(x[0])
                            nodosNuevos.append(x[1])
                            nuevosLados[l[0]] = l[1]

                    if (len(nodosNuevos)==len(self.nodos) and len(nuevosLados)==len(self.lados)-1):
                        break


        listaLados = []
        for k in nuevosLados.keys():
            listaLados.append((k,nuevosLados[k]))
        G = weightedGraph(nodosNuevos,listaLados)

        return G
	
    def vecinos(self):
        d = {}
	for u in self.nodos:
	    x = []
	    for v in self.nodos:
	        if ((u,v) in self.lados):
		    x.append((u,v))
		elif((v,u) in self.lados):
		    x.append((v,u))
	    print x
            d[u] = x
	return d
