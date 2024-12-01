# Lista para almacenar los platos del menú
menu = []

def mostrar_menu_principal():
    print("\n--- Menú del Restaurante 'Segunda es Todo' ---")
    print("1. Añadir plato al menú")
    print("2. Buscar en el menú")
    print("3. Eliminar plato del menú")
    print("4. Mostrar platos del menú")
    print("5. Salir")

def añadir_plato():
    plato = input("Ingrese el nombre del plato que desea añadir: ").strip()
    if plato:
        menu.append(plato)
        print(f"Plato '{plato}' añadido al menú.")
    else:
        print("El nombre del plato no puede estar vacío.")

def buscar_plato():
    plato = input("Ingrese el nombre del plato que desea buscar: ").strip()
    if plato in menu:
        print(f"El plato '{plato}' está en el menú.")
    else:
        print(f"El plato '{plato}' no se encuentra en el menú.")

def eliminar_plato():
    plato = input("Ingrese el nombre del plato que desea eliminar: ").strip()
    if plato in menu:
        menu.remove(plato)
        print(f"Plato '{plato}' eliminado del menú.")
    else:
        print(f"El plato '{plato}' no se encuentra en el menú para eliminar.")

def mostrar_platos():
    if menu:
        print("\n--- Platos en el menú ---")
        for i, plato in enumerate(menu, start=1):
            print(f"{i}. {plato}")
    else:
        print("El menú está vacío.")

def main():
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == "1":
            añadir_plato()
        elif opcion == "2":
            buscar_plato()
        elif opcion == "3":
            eliminar_plato()
        elif opcion == "4":
            mostrar_platos()
        elif opcion == "5":
            print("Saliendo del programa. ¡Gracias por usar el menú de 'Segunda es Todo'!")
            break
        else:
            print("Opción no válida, por favor seleccione una opción entre 1 y 5.")

if __name__ == "__main__":
    main()