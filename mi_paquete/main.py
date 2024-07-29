# main.py

from mi_paquete.cliente import Cliente
from mi_paquete.gestion_usuarios import registrar_usuario, mostrar_usuarios, login_usuario

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Registrar usuario (Objeto Cliente)")
        print("2. Mostrar usuarios (Objeto Cliente)")
        print("3. Iniciar sesión (Objeto Cliente)")
        print("4. Registrar usuario (Función Simple)")
        print("5. Mostrar usuarios (Función Simple)")
        print("6. Iniciar sesión (Función Simple)")
        print("7. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre_usuario = input("Introduce el nombre de usuario: ")
            contrasena = input("Introduce la contraseña: ")
            nombre_completo = input("Introduce el nombre completo: ")
            email = input("Introduce el email: ")
            Cliente.registrar_cliente(nombre_usuario, contrasena, nombre_completo, email)
        elif opcion == "2":
            Cliente.mostrar_clientes()
        elif opcion == "3":
            nombre_usuario = input("Introduce el nombre de usuario: ")
            contrasena = input("Introduce la contraseña: ")
            Cliente.login_cliente(nombre_usuario, contrasena)
        elif opcion == "4":
            registrar_usuario()
        elif opcion == "5":
            mostrar_usuarios()
        elif opcion == "6":
            login_usuario()
        elif opcion == "7":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 7.")

if __name__ == "__main__":
    menu()
