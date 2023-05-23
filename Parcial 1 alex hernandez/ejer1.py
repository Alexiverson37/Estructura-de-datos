import numpy as np
import random
#crea matriz con un numeros random y un rango de 3x3
matriz = np.array([[random.randint(5,10) for i in range(3)] for j in range(3)])
print(matriz)
#encuentra la determinante automatica
deter = np.linalg.det(matriz)
print(deter)