class ListaTareas:
    def __init__(self):
        self.tareas = []  # Lista para almacenar las tareas
    def agregar_tarea(self, tarea): # Agrega una nueva tarea a la lista
        while True:
            # Solicitar una nueva tarea si no se ingreso ningún caracter
            while not tarea:
                print("por favor, ingrese al menos un caracter")
                tarea = input("Ingrese el nombre de la tarea a agregar: ")
            # Verificar si ya existe en la lista la tarea
            for t in self.tareas:
                if t['tarea'] == tarea:
                    print(f"La tarea '{tarea}' ya existe en la lista.")
                    tarea = input("Ingrese una tarea valida y no duplicada: ")
                    break
            else:
                # Agregar la tarea a Lista de tareas pendientes
                self.tareas.append({'tarea': tarea, 'completada': False})
                print(f"Tarea '{tarea}' agregada a la lista de pendientes")
                break
    def eliminar_tarea(self, indice): # Elimina tarea de la lista
        if 0 <= indice < len(self.tareas):
            del self.tareas[indice]
        else:                         # De lo contrario imprime indice de Tarea no valido
            print("¡¡Índice de tarea no válido!!")

    def marcar_completada(self, indice): # Marca la tarea como completada
        if 0 <= indice < len(self.tareas):
            self.tareas[indice]['completada'] = True
        else:                            # De lo contrario imprime indice de tarea no valido
            print("¡¡Índice de tarea no válido!!")

    def mostrar_tareas(self): # Enumerar las tareas
        print(Fore.GREEN + "\n--- Tareas Pendientes ---")
        for i, tarea in enumerate(self.tareas): # Enumera las tareas pendientes
            if not tarea['completada']:
                print(f"{i + 1}. {tarea['tarea']}")

        print(Fore.GREEN + "\n--- Tareas Completadas ---")
        for i, tarea in enumerate(self.tareas): # Enumera las tareas completadas
            if tarea['completada']:
                print(f"{i + 1}. {tarea['tarea']}")

# En esta parte se crea el menu para q el usuario pueda elegir segun el caso
if __name__ == "__main__":
    lista_tareas = ListaTareas() 
    while True:
        from colorama import Fore, Back, init # Se inicializa libreria colorama para dar color a las lineas
        init()
        print(Fore.BLUE + "\n/// Lista de Tareas ///")
        lista_tareas.mostrar_tareas() # Muestra tareas pendientes y completadas
        print(Fore.CYAN + "\n1.- ♣ Agregar tarea ♣")
        print("2.- ♠ Eliminar tarea ♠")
        print("3.- ♦ Marcar tarea como completada ♦")
        print("4.- ♥ Visualizar tareas ♥")
        print("5.- ☻ Salir ☻")
        
        opcion = input(Fore.GREEN + "\nIngrese el número de la opción que desea realizar: ")
        
        if opcion == '1':
            tarea = input("Ingrese el nombre de la tarea a agregar: ")
            lista_tareas.agregar_tarea(tarea)
        elif opcion == '2':
            indice = int(input("Ingrese el número de la tarea que desea eliminar: ")) - 1
            lista_tareas.eliminar_tarea(indice)
        elif opcion == '3':
            indice = int(input("Ingrese el número de la tarea que desea marcar como completada: ")) - 1
            lista_tareas.marcar_completada(indice)
        elif opcion == '4':
            pass
        elif opcion == '5':
            print("¡¡Adiós!!")
            break 
        else:
            print("¡¡Opción no válida! Por favor ingrese una opción válida.!!")
# Este programa es hecho por Jorge Luis Mego Gutierrez para el
# curso de Python de IBM SkillBuil Mayo 2024