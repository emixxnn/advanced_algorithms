# Sergio Santiago Sánchez Salazar A01645255
# Emiliano Nuñez Felix A01645413

import random
import math
import matplotlib.pyplot as plt

def f(x):
    return (-(x**4) + (4*(x**3)) - (10*(x**2)) + (8*x))

def mejoraIterativa(domain, step, n):
    print("Mejora Iterativa: \n" )
    x = random.uniform(domain[0], domain[1])
    best = (x, f(x))
    visitados = [x]
    decision = False
    for i in range(n):
        vecino = x + random.uniform(-step, step)
        if vecino < domain[0]:
            vecino = domain[0]
        if vecino > domain[1]:
            vecino = domain[1]
        visitados.append(vecino)
        if f(vecino) > f(x):
            x = vecino
            best = (x, f(x))    
            decision = True
        else:
            decision = False

        print(f"Iteracion {i+1}: x = {x}, f(x) = {f(x)}, vecino = {vecino}, f(vecino) = {f(vecino)}, decision = {"Cambiar" if decision else "No Cambiar"}")
    return (best, visitados)

def hillClimbing(domain, step, n):
    print("Hill Climbing: \n")
    x = random.uniform(domain[0], domain[1])
    best = (x, f(x))
    visitados = [x]
    decision = "Inicio"
    for i in range(n):
        vecinoIzq = x - step
        vecinoDer = x + step
        if vecinoIzq < domain[0]:
            vecinoIzq = domain[0]
        if vecinoDer > domain[1]:
            vecinoDer = domain[1]
        if f(vecinoIzq) >= f(vecinoDer) and f(vecinoIzq) > f(x):
            x = vecinoIzq
            best = (x, f(x))
            decision = "cambiar a izquierdo"
        elif f(vecinoDer) > f(vecinoIzq) and f(vecinoDer) > f(x):
            x = vecinoDer
            best = (x, f(x))
            decision = "cambiar a derecho"
        else:
            decision = "no hay mejora (break)"
            break

        visitados.append(x)
        print(f"Iteracion {i+1}: x = {x}, f(x) = {f(x)}, vecinoIzq = {vecinoIzq}, f(vecinoIzq) = {f(vecinoIzq)}, vecinoDer = {vecinoDer}, f(vecinoDer) = {f(vecinoDer)}, decision = {decision}")
    return (best, visitados)

def simulatedAnnealing(domain, step, n):
    print("Simulated Annealing: \n")
    x = random.uniform(domain[0], domain[1])
    best = (x, f(x))
    visitados = [x]
    T = 100.0
    alpha = 0.95
    decision = "Inicio"
    for i in range(n):
        vecino = x + random.uniform(-step, step)
        if vecino < domain[0]:
            vecino = domain[0]
        if vecino > domain[1]:
            vecino = domain[1]
        deltaE = f(vecino) - f(x)
        if deltaE > 0:
            x = vecino
            decision = "cambiar a vecino (mejora)"
        else:
            probabilidad = math.exp(deltaE / T)
            if random.random() < probabilidad:
                x = vecino
                decision = "cambiar a vecino (probabilidad)"
            else:
                decision = "no cambiar"

        if f(x) > best[1]:
            best = (x, f(x))

        visitados.append(x)
        T = T * alpha
        print(f"Iteracion {i+1}: x = {x}, f(x) = {f(x)}, vecino = {vecino}, f(vecino) = {f(vecino)}, T = {T}, probabilidad = {probabilidad if deltaE <= 0 else 'N/A'}, decision = {decision}")
    return (best, visitados)
        
def main():
    n = input("Introduce el numero de iteraciones: ")
    step = input("Introduce el tamaño del step: ")
    domain = [-2, 4]
    n = int(n)
    step = float(step)
    maxMI, visitadosMI = mejoraIterativa(domain, step, n)
    maxHC, visitadosHC = hillClimbing(domain, step, n)
    maxSA, visitadosSA = simulatedAnnealing(domain, step, n)
    print("Mejora Iterativa: ", maxMI)
    print("Hill Climbing: ", maxHC)
    print("Simulated Annealing: ", maxSA)
    x = [i * 0.1 for i in range(-20, 41)]
    y = [f(i) for i in x]
    plt.plot(x, y, label='f(x)')
    plt.scatter(maxMI[0], maxMI[1], color='orange', label='Mejora Iterativa Maxima', s=50)
    plt.scatter(visitadosMI, [f(i) for i in visitadosMI], color='red', label='Mejora Iterativa', s=10)
    plt.scatter(maxHC[0], maxHC[1], color='violet', label='Hill Climbing Maxima', s=50)
    plt.scatter(visitadosHC, [f(i) for i in visitadosHC], color='green', label='Hill Climbing', s=10)
    plt.scatter(maxSA[0], maxSA[1], color='cyan', label='Simulated Annealing Maxima', s=50)
    plt.scatter(visitadosSA, [f(i) for i in visitadosSA], color='blue', label='Simulated Annealing', s=10)
    plt.legend()
    plt.title('Optimization Algorithms Comparison')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()  
    return 0

main()


'''
¿Cuál algoritmo llegó más cerca del óptimo global?
En la mayoria de ejecuciones hill climbing tiende a llegar de forma mas rapida a un óptimo cercano y quedarse ahi.
¿Cuál exploró más el espacio?
Simulated annealing explora más ya que aunque llegue a un óptimo sigue buscando hacia ambos lados por mejores soluciones, distinto de hill climbing y el iterativo que 
que se mueven rapidamente al óptimo local y se quedan ahi.
¿Cuántas iteraciones aprox son necesarias para llegar a la meta en cada algoritmo?
Hill climbing suele llegar en menos iteraciones, seguido de mejora iterativa y finalmente simulated annealing que puede tomar más tiempo debido a su naturaleza exploratoria.
'''