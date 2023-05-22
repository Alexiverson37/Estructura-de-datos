import numpy as np

# Matriz identidad de similar dimensión a la matriz A
matriz_identidad = np.array([[1, 0], 
                             [0,1]]) 

# Matriz A de dimensiones 2 por 2
matriz_A = np.array([[1, 2], [3, 4]])

print(f"La matriz A, es: {matriz_A}\n")

# Función de numpy que obtiene la inversa de una matriz
inversa_A = np.linalg.inv(matriz_A) 

print(f"La inversa de la matriz A, es: {inversa_A}\n")

# Multiplicación de matrices 
producto = np.matmul(matriz_A, inversa_A)

# Se limitan la cantidad de decimales para obtener la matriz identidad
producto = np.around(producto, decimals=10) 

# Producto de matriz A por su inversa
print(f"El producto de A por su inversa, es: {producto}\n")

# Comprobación de propiedad matricial
print(f"Se comprueba que una matriz multiplicada por su inversa, entrega la matriz identidad, ya que producto == matriz_identidad.")
