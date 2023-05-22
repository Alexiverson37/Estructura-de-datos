import random 
import numpy as np

matriz_3x3 = []

# Se determina que tanto la cantidad de filas como de columnas será de 3
for i in range(3):
	matriz_3x3.append( [0] * 3)
	
for i in range(3):
	for j in range(3):
		matriz_3x3[i][j] = int((random.randint(1,10)))

# Se imprime la primera matriz con sus elementos aleatorios de rango 1-10
print(f"Primera matriz {(matriz_3x3)}\n")

# Se transforma la matriz a un arreglo numpy
array_m3 = np.array(matriz_3x3)

# Se hace uso de linalg.det() de la biblioteca numpy para hallar la determinante
determinante = np.linalg.det(array_m3)

# Se limitan la cantidad de decimales para la determinante redondeada
determinante = np.around(determinante, decimals=10)

# Resultado final
print(f"La determinante de la matriz 3x3, es {determinante}\n")

