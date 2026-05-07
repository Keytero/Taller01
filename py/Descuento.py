valor = int (input("ingrese el valor de su compra: "))
descuento = valor * 0.10
total = valor - descuento

if valor >= 100000:
    print ("descuento de:", descuento)
    print ("Total:", total, "pesos")
else:
    print ("no aplica descuento")
    print ("total:", valor, "pesos")