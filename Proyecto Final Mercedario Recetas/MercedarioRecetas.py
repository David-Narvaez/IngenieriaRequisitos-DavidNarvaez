import os

class Ingrediente:
    def __init__(self, nombre, unidad, valor, sitio, calorias):
        self.nombre = nombre
        self.unidad = unidad
        self.valor = valor
        self.sitio = sitio
        self.calorias = calorias

class Receta:
    def __init__(self, nombre, tiempo, personas, ingredientes, descripcion):
        self.nombre = nombre
        self.tiempo = tiempo
        self.personas = personas
        self.ingredientes = ingredientes
        self.descripcion = descripcion

    def calcular_calorias(self):
        total_calorias = sum(ingrediente.calorias for ingrediente in self.ingredientes)
        return total_calorias

    def calcular_costo(self):
        total_costo = sum(ingrediente.valor for ingrediente in self.ingredientes)
        return total_costo

class MercedarioRecetas:
    def __init__(self):
        self.usuarios = {'chef': '123', 'administrador': '123'}
        self.usuario_actual = None
        self.ingredientes = []
        self.recetas = []

    def iniciar_sesion(self):
        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")
        if usuario in self.usuarios and self.usuarios[usuario] == contraseña:
            self.usuario_actual = usuario
            print(f"Bienvenido, {usuario}!")
        else:
            print("Usuario o contraseña incorrectos.")

    def mostrar_menu_principal(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la consola
            print("===== Mercedario Recetas =====")
            print("Desarrollado por:")
            print("- Santiago Getial")
            print("- Samuel Ibarra")
            print("- David Narvaez")
            print("Universidad Cooperativa de Colombia\n")
            print("===== Menú Principal =====")
            print("1. Gestionar Ingredientes")
            print("2. Gestionar Recetas")
            print("3. Visualizar Ingredientes")
            print("4. Visualizar Recetas")
            print("5. Cerrar Sesión")
            opcion = input("Seleccione una opción: ")
            if opcion == '1':
                self.gestionar_ingredientes()
            elif opcion == '2':
                self.gestionar_recetas()
            elif opcion == '3':
                self.visualizar_ingredientes()
            elif opcion == '4':
                self.visualizar_recetas()
            elif opcion == '5':
                self.usuario_actual = None
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def gestionar_ingredientes(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la consola
            print("===== Gestionar Ingredientes =====")
            print("1. Agregar Ingrediente")
            print("2. Editar Ingrediente")
            print("3. Eliminar Ingrediente")
            print("4. Volver al Menú Principal")
            opcion = input("Seleccione una opción: ")
            if opcion == '1':
                self.agregar_ingrediente()
            elif opcion == '2':
                self.editar_ingrediente()
            elif opcion == '3':
                self.eliminar_ingrediente()
            elif opcion == '4':
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def agregar_ingrediente(self):
        print("===== Agregar Ingrediente =====")
        nombre = input("Nombre del ingrediente: ")
        unidad = input("Unidad de medida: ")
        valor = float(input("Valor del ingrediente por unidad: "))
        sitio = input("Sitio de compra: ")
        calorias = float(input("Calorías por unidad: "))
        ingrediente = Ingrediente(nombre, unidad, valor, sitio, calorias)
        self.ingredientes.append(ingrediente)
        print(f'Ingrediente "{nombre}" agregado con éxito.')

    def editar_ingrediente(self):
        print("===== Editar Ingrediente =====")
        nombre = input("Nombre del ingrediente a editar: ")
        for ingrediente in self.ingredientes:
            if ingrediente.nombre == nombre:
                print(f'Editando ingrediente "{nombre}"...')
                ingrediente.nombre = input("Nuevo nombre del ingrediente: ")
                ingrediente.unidad = input("Nueva unidad de medida: ")
                ingrediente.valor = float(input("Nuevo valor del ingrediente por unidad: "))
                ingrediente.sitio = input("Nuevo sitio de compra: ")
                ingrediente.calorias = float(input("Nuevas calorías por unidad: "))
                print(f'Ingrediente "{nombre}" editado con éxito.')
                return
        print(f'Ingrediente "{nombre}" no encontrado.')

    def eliminar_ingrediente(self):
        print("===== Eliminar Ingrediente =====")
        nombre = input("Nombre del ingrediente a eliminar: ")
        for ingrediente in self.ingredientes:
            if ingrediente.nombre == nombre:
                self.ingredientes.remove(ingrediente)
                print(f'Ingrediente "{nombre}" eliminado con éxito.')
                input("Presione Enter para continuar...")
                return
        print(f'Ingrediente "{nombre}" no encontrado.')
        input("Presione Enter para continuar...")

    def gestionar_recetas(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la consola
            print("===== Gestionar Recetas =====")
            print("1. Agregar Receta")
            print("2. Editar Receta")
            print("3. Eliminar Receta")
            print("4. Volver al Menú Principal")
            opcion = input("Seleccione una opción: ")
            if opcion == '1':
                self.agregar_receta()
            elif opcion == '2':
                self.editar_receta()
            elif opcion == '3':
                self.eliminar_receta()
            elif opcion == '4':
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def agregar_receta(self):
        print("===== Agregar Receta =====")
        nombre = input("Nombre de la receta: ")
        tiempo = float(input("Tiempo de preparación en horas: "))
        personas = int(input("Cantidad de personas: "))
        print("Ingredientes disponibles:")
        for i, ingrediente in enumerate(self.ingredientes, 1):
            print(f"{i}. {ingrediente.nombre}")
        ingredientes_seleccionados = []
        while True:
            seleccion = input("Seleccione un ingrediente (0 para terminar): ")
            if seleccion == '0':
                break
            elif seleccion.isdigit() and 0 < int(seleccion) <= len(self.ingredientes):
                ingredientes_seleccionados.append(self.ingredientes[int(seleccion) - 1])
            else:
                print("Selección no válida. Intente de nuevo.")
        descripcion = input("Descripción de la preparación: ")
        receta = Receta(nombre, tiempo, personas, ingredientes_seleccionados, descripcion)
        self.recetas.append(receta)
        total_calorias = receta.calcular_calorias()
        total_costo = receta.calcular_costo()
        print(f'Receta "{nombre}" agregada con éxito.')
        print(f'Total de calorías: {total_calorias}')
        print(f'Total de costo: {total_costo}')

    def editar_receta(self):
        print("===== Editar Receta =====")
        nombre = input("Nombre de la receta a editar: ")
        for receta in self.recetas:
            if receta.nombre == nombre:
                print(f'Editando receta "{nombre}"...')
                receta.nombre = input("Nuevo nombre de la receta: ")
                receta.tiempo = float(input("Nuevo tiempo de preparación en horas: "))
                receta.personas = int(input("Nueva cantidad de personas: "))
                print("Ingredientes disponibles:")
                for i, ingrediente in enumerate(self.ingredientes, 1):
                    print(f"{i}. {ingrediente.nombre}")
                ingredientes_seleccionados = []
                while True:
                    seleccion = input("Seleccione un ingrediente (0 para terminar): ")
                    if seleccion == '0':
                        break
                    elif seleccion.isdigit() and 0 < int(seleccion) <= len(self.ingredientes):
                        ingredientes_seleccionados.append(self.ingredientes[int(seleccion) - 1])
                    else:
                        print("Selección no válida. Intente de nuevo.")
                receta.ingredientes = ingredientes_seleccionados
                receta.descripcion = input("Nueva descripción de la preparación: ")
                print(f'Receta "{nombre}" editada con éxito.')
                input("Presione Enter para continuar...")
                return
        print(f'Receta "{nombre}" no encontrada.')
        input("Presione Enter para continuar...")

    def eliminar_receta(self):
        print("===== Eliminar Receta =====")
        nombre = input("Nombre de la receta a eliminar: ")
        for receta in self.recetas:
            if receta.nombre == nombre:
                self.recetas.remove(receta)
                print(f'Receta "{nombre}" eliminada con éxito.')
                input("Presione Enter para continuar...")
                return
        print(f'Receta "{nombre}" no encontrada.')
        input("Presione Enter para continuar...")

    def visualizar_ingredientes(self):
        print("===== Visualizar Ingredientes =====")
        for ingrediente in self.ingredientes:
            print(f"Nombre: {ingrediente.nombre}")
            print(f"Unidad de medida: {ingrediente.unidad}")
            print(f"Valor por unidad: {ingrediente.valor}")
            print(f"Sitio de compra: {ingrediente.sitio}")
            print(f"Calorías por unidad: {ingrediente.calorias}")
            print("--------------------------")
        input("Presione Enter para continuar...")

    def visualizar_recetas(self):
        print("===== Visualizar Recetas =====")
        for receta in self.recetas:
            print(f"Nombre: {receta.nombre}")
            print(f"Tiempo de preparación: {receta.tiempo} horas")
            print(f"Cantidad de personas: {receta.personas}")
            print("Ingredientes:")
            for ingrediente in receta.ingredientes:
                print(f"  - {ingrediente.nombre}")
            print(f"Descripción: {receta.descripcion}")
            total_calorias = receta.calcular_calorias()
            total_costo = receta.calcular_costo()
            print(f'Total de calorías: {total_calorias}')
            print(f'Total de costo: {total_costo}')
            print("--------------------------")
        input("Presione Enter para continuar...")

# Crear instancia del sistema
sistema_recetas = MercedarioRecetas()

while True:
    # Limpiar la consola
    os.system('cls' if os.name == 'nt' else 'clear')

    # Mostrar el menú de inicio de sesión
    print("===== Mercedario Recetas =====")
    print("Desarrollado por:")
    print("- Santiago Getial")
    print("- Samuel Ibarra")
    print("- David Narvaez")
    print("Universidad Cooperativa de Colombia\n")
    print("1. Iniciar Sesión")
    print("2. Salir")
    opcion_inicio = input("Seleccione una opción: ")

    if opcion_inicio == '1':
        sistema_recetas.iniciar_sesion()

        if sistema_recetas.usuario_actual == 'chef':
            sistema_recetas.mostrar_menu_principal()

        elif sistema_recetas.usuario_actual == 'administrador':
            sistema_recetas.visualizar_ingredientes()
            sistema_recetas.visualizar_recetas()

    elif opcion_inicio == '2':
        break

    else:
        print("Opción no válida. Intente de nuevo.")
