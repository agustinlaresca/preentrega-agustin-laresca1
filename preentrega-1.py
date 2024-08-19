# Diccionario
usuarios_db = {}

# registrar usuarios
def registrar_usuario(usuario, contraseña):
    if usuario in usuarios_db:
        print("Error: El usuario ya existe.")
    else:
        usuarios_db[usuario] = contraseña
        print("Usuario registrado exitosamente.")

# mostrar usuarios 
def mostrar_usuarios():
    if usuarios_db:
        print("Usuarios registrados:")
        for usuario, contraseña in usuarios_db.items():
            print(f"Usuario: {usuario}, Contraseña: {contraseña}")
    else:
        print("No hay usuarios registrados.")

# inicio de secion
def login(usuario, contraseña):
    if usuario in usuarios_db and usuarios_db[usuario] == contraseña:
        print("inicio de sesion exitoso.")
    else:
        print("Error: Usuario o contraseña incorrectos.")

# Programa general
while True:
    print("\nMenu Principal:")
    print("1. Registrar usuario")
    print("2. Mostrar usuarios")
    print("3. Iniciar sesion")
    print("4. Cerrar sesion")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        usuario = input("Ingresa el nombre de usuario: ")
        contraseña = input("Ingresa la contraseña: ")
        registrar_usuario(usuario, contraseña)
    elif opcion == "2":
        mostrar_usuarios()
    elif opcion == "3":
        usuario = input("Ingresa tu nombre de usuario: ")
        contraseña = input("Ingresa tu contraseña: ")
        login(usuario, contraseña)
    elif opcion == "4":
        print("cerrando sesion...")
        break
    else:
        print("Opción no válida, intenta de nuevo.")
