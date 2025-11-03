# Sergio Santiago Sanchez Salazar A01645255
# Emiliano Nuñez Felix A01645413

import heapq
import math

def mstPrim(distancias):
    n = len(distancias)
    visitado = [False] * n
    minHeap = [(0, -1, 0)] #Min heap con tuplas (peso, nodoOrigen, nodoDestino)
    mst = []

    while minHeap:
        peso, nodoOrigen, nodoDestino = heapq.heappop(minHeap)
        if not visitado[nodoDestino]:
            visitado[nodoDestino] = True
            if nodoOrigen != -1:
                mst.append((nodoOrigen, nodoDestino))

            for i in range(n):
                if not visitado[i] and distancias[nodoDestino][i] > 0: #Un camino que no existe puede ser 0 o cualquier negativo por ejemplo -1
                    heapq.heappush(minHeap, (distancias[nodoDestino][i], nodoDestino, i))
                    
    return mst

def tspHeldKarp(distancias):
    n = len(distancias)
    memo = [[-1] * (1 << n) for _ in range(n)]
    path_memo = [[-1] * (1 << n) for _ in range(n)] #Guardamos en cada decision el siguiente nodo que visitamos para reconstruir el camino al final
    costo_minimo = tspHelper(0, 1, distancias, memo, path_memo)


    # Codigo generado con apoyo de IA para reconstruir la ruta y convertir nodos a letras
    ruta = []
    curr = 0
    bitmask = 1
    
    # Empezamos en A (nodo 0).
    nodos_char = [chr(ord('A') + i) for i in range(n)]
    ruta.append(nodos_char[curr])

    for _ in range(n - 1):
        # Obtenemos el siguiente mejor paso guardado en la tabla
        siguiente_nodo = path_memo[curr][bitmask]
        
        ruta.append(nodos_char[siguiente_nodo])
        
        bitmask = bitmask | (1 << siguiente_nodo) # "Encendemos" el bit del nodo visitado
        curr = siguiente_nodo

    # Agregar el regreso al inicio
    ruta.append(nodos_char[0])

    return costo_minimo, ruta

def tspHelper(curr, bitmask, distancias, memo, path_memo):
    n = len(distancias)

    if bitmask == (1 << n) - 1:
        return distancias[curr][0]
    
    if memo[curr][bitmask] != -1:
        return memo[curr][bitmask]
    
    minDist = float('inf')

    for colonia in range(n):
        if bitmask & (1 << colonia) == 0: #Si la colonia no ha sido visitada 
            if distancias[curr][colonia] > 0: #Si hay camino entre las dos colonias
                dist = distancias[curr][colonia] + tspHelper(colonia, bitmask | (1 << colonia), distancias, memo, path_memo)
                if dist < minDist:
                    minDist = dist
                    path_memo[curr][bitmask] = colonia #Guardamos el siguiente nodo a visitar para esta combinacion de curr y bitmask


    memo[curr][bitmask] = minDist #Guardamos la distancia minima para llegar a este nodo con los nodos visitados en bitmask
    return minDist

def bfs(residual, inicio, fin, padre):
    n = len(residual)
    visitado = [False] * n
    cola = []
    cola.append(inicio)
    visitado[inicio] = True

    while cola:
        u = cola.pop(0)

        for v in range(n):
            if not visitado[v] and residual[u][v] > 0:
                cola.append(v)
                visitado[v] = True
                padre[v] = u
                if v == fin:
                    return True #Si existe un camino 
    return False #No existe un camino 

def flujoMaximoEdmondsKarp(flujos, inicio, fin):
    n = len(flujos)
    residual = [row[:] for row in flujos]
    flujoMaximo = 0
    padre = [-1] * n
    while bfs(residual, inicio, fin, padre): #Mientras exista un camino del nodo inicio al nodo fin
        flujoCamino = float('inf')
        actual = fin
        while actual != inicio: # Encontrar el flujo minimo en el camino
            flujoCamino = min(flujoCamino, residual[padre[actual]][actual])
            actual = padre[actual]

        siguiente = fin
        while siguiente != inicio: # Actualizar el grafo residual permitiendo encontrar mejores caminos
            u = padre[siguiente]
            residual[u][siguiente] -= flujoCamino
            residual[siguiente][u] += flujoCamino
            siguiente = padre[siguiente]

        flujoMaximo += flujoCamino 

    return flujoMaximo

def busquedaGeometrica(coordenadas): #Busqueda geometrica como la hicimos en la actividad pasada
    l = len(coordenadas)
    mid = l // 2
    coordenadas = sorted(coordenadas, key=lambda coord: coord[0])
    L = coordenadas[:mid]
    R = coordenadas[mid:]
    minDistL = float('inf')
    minDistLCords = None
    minDistR = float('inf')
    minDistRCords = None
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            dx = L[i][0] - L[j][0]
            dy = L[i][1] - L[j][1]
            d = math.sqrt(dx * dx + dy * dy)
            if d < minDistL:
                minDistL = d
                minDistLCords = (L[i], L[j])


    for i in range(len(R)):
        for j in range(i + 1, len(R)):
            dx = R[i][0] - R[j][0]
            dy = R[i][1] - R[j][1]
            d = math.sqrt(dx * dx + dy * dy)
            if d < minDistR:
                minDistR = d
                minDistRCords = (R[i], R[j])

    globalMinDist = min(minDistL, minDistR)
    stripMinDist = float('inf')
    stripMinCords = None
    xMid = coordenadas[mid][0]
    xMinStrip = xMid - globalMinDist
    xMaxStrip = xMid + globalMinDist
    stripCoords = [coord for coord in coordenadas if xMinStrip <= coord[0] <= xMaxStrip]
    stripCoords = sorted(stripCoords, key=lambda coord: coord[1])

    for i in range(len(stripCoords)):
        for j in range(i + 1, len(stripCoords)):
            if (stripCoords[j][1] - stripCoords[i][1]) >= globalMinDist:
                break
            dx = stripCoords[i][0] - stripCoords[j][0]
            dy = stripCoords[i][1] - stripCoords[j][1]
            d = math.sqrt(dx * dx + dy * dy)
            if d < stripMinDist:
                stripMinDist = d
                stripMinCords = (stripCoords[i], stripCoords[j])

    globalMinDist = min(globalMinDist, stripMinDist)
    closestPairs = []
    if globalMinDist == minDistL:
        closestPairs = [minDistLCords]
    if globalMinDist == minDistR:
        closestPairs = [minDistRCords]
    if globalMinDist == stripMinDist:
        closestPairs = [stripMinCords]

    return closestPairs, globalMinDist

def main():
    # Pedir inputs
    n = int(input("Numero de colonias: "))
    distancias = []
    for _ in range(n):
        d = list(map(int, input().split()))
        distancias.append(d)

    flujos = []
    for _ in range(n):
        f = list(map(int, input().split()))
        flujos.append(f)

    coordenadas = []
    for _ in range(n):
        x, y = map(float, input().split())
        c = (x, y)
        coordenadas.append(c)

    # Paso 1 forma de cablear colonias
    mst = mstPrim(distancias)
    print("\nAristas del MST:")
    for u, v in mst:
        print(f"{u} - {v}") 

    # Paso 2 ruta del viajero por todas las colonias
    costo_minimo, ruta = tspHeldKarp(distancias)
    print(f"\nCosto minimo del TSP: {costo_minimo}")
    print("Ruta del TSP:", " -> ".join(ruta))

    # Paso 3 Flujo maximo de datos entre colonia inicial y final
    inicio = 0
    fin = n - 1
    flujo_maximo = flujoMaximoEdmondsKarp(flujos, inicio, fin)
    print(f"\nFlujo maximo entre colonia {inicio} y colonia {fin}: {flujo_maximo}")

    
    # Paso 4 Colonias mas cercanas con busqueda geometrica    
    closestPairs, minDist = busquedaGeometrica(coordenadas)
    print(f"\nDistancia minima entre colonias: {minDist}")
    print("Pares de colonias mas cercanas:")
    for pair in closestPairs:
        print(f"{pair[0]} - {pair[1]}")

if __name__ == "__main__":
    main()