class Empleado:
    def __init__(self, nombre, cargo):
        self.nombre = nombre
        self.cargo = cargo
        self.subordinados = []
    # agregar_subordinado: Str -> None
    # Es el método que añade a la lista empleados un empleado.
    def agregar_subordinado(self, subordinado):
        self.subordinados.append(subordinado)

    # eliminar_subordinado: Str -> None
    # Es el método que quita a la lista empleados un empleado.
    def eliminar_subordinado(self, subordinado):
        self.subordinados.remove(subordinado)

    # obtener_subordinados: None -> List[Str]
    # Es el método que da a conocer los empleados en la lista empleados.
    def obtener_subordinados(self):
        return self.subordinados

    # __str__: None -> Str
    # Es el método que devuelve el string de la clase Empleado.
    def __str__(self):
        return self.nombre + " - " + self.cargo


class JerarquiaEmpleados:
    def __init__(self):
        self.raiz = None

    # agregar_empleado: Str Str Str -> None
    # Es el método agregar_empleado  que se encarga de agregar un empleado.
    def agregar_empleado(self, nombre, cargo, jefe=None): # A)
        empleado = Empleado(nombre, cargo)
        if jefe is None:
            self.raiz = empleado
        else:
            jefe.agregar_subordinado(empleado)

    # eliminar_empleado: Str -> None or Str
    # Es el método que se encarga de eliminar un empleado.
    def eliminar_empleado(self, empleado): # B)
        if self.raiz == empleado:
            self.raiz = None
        else:
            jefe = self.obtener_jefe_directo(empleado)
            if jefe is not None:
                jefe.eliminar_subordinado(empleado)

    # mostrar_jerarquia: None -> None
    # Es el método que muestra la jerarquía de la empresa.
    def mostrar_jerarquia(self): # C)
        self.mostrar_empleado(self.raiz, "")

    # mostrar_empleado: Str Str -> 
    # Es el método público que muestra empleado en específico.
    def mostrar_empleado(self, empleado, espacio):
        if empleado is not None:
            print(espacio + str(empleado))
            subordinados = empleado.obtener_subordinados()
            for subordinado in subordinados:
                self.mostrar_empleado(subordinado, espacio + "   ")

    # _buscar_empleado: Str -> Str
    # Es el método privado que busca un empleado en específico de la empresa. 
    def buscar_empleado(self, nombre): # D) 
        return self.buscar_empleado_recursivo(self.raiz, nombre)

    # buscar_empleado_recursivo: Str Str -> Str
    # Es el método que busca el empleado recursivo.
    def buscar_empleado_recursivo(self, empleado, nombre):
        if empleado is not None:
            if empleado.nombre == nombre:
                return empleado
            else:
                subordinados = empleado.obtener_subordinados()
                for subordinado in subordinados:
                    resultado = self.buscar_empleado_recursivo(subordinado, nombre)
                    if resultado is not None:
                        return resultado
        return None

    # _obtener_jefe_directo: Str -> None or Str 
    # Es el método público que obtiene el jefe directo de un empleado.
    def obtener_jefe_directo(self, empleado): # E) 
        return self.obtener_jefe_directo_recursivo(self.raiz, empleado)

    # _obtener_jefe_directo: Str -> None or Str 
    # Es el método privado que obtiene el jefe directo de un empleado.
    def obtener_jefe_directo_recursivo(self, actual, empleado):
        if actual is not None:
            subordinados = actual.obtener_subordinados()
            if empleado in subordinados:
                return actual
            else:
                for subordinado in subordinados:
                    resultado = self.obtener_jefe_directo_recursivo(subordinado, empleado)
                    if resultado is not None:
                        return resultado
        return None


# Ejemplos de uso

jerarquia = JerarquiaEmpleados()

jerarquia.agregar_empleado("CEO", "Chief Executive Officer")
jerarquia.agregar_empleado("CFO", "Chief Financial Officer", jerarquia.buscar_empleado("CEO"))
jerarquia.agregar_empleado("CTO", "Chief Technology Officer", jerarquia.buscar_empleado("CEO"))
jerarquia.agregar_empleado("Gerente de Ventas", "Sales Manager", jerarquia.buscar_empleado("CFO"))
jerarquia.agregar_empleado("Gerente de Marketing", "Marketing Manager", jerarquia.buscar_empleado("CFO"))
jerarquia.agregar_empleado("Desarrollador Senior", "Senior Developer", jerarquia.buscar_empleado("CTO"))
jerarquia.agregar_empleado("Desarrollador Junior", "Junior Developer", jerarquia.buscar_empleado("Desarrollador Senior"))

print("Mostrando jerarquía completa:")
jerarquia.mostrar_jerarquia()

print()

empleado_buscado = jerarquia.buscar_empleado("CTO")
if empleado_buscado is not None:
    print("Cargo del empleado:", empleado_buscado.cargo)
    subordinados = empleado_buscado.obtener_subordinados()
    if subordinados:
        print("Subordinados:")
        for subordinado in subordinados:
            print(subordinado.nombre, "-", subordinado.cargo)
    else:
        print("No tiene subordinados")

print()

empleado = jerarquia.buscar_empleado("Gerente de Ventas")
jefe_directo = jerarquia.obtener_jefe_directo(empleado)
if jefe_directo is not None:
    print("Jefe directo de", empleado.nombre + ":", jefe_directo.nombre, "-", jefe_directo.cargo)

# Código realizado por Álex Hernández, Ignacio Soto y Nicolás Almuna.

