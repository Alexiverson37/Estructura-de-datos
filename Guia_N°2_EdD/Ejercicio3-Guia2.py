import math

# Se crea la clase nodo.
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

# Se crea la clase ListaEnlazada.
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

# A) Agrega un nuevo dato a la lista, este metodo crea un nuevo nodo con el dato
# y lo agrega al final de la lista enlazada simple.
    def agregar_dato(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo

# B) Calcula y devuelve la media de los datos almacenados en la lista.
# Este metodo recorre la lista enlazada desde la cabeza hasta el final.
    def calcular_media(self):
        if not self.cabeza:
            return 0
        suma = 0
        contador = 0
        nodo_actual = self.cabeza
        while nodo_actual:
            suma += nodo_actual.dato
            contador += 1
            nodo_actual = nodo_actual.siguiente
        return suma / contador
    
# C) Calcula y devuelve la desviacion estandar.
# El metodo es igual al anterior.
    def calcular_desviacion_estandar(self):
        if not self.cabeza:
            return 0
        media = self.calcular_media()
        suma_cuadrados = 0
        contador = 0
        nodo_actual = self.cabeza
        while nodo_actual:
            suma_cuadrados += (nodo_actual.dato - media) ** 2
            contador += 1
            nodo_actual = nodo_actual.siguiente
        return math.sqrt(suma_cuadrados / contador) # Aquí es donde se hace uso del import math.
    
# D) Imprime la lista en pantalla.
# Este método recorre la lista enlazada simple desde la cabeza hasta el final e imprime cada dato.
    def imprimir_lista(self):
        if not self.cabeza:
            print("La lista está vacía")
            return
        print("Datos en la lista:")
        nodo_actual = self.cabeza
        while nodo_actual:
            print(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente

# E) Verifica si la lista esta vacia.
    def verificar(self):
        return not bool(self.cabeza)

# Ejemplos de uso

# Se llama a la clase ListaEnlazada() para crear un objeto.
lista_enlazada= ListaEnlazada()

# Se llama a la función agregar_dato() para agregar datos en la lista creada previamente.
lista_enlazada.agregar_dato(1)
lista_enlazada.agregar_dato(2)
lista_enlazada.agregar_dato(3)

# Se solicita imprimir la lista mediante el método imprimir_lista().
lista_enlazada.imprimir_lista()

# Se imprimen strings relacionados a funciones de la clase ListaEnlazada().
print("La Media de los datos es: ", lista_enlazada.calcular_media())
print("La Desviación estándar de los datos es: ", lista_enlazada.calcular_desviacion_estandar())
print("¿La lista está vacía?", lista_enlazada.verificar())

# Código realizado por Álex Hernández, Ignacio Soto y Nicolás Almuna.

