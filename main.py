from regitrar import registrar_Libro 
from consultar import consultar_libros
from eliminar import eliminar_Libro

def menu():
    while True:
        print("\n--- Sistema de Biblioteca ---")
        print("1. Registrar Libro")
        print("2. Consultar Libros")
        print("3. Registrar Prestamo")
        print("4. Consultar Prestamo")
        print("5. Cancelar Presttamo")
        print("0. Salir")
        
        try:
            opcion = int(input("Seleccione una opciin: "))
        except ValueError:
            print("Error: Por favor, ingrese un número vido.")
            continue

        if opcion == 1:
            nombre = input("Nombre del Libro: ")
            try:
                estudiante = (input("estudiante: "))
                Libro_id = (input("Libro_id: "))
                fecha = (input("fecha: "))
                registrar_Libro(estudiante, Libro_id, fecha)
            except ValueError:
                print("Error rientente con las opciones validas")
        elif opcion == 2:
            consultar_libros()
        elif opcion == 3:
            Usuario = input("Nombre del estudiante: ")
            try:
                
                
        elif opcion == 4:
            consultar_reservas()
        elif opcion == 5:
            try:
                id_res = int(input("ID de la reserva a cancelar: "))
                cancelar_reserva(id_res)
            except ValueError:
                print("Error: El ID debe ser un numero.")
        elif opcion == 0:
            print("Saliendo")
            break
        else:
            print("Reintente.")

if __name__ == "__main__":
    menu()