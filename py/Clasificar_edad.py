edad = int(input("Inrese su edad: "))

if edad >= 0 and edad <= 12:
    print("Niño")
elif edad >= 13 and edad <= 17:
    print("Joven")
elif edad >= 18 and edad <= 59:
    print("Adulto")
else:
    print("Adulto mayor")