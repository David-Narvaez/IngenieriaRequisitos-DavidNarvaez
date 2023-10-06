# David Esteban Narvaez Muñoz Ingenieria de Requisitos - calculadora

class Calculadora:
    def sumar (self, a,b):
        return a+b
    def rest (self, a,b):
        return a-b
    def multiplicacion (self, a,b):
        return a*b
    def division (self, a,b):
        if b==0:
            return"Error al dividir"
        return a/b
    
if __name__ == "__main__":
    calculadora=Calculadora()
    a=int(input("Digite el primer numero:"))
    b=int(input("Digite el segundo numero:"))    

    suma = calculadora.sumar(a, b)
    rest = calculadora.rest(a, b)
    multiplicacion = calculadora.multiplicacion(a, b)
    division = calculadora.division(a, b)

    print(f"suma: {suma}")
    print(f"resta: {rest}")
    print(f"multiplicacion: {multiplicacion}")
    print(f"division: {division}")