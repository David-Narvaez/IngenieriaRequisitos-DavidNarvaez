# INGENIERIA DE REQUISITOS 
# CAMILA ZAMBRANO - DAVID NARVAEZ
# BOLETOS DE TREN 

class BoletoTren:
    destinos = ["Bogota" , "Medellin", "Pasto"]  # Lista de destinos posibles

    def __init__(self, destino, tarjeta_credito, id_personal):
        self.destino = destino
        self.tarjeta_credito = tarjeta_credito                        # __init__ se encarga de tomar los datos de destino, tarjeta de crédito e identificador personal cuando se crea un nuevo objeto de la clase luego, asigna estos valores a los atributos, lo que permite que cada boleto de tren tenga su propio destino, número de tarjeta de crédito y identificador personal.
        self.id_personal = id_personal                                # self dar valores a los atributos asignados

    def emitir_boleto(self):
        print("Boleto emitido para {}.".format(self.destino))
        print("Importe cargado a la tarjeta de crédito: 10.000$")     # imprime información sobre la emisión del boleto y el importe cargado a la tarjeta de crédito (aunque el valor real del importe no está implementado).

def main():
    print("===============================================")
    print("SISTEMA DE EXPEDICION DE BOLETOS DE TREN")
    print("===============================================")

    while True:  # Inicia bucle 
        print("\n * Destinos disponibles:")                                                                         # Imprime un mensaje indicando que se mostrarán los destinos disponibles.
        for idx, destino in enumerate(BoletoTren.destinos):                                                         # Iteracion de, indice y el valor registrado en cada iteracion.
            print("{}. {}".format(idx + 1, destino))                                                                # índice del destino más uno (para que la numeración comience desde 1) y el nombre del destino.
        try:                                                                                                        # Maneja posibles exepciones 
            seleccion = int(input("\nSeleccione el número de destino (1-{}): ".format(len(BoletoTren.destinos))))   # Solicita al usuario que ingrese un número correspondiente al destino deseado y lo convierte en un entero.
            if 1 <= seleccion <= len(BoletoTren.destinos):                                                          # Comprueba si la selección del usuario está dentro de los límites válidos (entre 1 y la cantidad de destinos disponibles).                                  # Comprueba si la selección del usuario está dentro de los límites válidos (entre 1 y la cantidad de destinos disponibles).
                destino_seleccionado = BoletoTren.destinos[seleccion - 1]
                print("\nDestino seleccionado: {}".format(destino_seleccionado))
                id_personal = int(input("Introduzca su identificador personal: "))
                tarjeta_credito = int(input("Introduzca el número de su tarjeta de crédito: "))

                boleto = BoletoTren(destino_seleccionado, tarjeta_credito, id_personal)
                boleto.emitir_boleto()                                                                             # Crea un boleto con la informacion digitada y lo imprime

            else:                                                                                                   # si no 
                print("Selección inválida. Por favor, elija un número de destino válido.")

        except ValueError:               
            print("Error: Introduzca una opcion válida.")                                                          # si el usuario digita algo que no concuerda con la informacion requerida

        continuar = input("\n¿Desea comprar otro boleto (1. Sí/ 2. No): ")                                              # Pregunta al usuario si quiere comprar otro boleto
        if continuar.lower() != "1":
            print("Gracias por utilizar nuestro servicio. ¡Buen viaje!")
            break  # rompe el bucle

if __name__ == "__main__":     # Verifica la ejecucion del programa
    main()
