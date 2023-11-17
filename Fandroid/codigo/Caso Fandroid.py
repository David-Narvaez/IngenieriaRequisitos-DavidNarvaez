class TarjetaCredito:
    def __init__(self, marca, numero, vencimiento, codigo_verificacion):
        self.marca = marca
        self.numero = numero
        self.vencimiento = vencimiento
        self.codigo_verificacion = codigo_verificacion

class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.tarjeta = None
        self.dispositivos = []
        self.puntos = 0

    def agregar_tarjeta(self, tarjeta):
        self.tarjeta = tarjeta

    def agregar_dispositivo(self, dispositivo):
        self.dispositivos.append(dispositivo)

    def comprar_aplicacion(self, aplicacion):
        self.puntos += aplicacion.puntos

    def canjear_premio(self):
        if self.puntos >= 100:
            self.puntos -= 100
            print("¡Premio canjeado! Has utilizado 100 puntos.")
        else:
            print("No tienes suficientes puntos para canjear un premio.")

    def consultar_informacion(self):
        print("Nombre: {}".format(self.nombre))
        print("Email: {}".format(self.email))
        if self.tarjeta:
            print("Tarjeta de crédito:")
            print("Marca: {}".format(self.tarjeta.marca))
            print("Número: {}".format(self.tarjeta.numero))
            print("Vencimiento: {}".format(self.tarjeta.vencimiento))
        else:
            print("Sin tarjeta de crédito asociada")
        print("Puntos acumulados: {}".format(self.puntos))

    def modificar_informacion(self, nombre, email):
        self.nombre = nombre
        self.email = email

class Aplicacion:
    def __init__(self, nombre, puntos):
        self.nombre = nombre
        self.puntos = puntos

def main():
    print("==================================================")
    print("                   FANDROID                       ")
    print("==================================================")

    nombre_cliente = input("Ingrese su nombre: ")
    email_cliente = input("Ingrese su correo electrónico: ")
    tarjeta = str(input("Marca: ")), int(input("Numero de Tarjeta: ")), float(input("Vencimiento: ")), int(input("Codigo de Verificacion: "))


    cliente = Cliente(nombre_cliente, email_cliente)
    cliente.agregar_tarjeta(tarjeta)

    while True:
        print("\n1. Comprar aplicación")
        print("\n2. Consultar/modificar información personal y tarjeta")
        print("\n3. Canjear premios")
        print("\n4. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            nombre_aplicacion = input("Introduzca el nombre de la aplicación: ")
            aplicacion = Aplicacion(nombre_aplicacion)
            cliente.comprar_aplicacion(aplicacion)
            print("¡Compra realizada! Puntos acumulados: {}".format(cliente.puntos))

        elif opcion == "2":
            cliente.consultar_informacion()
            nuevo_nombre = str(input("Nuevo nombre: "))
            nuevo_email = str(input("Nuevo correo electrónico: "))
            nueva_tarjeta = str(input("Marca: ")), int(input("Numero de Tarjeta: ")), float(input("Vencimiento: ")), int(input("Codigo de Verificacion: "))
            cliente.modificar_informacion(nuevo_nombre, nuevo_email)
            print("Información modificada exitosamente.")

        elif opcion == "3":
            nombre_aplicacion = input("Introduzca el nombre de la aplicación: ")
            cliente.canjear_premio()
            print ("Gracias por canjear")

        elif opcion == "4":
            print("Gracias por utilizar la plataforma. ¡Hasta pronto!")
            break

        else:
            print("Opción inválida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    main()
