import heapq

def dijkstra(matrix):
    n = len(matrix)
    origin = n - 1
    distances = [float('inf')] * n
    distances[origin] = 0
    
    queue = [(0, origin)]
    
    while queue:
        currDist, currNode = heapq.heappop(queue)
        
        if currDist > distances[currNode]:
            continue
            
        for neighbor in range(n):
            weight = matrix[currNode][neighbor]
            if weight > 0 and weight != float('inf'):
                distance = currDist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))
                    
    return distances

def floydWarshall(matrix):
    n = len(matrix)
    dist = [row[:] for row in matrix]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] +dist[k][j]

    return dist


def main():
    n = int(input())
    matrix = []
    for _ in range(n):
        row = input().split()
        row = [int(x) for x in row]
        matrix.append(row)

    matrixFloyd = floydWarshall(matrix)
    print(matrixFloyd)
    distances = dijkstra(matrix)
    print(f"Shortest distances from node {n}:")
    for i, d in enumerate(distances):
        print(f"To node {i+1}: {d}")

main()