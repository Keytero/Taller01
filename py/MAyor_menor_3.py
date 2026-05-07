num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))
num3 = int(input("Ingresa el tercer numero: "))

if num1 > num2 and num1 > num3:
    print("El primer numero es el mayor")
    
elif num2 > num1 and num2 > num3:
    print("El segundo numero es el mayor")
    
else:
 print("El tercer numero es el mayor")