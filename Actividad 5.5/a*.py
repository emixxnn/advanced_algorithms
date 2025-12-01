# Sergio Santiago Sánchez Salazar A01645255
# Emiliano Nuñez Felix A01645413

import heapq

class MazeSolver:
    def __init__(self, n, matrix):
        self.N = n
        self.grid = matrix
        self.directions = [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')] # formato: (cambio_fila, cambio_columna, caracter_movimiento)

    def heuristic(self, r, c):
        return abs(r - (self.N - 1)) + abs(c - (self.N - 1))

    def solve(self):
        if self.grid[0][0] == 0 or self.grid[self.N-1][self.N-1] == 0:
            return "Sin solucion (Inicio o Destino bloqueado)"
        pq = []
        visited = set()
        
        start_node = (0, 0)
        goal_node = (self.N - 1, self.N - 1)

        # Costos iniciales
        g_start = 0
        h_start = self.heuristic(0, 0)
        f_start = g_start + h_start

        # Añadir nodo inicial a la cola
        heapq.heappush(pq, (f_start, g_start, 0, 0, ""))
        visited.add(start_node)

        while pq:

            current_f, current_g, r, c, path = heapq.heappop(pq)

            # Si llegamos al destino, retornamos el camino
            if (r, c) == goal_node:
                return path

            # Explorar vecinos
            for dr, dc, move in self.directions:
                nr, nc = r + dr, c + dc

                # Verificar límites y si es caminable 
                if 0 <= nr < self.N and 0 <= nc < self.N:
                    if self.grid[nr][nc] == 1 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        
                        new_g = current_g + 1
                        new_h = self.heuristic(nr, nc)
                        new_f = new_g + new_h
                        
                        heapq.heappush(pq, (new_f, new_g, nr, nc, path + move))

        return "Sin solucion (No existe camino)"

def run_tests():
    print("--- INICIANDO PRUEBAS DE FUNCIONALIDAD Y CASOS EXTREMOS ---\n")

    print("CASO 1: Ejemplo Estándar")
    grid1 = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 1]
    ]
    solver1 = MazeSolver(4, grid1)
    print(f"Resultado: {solver1.solve()}\n")

    print("CASO 2: Muro Impasable (Sin Solución)")
    grid2 = [
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 0],  
        [0, 0, 1, 1]
    ]
    solver2 = MazeSolver(4, grid2)
    print(f"Resultado: {solver2.solve()}\n")

    print("CASO 3: Camino Largo (Zig-Zag)")
    grid3 = [
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1]
    ]
    solver3 = MazeSolver(5, grid3)
    print(f"Resultado: {solver3.solve()}\n")

    print("CASO 4: Destino Bloqueado")
    grid4 = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 0]  
    ]
    solver4 = MazeSolver(3, grid4)
    print(f"Resultado: {solver4.solve()}\n")

if __name__ == "__main__":
    run_tests()