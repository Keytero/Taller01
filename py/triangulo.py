lado1 = int(input("Ingrese el primer lado"))
lado2 = int(input("Ingrese el segundo lado"))
lado3 = int(input("Ingrese el tercer lado"))

if lado1 == lado2 and lado1 == lado3:
    print("El triangulo es Equilatero")
elif lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
    print("El triangulo es Isoceles")
else:
    print("El triangulo es escaleno")