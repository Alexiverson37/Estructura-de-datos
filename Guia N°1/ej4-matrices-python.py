# gauss: list -> list
# Ejecuta el método de gauss para la inversa de una matriz
def gauss(matriz):
    n = len(matriz)
    
    # Concatenar la matriz identidad a la matriz inicial
    matriz_aumentada = []
    for i in range(n):
        # Se define la matriz identidad
        matriz_identidad = matriz[i] + [1 if i == j else 0 for j in range(n)]
        # Se agrega la matriz identidad a la matriz aumentada
        matriz_aumentada.append(matriz_identidad)
    
    # Aplicar el algoritmo de Gauss-Jordan
    for i in range(n):
        # Se intercambian filas si es necesario para evitar divisiones por cero
        if matriz_aumentada[i][i] == 0:
            for j in range(i + 1, n):
                if matriz_aumentada[j][i] != 0:
                    matriz_aumentada[i], matriz_aumentada[j] = matriz_aumentada[j], matriz_aumentada[i]
                    break
        
        aux = matriz_aumentada[i][i]
        
        # Dividir toda la fila por el pivote
        matriz_aumentada[i] = [element / aux for element in matriz_aumentada[i]]
        
        # Restar múltiplos de la fila actual de otras filas para hacer ceros en la columna del pivote
        for j in range(n):
            if j != i:
                factor = matriz_aumentada[j][i]
                matriz_aumentada[j] = [element - factor * matriz_aumentada[i][idx] for idx, element in enumerate(matriz_aumentada[j])]
    
    # Extraer la matriz inversa de la parte derecha de la matriz aumentada
    inverse = [row[n:] for row in matriz_aumentada]
    
    return inverse



# Condicional que determina si la matriz A es cuadrada no-singular
def ejecucion(matriz):
    if len(matriz) == len(matriz[0]): 
        inverse = gauss(matriz)
        print("Matriz inversa de A:\n")
        for i in inverse:
            print(i)

        # Si no es cuadrada no-singular
    else:
        print("La matriz no es cuadrada, entonces no se puede calcular la matriz inversa.")

# Ejemplo de uso con una matriz cuadrada
matriz_A = [[2, 4, -1], [0, 2, 1], [1, 0, 3]]  
print(f"\nMatriz original A {matriz_A}\n")
resultado_A = ejecucion(matriz_A)


# Ejemplo de uso con una matriz que no es cuadrada
matriz_B = [[1, 2], [3, 4], [8, 12]]
print(f"\nMatriz original B {matriz_B}\n")
resultado_B = ejecucion(matriz_B)




