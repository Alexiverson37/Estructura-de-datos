import numpy as np
A = np.random.randint(-10, -5, size=(3, 3))
B = np.random.randint(-10, -5, size=(3, 3))

C = np.multiply(A, B)
D = np.matmul(A, B)

E = np.eye(3) 
F = np.matmul(D, E)
print(F)    
