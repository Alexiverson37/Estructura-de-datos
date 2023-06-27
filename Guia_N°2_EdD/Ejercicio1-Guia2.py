# Clase Cancion de atributos titulo y artista
class Cancion:
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista

# Clase Nodo que cuenta con un único atributo, "cancion"
class Nodo:
    def __init__(self, cancion):
        self.cancion = cancion
        self.siguiente = None
        self.anterior = None

# Aquí en ListaReproduccion es donde se hace uso de la lista doblemente enlazada
class ListaReproduccion:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar_cancion(self, cancion):
        nuevo_nodo = Nodo(cancion)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def mostrar_lista(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            print(nodo_actual.cancion.titulo + " - " + nodo_actual.cancion.artista)
            nodo_actual = nodo_actual.siguiente

# Ejemplos de usos
print("Mi lista de reproducción:")

# Se llama a la clase ListaReproduccion para crear un objeto
mi_lista = ListaReproduccion() 

# Se le añaden canciones a la lista previamente creada
mi_lista.agregar_cancion(Cancion("Love Sosa", "Chief Keef"))
mi_lista.agregar_cancion(Cancion("Self Love", "Metro Boomin, Coi Leray"))
mi_lista.agregar_cancion(Cancion("Rich Flex", "Drake, 21 Savage"))

# Se llama a la función mostrar_lista() para que muestre las canciones que están en la lista
mi_lista.mostrar_lista()

# Código realizado por Álex Hernández, Ignacio Soto y Nicolás Almuna.