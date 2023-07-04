# (la mayoria son nodos)Clase Nodo para representar cada artículo del inventario
class Nodo:
    # Constructor con código, nombre, descripcin y cantidad
    def __init__(self, codigo, nombre, descripcion, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.siguiente = None 
        self.anterior = None 

# Clase Lista para representar la lista bidireccional del inventario
class Lista:
    # Constructor con un nodo vacio
    def __init__(self):
        self.cabeza = Nodo(None, None, None, None) 
        self.cabeza.siguiente = self.cabeza 
        self.cabeza.anterior = self.cabeza 

    # Metodo para agregar un articulo al inventario, ingresando su código, nombre, descripcion y cantidad inicial
    def agregar(self, codigo, nombre, descripcion, cantidad):
        nuevo = Nodo(codigo, nombre, descripcion, cantidad) 
        actual = self.cabeza.siguiente 
        while actual != self.cabeza and actual.codigo < codigo:
            actual = actual.siguiente 
        anterior = actual.anterior 
        nuevo.siguiente = actual 
        nuevo.anterior = anterior 
        anterior.siguiente = nuevo 
        actual.anterior = nuevo

    # Metodo para eliminar un articulo del inventario utilizando su codigo
    def eliminar(self, codigo):
        encontrado = self.buscar(codigo) # busca por codigo 
        if encontrado: 
            anterior = encontrado.anterior 
            siguiente = encontrado.siguiente 
            anterior.siguiente = siguiente 
            siguiente.anterior = anterior 
            return True 
        else: 
            return False 

    # Metodo para buscar un articulo en especifico por su código
    def buscar(self, codigo):
        actual = self.cabeza.siguiente 
        while actual != self.cabeza and actual.codigo <= codigo: 
            if actual.codigo == codigo: 
                return actual 
            actual = actual.siguiente 
        return None 

    # Metodo para actualizar la cantidad disponible de un articulo
    def actualizar(self, codigo, cantidad):
        encontrado = self.buscar(codigo) 
        if encontrado: 
            encontrado.cantidad = cantidad 
            return True 
        else: 
            return False 

    # Metodo para mostrar todos los artículos del inventario en orden ascendente segun su código
    def mostrar(self):
        actual = self.cabeza.siguiente 
        while actual != self.cabeza:  
            print(f"Código: {actual.codigo}, Nombre: {actual.nombre}, Descripción: {actual.descripcion}, Cantidad: {actual.cantidad}") 
             
            actual = actual.siguiente

                                        # no se como demostarlo