from datetime import datetime

class EmpresaAlquiler:
    def __init__(self):
        self.clientes = []
        self.agencias = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def agregar_agencia(self, agencia):
        self.agencias.append(agencia)

    def realizar_reserva(self, cliente, coches, fecha_inicio, fecha_fin, litros_gasolina, precio_total):
        reserva = Reserva(cliente, coches, fecha_inicio, fecha_fin, litros_gasolina, precio_total)
        cliente.reservas.append(reserva)
        return reserva

class Cliente:
    def __init__(self, dni, nombre, direccion, telefono, codigo_uniq):
        self.dni = dni
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.codigo_uniq = codigo_uniq
        self.avalado_por = None
        self.reservas = []

class Reserva:
    def __init__(self, cliente, coches, fecha_inicio, fecha_fin, litros_gasolina, precio_total):
        self.cliente = cliente
        self.coches = coches
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.litros_gasolina = litros_gasolina
        self.precio_total = precio_total
        self.entregado = False

    def calcular_precio_total(self):
        return self.precio_total

class Coche:
    def __init__(self, matricula, modelo, color, marca, garaje):
        self.matricula = matricula
        self.modelo = modelo
        self.color = color
        self.marca = marca
        self.garaje = garaje

class Agencia:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

class Garaje:
    def __init__(self, matricula, modelo, color, marca):
        self.matricula = matricula
        self.modelo = modelo
        self.color = color
        self.marca = marca

def obtener_datos_cliente():
    dni = input("Ingrese el DNI del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    codigo_uniq = input("Ingrese el código único del cliente: ")
    return Cliente(dni, nombre, direccion, telefono, codigo_uniq)

def obtener_datos_coche():
    matricula = input("Ingrese la matrícula del coche: ")
    modelo = input("Ingrese el modelo del coche: ")
    color = input("Ingrese el color del coche: ")
    marca = input("Ingrese la marca del coche: ")
    return Coche(matricula, modelo, color, marca, None)  # El garaje se asignará más tarde

def obtener_fecha(texto):
    fecha_str = input(texto + " (Formato: DD/MM/AAAA): ")
    return datetime.strptime(fecha_str, "%d/%m/%Y")

def main():
    empresa = EmpresaAlquiler()

    while True:
        print("\nMenú:")
        print("1. Agregar Cliente")
        print("2. Agregar Agencia")
        print("3. Realizar Reserva")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cliente = obtener_datos_cliente()
            empresa.agregar_cliente(cliente)
            print(f"Cliente {cliente.nombre} agregado con éxito.")

        elif opcion == "2":
            nombre = input("Ingrese el nombre de la agencia: ")
            direccion = input("Ingrese la dirección de la agencia: ")
            telefono = input("Ingrese el teléfono de la agencia: ")
            agencia = Agencia(nombre, direccion, telefono)
            empresa.agregar_agencia(agencia)
            print(f"Agencia {agencia.nombre} agregada con éxito.")

        elif opcion == "3":
            print("Seleccione un cliente para la reserva:")
            for i, cliente in enumerate(empresa.clientes, start=1):
                print(f"{i}. {cliente.nombre}")

            cliente_seleccionado = int(input("Ingrese el número del cliente: ")) - 1

            if 0 <= cliente_seleccionado < len(empresa.clientes):
                cliente = empresa.clientes[cliente_seleccionado]
                fecha_inicio = obtener_fecha("Ingrese la fecha de inicio de la reserva")
                fecha_fin = obtener_fecha("Ingrese la fecha de fin de la reserva")
                litros_gasolina = float(input("Ingrese los litros de gasolina en el depósito: "))
                precio_total = float(input("Ingrese el precio total de la reserva: "))
                coches = []

                while True:
                    coche = obtener_datos_coche()
                    coches.append(coche)
                    continuar = input("¿Desea agregar otro coche? (S/N): ").strip().lower()
                    if continuar != "s":
                        break

                reserva = empresa.realizar_reserva(cliente, coches, fecha_inicio, fecha_fin, litros_gasolina, precio_total)
                print(f"Reserva realizada con éxito. Número de reserva: {id(reserva)}")

            else:
                print("Número de cliente no válido.")

        elif opcion == "4":
            print("Gracias por utilizar el sistema de alquiler de automóviles. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()

