#ejercicio 1
# Clase Nodo para representar cada contacto
class Nodo:
    # Constructor con nombre, telefono y emaill
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.siguiente = None 
        self.anterior = None 


# Clase Lista para representar la lita circular bidireccional
class Lista:
    
    def __init__(self):
        self.cabeza = Nodo(None, None, None) 
        self.cabeza.siguiente = self.cabeza 
        self.cabeza.anterior = self.cabeza 

    # Método para agregar un contacto a la lista
    def agregar(self, nombre, telefono, email):
        nuevo = Nodo(nombre, telefono, email) 
        ultimo = self.cabeza.anterior 
        nuevo.siguiente = self.cabeza 
        nuevo.anterior = ultimo 
        ultimo.siguiente = nuevo 
        self.cabeza.anterior = nuevo 

    # Método para mostrar la lista de contactos
    def mostrar(self):
        actual = self.cabeza.siguiente 
        while actual != self.cabeza: 
            print(f"Nombre: {actual.nombre}, Teléfono: {actual.telefono}, Email: {actual.email}") # Imprimir los datos del contacto
            actual = actual.siguiente 

    # Método para buscar un contacto por su nombre
    def buscar(self, nombre):
        actual = self.cabeza.siguiente # Empezar desde el primer nodo de la lista (no el cabeza)
        while actual != self.cabeza: 
            if actual.nombre == nombre: 
                return actual 
            actual = actual.siguiente 
        return None 

    # Método eliminar un contactode la lista
    def eliminar(self, nombre):
        encontrado = self.buscar(nombre) # Buscar el contacto por su nombre
        if encontrado: 
            anterior = encontrado.anterior 
            siguiente = encontrado.siguiente 
            anterior.siguiente = siguiente 
            siguiente.anterior = anterior 
            return True 
        else: 
            return False 

    # Método para verificar si la lista de contacto está vacía
    def vacia(self):
        return self.cabeza.siguiente == self.cabeza and self.cabeza.anterior == self.cabeza 

                         # ejemplo especifico para mostrar funcionamiento         
# Crear una lista de contactos vacía
lista = Lista()

# Agregar algunos contactos a la lista
lista.agregar("Ana", "123456789", "ana@gmail.com")
lista.agregar("Beto", "234567890", "beto@gmail.com")
lista.agregar("Carlos", "456789123", "carlos@gmail.com")

# Mostrar la lista de contactos
print("Lista de contactos:")
lista.mostrar()

# Buscar un contacto por su nombre
print("Buscar a Ana:")
encontrado = lista.buscar("Ana")
if encontrado:
    print(f"Nombre: {encontrado.nombre}, Teléfono: {encontrado.telefono}, Email: {encontrado.email}")
else:
    print("No se encontro el contacto")

# Eliminar un contacto de la lista
print("Eliminar a Beto:")
eliminado = lista.eliminar("Beto")
if eliminado:
    print("Se elimino el contacto")
else:
    print("No se eliminoel contacto")

# Verificar si la lista esta vacia
print("Verificar si la lista esta vacia:")
if lista.vacia():
    print("La lista esta vacia")
else:
    print("La lista no esta vacia")
