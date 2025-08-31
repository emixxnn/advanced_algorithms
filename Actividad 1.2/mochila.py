# Emiiano Nuñez Félix A01645413

"""
En este archivo se encuentra la implementación del algoritmo de programación dinámica para el problema de la mochila.
El programa comienza creando una matriz de 0s de tamaño (n+1) x (W+1), donde n es el número de objetos y W es la capacidad máxima de 
la mochila.
Luego, llena la matriz utilizando una doble iteración: la primera itera sobre los objetos y la segunda sobre las capacidades de la
mochila.
Para cada objeto y cada capacidad, se verifica si el peso del objeto actual es menor o igual a la capacidad actual de la mochila. Si es
así, se decide si tomar o no el objeto, eligiendo la opción que maximiza el valor total. Si el peso del objeto es mayor que la 
capacidad, simplemente no se toma el objeto.
Finalmente, el valor máximo que se puede obtener con la capacidad W se encuentra en la posición dp[n][W] de la matriz.
"""

import numpy as np

def pd_mochila(w, v, W):
    n = len(w)
    # crea una matriz de 0s de tamaño (n+1) x (W+1)
    dp = np.zeros((n + 1, W + 1), dtype=int)
    
    # llenar la matriz
    for i in range(1, n + 1):
        # para cada capacidad de la mochila
        for weight in range(1, W + 1):
            # si el peso del objeto actual es menor o igual a la capacidad actual de la mochila 
            if w[i-1] <= weight:
                # o lo tomo o no lo tomo
                dp[i][weight] = max(dp[i-1][weight], dp[i-1][weight - w[i-1]] + v[i-1])
            # si no, no lo tomo
            else:
                dp[i][weight] = dp[i-1][weight]
    
    return dp[n][W]




    


    

