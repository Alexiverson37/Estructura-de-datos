
import numpy as np


filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))
matriz1 = np.random.randint(1, 6, size=(filas, columnas))
matriz2 = np.random.randint(1, 6, size=(filas, columnas))
matriz3 = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(matriz1[i][j] + matriz2[i][j])
    matriz3.append(fila)
# +
print("la suma es:")
for fila in matriz3:
    print(fila)
escalar = int(input("Ingrese un escalar del 1 al 10: "))


matriz4 = np.array(matriz3) * escalar
print("La matriz de la multiplicación por el escalar:")
print(matriz4)


filas2 = int(input("Ingrese las filas: "))
columnas2 = int(input("Ingrese las columnas: "))


matriz5 = []
print("Ingrese los numeros de la nueva matriz:")
for i in range(filas2):
    fila = []
    for j in range(columnas2):
        fila.append(int(input(f"Ingrese el elemento {i+1},{j+1}: ")))
    matriz5.append(fila)


matriz6 = np.dot(matriz4, matriz5)
print("La matriz final es:")
print(matriz6)