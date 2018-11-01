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
	a = set(x)
	print a
	b = set(['a'])
	print a-b
	#c =set
        """for i in b:
	    if(i in a):
	        a.remove(i)
	print a
	"""
	return 0
	
		
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

	#Pesos de los nodos:
	eX = []
	eY = []
	for r in mat:
	    eX.append(max(r))
	    eY.append(0)
	print "x:"
	print x
	print "etiquetas de x: ",eX	

	print "y:"
	print y
	print "etiquetas de y: ",eY
	return	



	#vc: cubrimiento minimo de vertices
	m,vc = self.caminoAumentador()

	#Verificando si emparejamiento es perfecto
	verif = []
	for l in m:
	    verif.append(l[0])
	    verif.append(l[1])
	if (set(vc) == set(self.nodos)):
	    return m
	else:
	    #q: cubrimiento minimo
	    q = []
	    # Creando lista de lados iniciales
	    ladosIni = []
	    for maximo in eX:
		for l in self.soloLados:
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
	    #Paso iterativo dificil -------- Crear el nuevo G al ginal
	    while(len(q) < len(x)):
		m,vc = G.caminoAumentador()
		q = set(vc)
		r = set(x) & q
		t = set(y) & q
	
	

