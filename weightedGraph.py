class weightedGraph(object):
    def __init__(self,nodos,lados):
        self.nodos = nodos
        self.lados = lados
	sl = []
	for l in self.lados:
	    sl.append(l[0])
	self.SoloLados = sl

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

    def algoritmoHungaro(self):
	#Creamos la biparticion x,y
	lados = []
	for l in self.lados:
	    lados.append(l[0])
	
	
	n = self.nodos[0]
	x = [n]
	y = []
	for v in self.nodos:
	    if (((n,v) in lados or (v,n) in lados) and v not in x):
	        y.append(v)
	    else:
		x.append(v)
	x.pop(0)

	print "Los conjuntos X y Y son:"
	print "x: ",x
	print "y: ",y


	#############################
	
	
	#DIFERENCIA ENTRE CONJUNTOS a-b
	
		
	#############################

	#Construimos la matriz de pesos

	mat = []
	dicc = {}
        for v in self.lados:
            dicc[v[0]] = v[1]

	for xi in x:
	    reg = []
	    for yi in y:
                if((xi,yi) in lados):
		   reg.append(dicc[(xi,yi)])
		elif ((yi,xi) in lados):
		    reg.append(dicc[(yi,xi)])
	    mat.append(reg)
        print "matriz: ",mat
	#Pesos de los nodos:
	eX = []
	eY = []
	for r in mat:
	    eX.append(max(r))
	    eY.append(0)

	#diccionario de pesos en nodos:
	dicV = {}
	for i in range(len(x)):
            dicV[x[i]] = eX[i]
        for i in range(len(y)):
            dicV[y[i]] = eY[i]
        #print dicV
	#return
	

	#vc: cubrimiento minimo de vertices
	m,vc = self.caminoAumentador()

	#Verificando si emparejamiento inicial es perfecto
	verif = []
	for l in m:
	    verif.append(l[0])
	    verif.append(l[1])
	if (set(vc) == set(self.nodos)):
	    return m
	else:
	    #Q: cubrimiento minimo
	    Q = []
	    # Creando lista de lados iniciales
	    ladosIni = []
	    for maximo in eX:
		for l in self.SoloLados:
		    if((l,maximo) in self.lados):
		        ladosIni.append((l,maximo))
	
	    #Creando lista de nodos iniciales
	    nodosIni = []
	    for l in ladosIni:
		for v in l[0]:
		    nodos.append(v)
	    nodosIni = list(set(nodosIni))
	    
	    #Creacion de Grafo inicial.
	    G = weightedGraph(nodosIni,ladosIni)
	    #Paso iterativo dificil -------- Crear el nuevo G al final
	    while(len(Q) < len(x)):
                print "-----------------------------"
                print "len(Q): ",len(Q)
		m,vc = G.caminoAumentador()
                #Verificando si emparejamiento inicial es perfecto
                verif = []
                for l in m:
                    verif.append(l[0])
                    verif.append(l[1])
                if (set(vc) == set(self.nodos)):
                    return m
		Q = set(vc)
		R = set(x) & Q
		T = set(y) & Q
		
		XnoR = set(x)-R
		YnoT = set(y)-T
		
		#Marcando las filas y columnas por ignorar para EXCESOS
		excesos = []
		for i in range(len(x)):
                    if x[i] not in Q:
                        for j in range(len(y)):
                            if y[j] not in Q:
                                E = dicV[x[i]] + dicV[y[j]] - mat[i][j]
                                excesos.append(E)
                E = min(excesos)

                #Disminuimos a E a todos los v en X-R y sumamos E a los y en T
                for v in dicV.keys():
                    if v in XnoR:
                        dicV[v] = dicV[v] - E
                    elif v in T:
                        dicV[v] = dicV[v] + E
                #Finalmente creamos el nuevo G a partir de los nuevos pesos de los vertices
                nuevosNodos = []
                nuevosLados = [] #parejas lado-peso

                #Nuevos lados
                for i in range(len(x)):
                    for j in range(len(y)):
                        if ((dicV[x[i]] + dicV[y[j]] - mat[i][j]) == 0):
                            if ((x[i],y[j]),mat[i][j]) in self.lados:
                                nuevosLados.append(((x[i],y[j]),mat[i][j]))
                            elif ((y[j],x[i]),mat[i][j]) in self.lados:
                                nuevosLados.append(((y[j],x[i]),mat[i][j]))
                # Nuevos nodos:
                for l in nuevosLados:
                    if l[0][0] not in nuevosNodos:
                        nuevosNodos.append(l[0][0])
                    elif l[0][1] not in nuevosNodos:
                        nuevosNodos.append(l[0][1])

                G = weightedGraph(nuevosNodos,nuevosLados)

            print "se ha encontrado un emparejamiento perfecto (y un cubrimiento minimo de vertices)"
