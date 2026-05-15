def factorial(n):
    resultado = 1

    for i in range(1, n + 1):
        resultado *= i

    return resultado



def es_primo(numero):
    if numero <= 1:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True



estudiantes = [
    {"nombre": "Jose", "notas": [4.0, 3.5, 5.0]},
    {"nombre": "Saray", "notas": [5.0, 4.8, 4.9]},
    {"nombre": "Lucas", "notas": [3.0, 3.2, 2.9]},
    {"nombre": "David", "notas": [4.0, 3.5, 5.0]}
]



def calcular_promedio(notas):
    return sum(notas) / len(notas)



for estudiante in estudiantes:
    estudiante["promedio"] = calcular_promedio(estudiante["notas"])



mejor = estudiantes[0]

for estudiante in estudiantes:
    if estudiante["promedio"] > mejor["promedio"]:
        mejor = estudiante

print("Mejor estudiante:", mejor["nombre"], mejor["promedio"])



sin_duplicados = []
nombres = set()

for estudiante in estudiantes:
    if estudiante["nombre"] not in nombres:
        sin_duplicados.append(estudiante)
        nombres.add(estudiante["nombre"])

print("\nLista sin duplicados:")
for e in sin_duplicados:
    print(e)




def busqueda_lineal(lista, nombre):
    for estudiante in lista:
        if estudiante["nombre"].lower() == nombre.lower():
            return estudiante

    return None



def busqueda_binaria(lista, nombre):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if lista[medio]["nombre"].lower() == nombre.lower():
            return lista[medio]

        elif lista[medio]["nombre"].lower() < nombre.lower():
            izquierda = medio + 1

        else:
            derecha = medio - 1

    return None



def orden_burbuja(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):

            if lista[j]["promedio"] < lista[j + 1]["promedio"]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista



def orden_seleccion(lista):
    n = len(lista)

    for i in range(n):
        maximo = i

        for j in range(i + 1, n):
            if lista[j]["promedio"] > lista[maximo]["promedio"]:
                maximo = j

        lista[i], lista[maximo] = lista[maximo], lista[i]

    return lista




print("\n=== SISTEMA ACADÉMICO ===")

ordenados = orden_burbuja(sin_duplicados)

print("\nEstudiantes ordenados:")

for estudiante in ordenados:
    print(estudiante["nombre"], "-", estudiante["promedio"])


buscar = input("\nIngrese nombre a buscar: ")

resultado = busqueda_lineal(ordenados, buscar)

if resultado:
    print("Encontrado:", resultado)
else:
    print("No encontrado")


print("\nMejor estudiante:")
print(mejor["nombre"], "-", mejor["promedio"])



print("\nFactorial de 5:", factorial(5))
print("¿7 es primo?", es_primo(7))