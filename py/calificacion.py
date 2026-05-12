nota = int (input("ingrese la nota: "))

if nota >= 45:
    print("Usted saco una excelente nota")
elif nota < 45 and nota >= 40:
    print ("Usted saco una buena nota")
elif nota < 40 and nota >= 30:
    print ("Usted aprobó")
else:
    print("Usted desaprobó")