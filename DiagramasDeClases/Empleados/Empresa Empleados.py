class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []
        self.clientes = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def mostrar_empleados(self):
        print("Empleados de", self.nombre)
        for empleado in self.empleados:
            empleado.mostrar_informacion()

    def mostrar_clientes(self):
        print("Clientes de", self.nombre)
        for cliente in self.clientes:
            cliente.mostrar_informacion()


class Empleado:
    def __init__(self, nombre, edad, sueldo_bruto):
        self.nombre = nombre
        self.edad = edad
        self.sueldo_bruto = sueldo_bruto

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Sueldo Bruto: {self.sueldo_bruto}")


class Directivo(Empleado):
    def __init__(self, nombre, edad, sueldo_bruto, categoria):
        super().__init__(nombre, edad, sueldo_bruto)
        self.categoria = categoria
        self.subordinados = []

    def agregar_subordinado(self, empleado):
        self.subordinados.append(empleado)

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Categoría: {self.categoria}")
        if self.subordinados:
            print("Subordinados:")
            for subordinado in self.subordinados:
                print(f"- {subordinado.nombre}")


class Cliente:
    def __init__(self, nombre, edad, telefono_contacto):
        self.nombre = nombre
        self.edad = edad
        self.telefono_contacto = telefono_contacto

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Teléfono de Contacto: {self.telefono_contacto}")


# Ejemplo de uso:
if __name__ == "__main__":
    empresa = Empresa("Mi Empresa")

    empleado1 = Empleado("Empleado 1", 30, 50000)
    empleado2 = Empleado("Empleado 2", 25, 45000)
    directivo = Directivo("Directivo 1", 35, 60000, "Gerente")
    directivo.agregar_subordinado(empleado1)
    directivo.agregar_subordinado(empleado2)

    cliente1 = Cliente("Cliente 1", 40, "123-456-7890")
    cliente2 = Cliente("Cliente 2", 28, "987-654-3210")

    empresa.agregar_empleado(empleado1)
    empresa.agregar_empleado(empleado2)
    empresa.agregar_empleado(directivo)
    empresa.agregar_cliente(cliente1)
    empresa.agregar_cliente(cliente2)

    empresa.mostrar_empleados()
    empresa.mostrar_clientes()