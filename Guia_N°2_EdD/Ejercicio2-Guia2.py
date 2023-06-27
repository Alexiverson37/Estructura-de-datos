class Cliente:
    def __init__(self, ticket, caja):
        self.ticket = ticket
        self.caja = caja

# Representa un nodo en la lista circular
class Nodo:
    def __init__(self, cliente):
        self.cliente = cliente
        self.siguiente = None

# Es la lista circular
# Este metodo crea un nodo cliente y lo agrega al final de la lista circular
class ColaAtencion:
    def __init__(self):
        self.cabeza = None

    def agregar_cliente(self, cliente):
        nuevo_nodo = Nodo(cliente)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente != self.cabeza:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza

# Este metodo elimina al primer nodo de la lista circular y muestra
# El numero de ticket y caja del cliente que esta siendo atendido
    def atender_cliente(self):
        if not self.cabeza:
            print("No hay clientes en la cola")
            return
        cliente_atendido = self.cabeza.cliente
        print("El Cliente con ticket " + str(cliente_atendido.ticket) + " esta siendo atendido en la caja " + str(cliente_atendido.caja))
        if self.cabeza.siguiente == self.cabeza:
            self.cabeza = None
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente != self.cabeza:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = self.cabeza.siguiente
            self.cabeza = self.cabeza.siguiente
    
# Muestra la cola de atencion 
# Este metodo recorre la lista circular desde la cabeza hasta el final
# Imprime el numero de ticket y el numero de caja de los clientes
    def mostrar_cola(self):
        if not self.cabeza:
            print("No hay clientes en la cola")
            return
        print("Clientes en la cola:")
        nodo_actual = self.cabeza
        while True:
            print("Cliente con ticket " + str(nodo_actual.cliente.ticket) + " pase a la caja " + str(nodo_actual.cliente.caja))
            if nodo_actual.siguiente == self.cabeza:
                break
            nodo_actual = nodo_actual.siguiente

# Ejemplos de uso
cliente_cola= ColaAtencion()
cliente_cola.agregar_cliente(Cliente(6, 1))
cliente_cola.agregar_cliente(Cliente(7, 2))
cliente_cola.agregar_cliente(Cliente(8, 3))
cliente_cola.mostrar_cola()
cliente_cola.atender_cliente()
cliente_cola.mostrar_cola()

# Código realizado por Álex Hernández, Ignacio Soto y Nicolás Almuna.

