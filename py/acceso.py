usuario_correcto1 = "David"
contraseña_correcta1 = "12345"

usuario_correcto2 = "Keiner"
contraseña_correcta2 = "654321"

usuario = input("Ingresa el usuario: ")
contraseña = input("Ingrese la contraseña: ")

if usuario == usuario_correcto1 and contraseña == contraseña_correcta1:
    print("Bienvenido")
    print("Tu rol es aprendiz")
elif usuario == usuario_correcto2 and contraseña == contraseña_correcta2:
    print("Bienbenido")
    print("Tu rol es ADMIN")
else:
    print("Error de ingreso")
    