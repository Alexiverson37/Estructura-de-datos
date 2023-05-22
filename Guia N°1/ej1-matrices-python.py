# Matriz ejemplar para hacer uso de las posteriores funciones
matriz1 = [[1,2,3,4,5],
	       [1,2,3,4,5],
           [1,2,3,4,5],
	       [1,2,3,4,5],
           [1,2,3,4,5]]

print(f"La matriz es {matriz1}.")

# Obtener el número de columnas
nColumnas = len(matriz1[0])

# Para almacenar la suma de los elementos de cada columna
sumaColumnas = [0] * nColumnas

# Algoritmo que suma los elementos de cada columna
for fila in matriz1:
    for i, elemento in enumerate(fila): # Enumerate sirve para iterar sobre una secuencia y obtener el el índice y valor del elemento
        sumaColumnas[i] += elemento

print(f"La suma de todos los elementos de cada columna de la matriz, es {sumaColumnas}.")

# Función que suma los elementos de cada fila
def sumaElementosFilas(matriz):
    sumaFilas = []
    for fila in matriz:
        sumaFila = sum(fila)
        sumaFilas.append(sumaFila)
    return sumaFilas
print(f"La suma de todos los elementos de cada fila de la matriz, es {sumaElementosFilas(matriz1)}.")

print(f"El número más bajo de la suma de los elementos de cada fila de la matriz, es {min(sumaElementosFilas(matriz1))}.")