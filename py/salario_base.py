salario = int(input("Ingrese el salario base:"))
horas_extra = int(input("Ingrese la cantidad de horas extra: "))
valor = int(input("Ingrese el valor de una hora: "))

extra = horas_extra * valor
total = extra + salario

print("Salario todal", total )