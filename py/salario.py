ingresos = int(input("Poner sus ingresos: "))

if ingresos < 1500000:
    print ("Sin impuestos")
    print ("Valor neto", ingresos)
elif ingresos >= 1500000 and ingresos <= 3000000:
    print ("Impuesto del 10%")
    print ("Valor neto", ingresos * 0.90)
else:
    print("Impuesto del 20%")
    print ("Valor neto", ingresos * 0.60)
    