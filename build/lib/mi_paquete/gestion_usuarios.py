# gestion_usuarios.py

usuarios = {}

def almacenar_usuario(nombre_usuario, contrasena):
    if nombre_usuario in usuarios:
        print("Este nombre de usuario ya está registrado.")
        return False
    else:
        usuarios[nombre_usuario] = contrasena
        print(f"Usuario {nombre_usuario} registrado con éxito.")
        return True

def registrar_usuario():
    nombre_usuario = input("Introduce el nombre de usuario: ")
    contrasena = input("Introduce la contraseña: ")
    almacenar_usuario(nombre_usuario, contrasena)

def mostrar_usuarios():
    if usuarios:
        print("Usuarios registrados:")
        for usuario, contrasena in usuarios.items():
            print(f"Usuario: {usuario}, Contraseña: {contrasena}")
    else:
        print("No hay usuarios registrados.")

def login_usuario():
    nombre_usuario = input("Introduce el nombre de usuario: ")
    contrasena = input("Introduce la contraseña: ")
    if nombre_usuario in usuarios and usuarios[nombre_usuario] == contrasena:
        print("Inicio de sesión exitoso.")
    else:
        print("Nombre de usuario o contraseña incorrectos.")
