# Sergio Santiago Sanchez Salazar A01645255
# Emiliano Nuñez Felix A01645413

import heapq
import math

def mstPrim(distancias):
    n = len(distancias)
    visitado = [False] * n
    minHeap = [(0, -1, 0)] # Min heap con tuplas (peso, nodoOrigen, nodoDestino)
    mst = []

    while minHeap:
        peso, nodoOrigen, nodoDestino = heapq.heappop(minHeap)
        if not visitado[nodoDestino]:
            visitado[nodoDestino] = True
            if nodoOrigen != -1:
                mst.append((nodoOrigen, nodoDestino))

            for i in range(n):
                if not visitado[i] and distancias[nodoDestino][i] > 0:  # Un camino que no existe puede ser 0 o cualquier negativo por ejemplo -1
                    heapq.heappush(minHeap, (distancias[nodoDestino][i], nodoDestino, i))
                    
    return mst

def tspHeldKarp(distancias):
    n = len(distancias)
    memo = [[-1] * (1 << n) for _ in range(n)]
    # Guardamos en cada decision el siguiente nodo que visitamos para reconstruir el camino
    path_memo = [[-1] * (1 << n) for _ in range(n)] 
    costo_minimo = tspHelper(0, 1, distancias, memo, path_memo)

    # Reconstruir la ruta y convertir nodos a letras
    ruta = []
    curr = 0
    bitmask = 1
    
    # Empezamos en A (nodo 0).
    nodos_char = [chr(ord('A') + i) for i in range(n)]
    ruta.append(nodos_char[curr])

    for _ in range(n - 1):
        siguiente_nodo = path_memo[curr][bitmask]
        ruta.append(nodos_char[siguiente_nodo])
        bitmask = bitmask | (1 << siguiente_nodo)
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
        if bitmask & (1 << colonia) == 0: # Si la colonia no ha sido visitada 
            if distancias[curr][colonia] > 0: # Si hay camino
                dist = distancias[curr][colonia] + tspHelper(colonia, bitmask | (1 << colonia), distancias, memo, path_memo)
                if dist < minDist:
                    minDist = dist
                    path_memo[curr][bitmask] = colonia

    memo[curr][bitmask] = minDist
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
                    return True 
    return False

def flujoMaximoEdmondsKarp(flujos, inicio, fin):
    n = len(flujos)
    residual = [row[:] for row in flujos]
    flujoMaximo = 0
    padre = [-1] * n
    
    while bfs(residual, inicio, fin, padre):
        flujoCamino = float('inf')
        actual = fin
        while actual != inicio:
            flujoCamino = min(flujoCamino, residual[padre[actual]][actual])
            actual = padre[actual]

        siguiente = fin
        while siguiente != inicio:
            u = padre[siguiente]
            residual[u][siguiente] -= flujoCamino
            residual[siguiente][u] += flujoCamino
            siguiente = padre[siguiente]

        flujoMaximo += flujoCamino 

    return flujoMaximo

# corrección paso 4: En lugar de buscar pares cercanos entre sí, 
# buscamos qué central existente está más cerca de una nueva ubicación.
def encontrarCentralMasCercana(coordenadas, nueva_contratacion):
    minDist = float('inf')
    closestIndex = -1
    
    # Búsqueda lineal O(N) para encontrar el vecino más cercano (Voronoi)
    for i in range(len(coordenadas)):
        cx, cy = coordenadas[i]
        nx, ny = nueva_contratacion
        
        dx = cx - nx
        dy = cy - ny
        d = math.sqrt(dx * dx + dy * dy)
        
        if d < minDist:
            minDist = d
            closestIndex = i
            
    return closestIndex, minDist

def main():
    # Pedir inputs
    try:
        n_input = input("Numero de colonias: ").strip()
        if not n_input: return # Salir si está vacío
        n = int(n_input)
    except ValueError:
        print("Error: Ingrese un número entero válido.")
        return

    distancias = []
    print("Ingrese la matriz de adyacencia (distancias):")
    for _ in range(n):
        d = list(map(int, input().split()))
        distancias.append(d)

    flujos = []
    print("Ingrese la matriz de capacidades (flujos):")
    for _ in range(n):
        f = list(map(int, input().split()))
        flujos.append(f)

    coordenadas = []
    print("Ingrese las coordenadas (x, y) de las centrales:")
    for _ in range(n):
        # corrección: Limpiamos paréntesis y comas antes de leer
        line = input().strip().replace('(', '').replace(')', '').replace(',', ' ')
        x, y = map(float, line.split())
        c = (x, y)
        coordenadas.append(c)

    mst = mstPrim(distancias)
    print("\n1. Aristas del MST (Cableado Óptimo):")
    # corrección: Imprimir Letras (A-Z) en lugar de números
    for u, v in mst:
        nodo_u = chr(ord('A') + u)
        nodo_v = chr(ord('A') + v)
        print(f"{nodo_u} - {nodo_v}") 

    costo_minimo, ruta = tspHeldKarp(distancias)
    print(f"\n2. Costo minimo del TSP: {costo_minimo}")
    print("   Ruta del TSP:", " -> ".join(ruta))

    inicio = 0
    fin = n - 1
    flujo_maximo = flujoMaximoEdmondsKarp(flujos, inicio, fin)
    print(f"\n3. Flujo maximo entre colonia {chr(ord('A') + inicio)} y colonia {chr(ord('A') + fin)}: {flujo_maximo}")

    # corrección: Se pide input de la nueva ubicación para asignarle la central más cercana
    print("\nIngrese las coordenadas de la nueva contratación (x, y):")
    line = input().strip().replace('(', '').replace(')', '').replace(',', ' ')
    nx, ny = map(float, line.split())
    nueva_contratacion = (nx, ny)
    
    idx_cercana, dist_cercana = encontrarCentralMasCercana(coordenadas, nueva_contratacion)
    nombre_central = chr(ord('A') + idx_cercana)
    
    print(f"\n4. La central más cercana a la nueva contratación es: {nombre_central}")
    print(f"   Coordenadas de la central: {coordenadas[idx_cercana]}")
    print(f"   Distancia: {dist_cercana:.2f}")

if __name__ == "__main__":
    main()