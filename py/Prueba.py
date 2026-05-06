num1 = int(input("Ingresa un número entre 0 y 10: "))
num2 = int(input("Ingresa otro número entre 0 y 10: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)

if num2 == 0:
    print("¡Error! no se puede dividir entre 0")
else:
    division = num1 / num2
    print("División:", division)
if num1 == 0:
    print("¡Error! no se puede dividir entre 0")