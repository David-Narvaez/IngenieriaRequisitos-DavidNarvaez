class BilleteDeTren:
    def __init__(self, destino, precio):
        self.destino = destino
        self.precio = precio

class SistemaExpedicionBilletes:
    def __init__(self):
        self.destinos = {
            "Destino bogota": 50,
            "Destino bucaramanga": 75,
            "Destino medellin": 100
        }

    def mostrar_menu_destinos(self):
        print("Seleccione su destino:")
        for i, destino in enumerate(self.destinos.keys(), start=1):
            print(f"{i}. {destino}")

    def expedir_billete(self, destino, precio):
        print(f"Billete de tren con destino a {destino} expedido. Precio: ${precio}")

    def ejecutar(self):
        self.mostrar_menu_destinos()
        opcion = int(input("Ingrese el número de destino deseado: "))

        if opcion in range(1, len(self.destinos) + 1):
            destinos_list = list(self.destinos.keys())
            destino_seleccionado = destinos_list[opcion - 1]
            precio_billete = self.destinos[destino_seleccionado]

            identificador_personal = input("Introduzca su identificador personal: ")
            # Aquí normalmente habría lógica para validar el identificador personal.

            # Simulamos la validación de la transacción de crédito
            transaccion_valida = True

            if transaccion_valida:
                self.expedir_billete(destino_seleccionado, precio_billete)
            else:
                print("Transacción de crédito no válida. No se pudo expedir el billete.")


if __name__ == "__main__":
    sistema = SistemaExpedicionBilletes()
    sistema.ejecutar()