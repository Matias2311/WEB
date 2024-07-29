# cliente.py

class Cliente:
    clientes = []

    def __init__(self, nombre_usuario, contrasena, nombre_completo, email):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.nombre_completo = nombre_completo
        self.email = email

    @classmethod
    def registrar_cliente(cls, nombre_usuario, contrasena, nombre_completo, email):
        for cliente in cls.clientes:
            if cliente.nombre_usuario == nombre_usuario:
                print("Este nombre de usuario ya está registrado.")
                return False
        nuevo_cliente = cls(nombre_usuario, contrasena, nombre_completo, email)
        cls.clientes.append(nuevo_cliente)
        print(f"Usuario {nombre_usuario} registrado con éxito.")
        return True

    @classmethod
    def mostrar_clientes(cls):
        if cls.clientes:
            print("Usuarios registrados:")
            for cliente in cls.clientes:
                print(cliente)
        else:
            print("No hay usuarios registrados.")

    @classmethod
    def login_cliente(cls, nombre_usuario, contrasena):
        for cliente in cls.clientes:
            if cliente.nombre_usuario == nombre_usuario and cliente.contrasena == contrasena:
                print("Inicio de sesión exitoso.")
                return True
        print("Nombre de usuario o contraseña incorrectos.")
        return False

    def __str__(self):
        return f"Usuario: {self.nombre_usuario}, Nombre Completo: {self.nombre_completo}, Email: {self.email}"

    def actualizar_email(self, nuevo_email):
        self.email = nuevo_email
        print(f"Email actualizado a: {nuevo_email}")

    def cambiar_contrasena(self, nueva_contrasena):
        self.contrasena = nueva_contrasena
        print("Contraseña actualizada con éxito.")
