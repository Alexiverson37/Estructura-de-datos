class Pila:
    def __init__(self):
        self.productos_recibidos = []

    def pila_esta_vacia(self):
        return len(self.productos_recibidos) == 0
    
    # verificar_pila: None -> Str
    # Retorna la verificación si está o no vacía la pila de productos.
    def verificar_pila(self):
        if self.pila_esta_vacia():
            return "Está vacía la pila de productos."
        else:
            return "No está vacía la pila de productos."

    # agregar_producto: Str -> None
    # Este método nos permite agregar un ítem a la lista de productos recibidos.
    def agregar_producto(self, item):
        self.productos_recibidos.append(item)

    def desapilar(self):
        if self.pila_esta_vacia():
            return None
        return self.productos_recibidos.pop()
    
    # imprimir_productos_recibidos: None -> List
    # Retorna la lista de productos recibidos en la pila.
    def imprimir_productos_recibidos(self):
        return self.productos_recibidos


class Cola(Pila):
    def __init__(self):
        super().__init__()
        self.productos_para_despachar = []

    def cola_esta_vacia(self):
        return len(self.productos_para_despachar) == 0
    
    # verificar_cola: None -> Str
    # Retorna la verificación si está o no vacía la cola de productos.
    def verificar_cola(self):
        if self.cola_esta_vacia():
            return "Está vacía la cola de productos."
        else:
            return "No está vacía la cola de productos."
    
    # encolar: Str -> None
    # Permite encolar un ítem en la cola de productos para despachar.
    def agregar_producto(self, item):
        self.productos_para_despachar.append(item)

    # despachar_producto: None -> Str or None
    # Remueve y devuelve el producto más antiguo de la cola de productos para despachar.
    # Si la cola está vacía, devuelve None.
    def despachar_producto(self):
        if self.cola_esta_vacia():
            print("No hay productos disponibles para despachar.")
            return None
        return self.productos_para_despachar.pop(0)
    
    # imprimir_productos_para_despachar: None -> List
    # Retorna la lista de productos para despachar en la cola.
    def imprimir_productos_para_despachar(self):
        return self.productos_para_despachar


class Almacen:
    
    # En el método constructor de la clase Almacen, se llama a las clases Cola y Pila.
    def __init__(self):
        self.cola = Cola()
        self.pila = Pila()
    
    # agregar_producto: Str -> None
    # Permite agregar un producto al almacén.
    def agregar_producto(self, item):
        self.pila.agregar_producto(item)
        self.cola.agregar_producto(item)

    # despachar_producto: None -> Str or None
    # Despacha un producto del almacén.
    # Retorna el producto despachado o None si no hay productos disponibles.
    def despachar_producto(self):
        return self.cola.despachar_producto()
    
    # verificar_pila: None -> Str
    # Verifica si la pila de productos está vacía o no vacía.
    # Retorna un mensaje indicando el estado de la pila.
    def verificar_pila(self):
        return self.pila.verificar_pila()

    # verificar_cola: None -> Str
    # Verifica si la cola de productos está vacía o no vacía.
    # Retorna un mensaje indicando el estado de la cola.
    def verificar_cola(self):
        return self.cola.verificar_cola()
    
    # imprimir_productos_recibidos: None -> List[Str]
    # Imprime la lista de productos recibidos en el almacén.
    def imprimir_productos_recibidos(self):
        return self.pila.imprimir_productos_recibidos()

    # imprimir_productos_para_despachar: None -> List[Str]
    # Imprime la lista de productos para despachar en el almacén.
    def imprimir_productos_para_despachar(self):
        return self.cola.imprimir_productos_para_despachar()
    
    # mostrar_cantidad_total: None -> Str
    # Muestra la cantidad total de productos en el almacén.
    # Retorna un mensaje con la cantidad total de productos.
    def mostrar_cantidad_total(self):
        total = (len(self.pila.productos_recibidos) + len(self.cola.productos_para_despachar))
        return f"Cantidad total de productos en el almacén = {total}"


# Ejemplos de uso

almacen_ejemplo = Almacen()
# A)
almacen_ejemplo.agregar_producto("Pan")
almacen_ejemplo.agregar_producto("Leche")
almacen_ejemplo.agregar_producto("Cereal")

# B)
almacen_ejemplo.despachar_producto() # Despacha el último producto de la Cola del almacén.

# C)
print(almacen_ejemplo.verificar_pila())  # Verificar si la pila de productos recibidos está vacía.

# D)
print(almacen_ejemplo.verificar_cola())  # Verificar si la cola de productos para despachar está vacía.

# E)
print(f"Productos recibidos: {almacen_ejemplo.imprimir_productos_recibidos()}")  # Imprimir lista de productos recibidos.

# F)
print(f"Productos para despachar: {almacen_ejemplo.imprimir_productos_para_despachar()}")  # Imprimir lista de productos para despachar.

# G)
print(almacen_ejemplo.mostrar_cantidad_total())  # Mostrar cantidad total de productos en el almacén.

# Código realizado por Álex Hernández, Ignacio Soto y Nicolás Almuna.





