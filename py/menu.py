print("MENÚ")
print("1. Saludar")
print("2. Fecha")
print("3. Salir")

opcion = int(input("Seleccione una opción: "))

if opcion == 1:
    print("Elegiste Saludar")
    print ("Hola, como estás?")
elif opcion == 2:
    print("Elegiste Fecha")
    print("Hoy es 23 de Mayo del 2015")
elif opcion == 3:
    print("Elegiste Salir")
    print("saliendo del programa...")
else:
    print("Error")

