mes = int(input("ingrese el mes: "))

if mes > 2 and mes < 6:
    print ("Estamos en primavera")
elif mes > 5 and mes < 9:
    print ("Estamos en verano")
elif mes > 8 and mes < 12: 
    print ("Estamos en otoño")
else: 
    print ("Estamos en invierno")