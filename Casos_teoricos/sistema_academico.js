function factorial(n) {
    let resultado = 1;

    for (let i = 1; i <= n; i++) {
        resultado *= i;
    }

    return resultado;
}



function esPrimo(numero) {

    if (numero <= 1) {
        return false;
    }

    for (let i = 2; i < numero; i++) {

        if (numero % i === 0) {
            return false;
        }
    }

    return true;
}



let estudiantes = [
    { nombre: "Santi", notas: [4.0, 3.5, 5.0] },
    { nombre: "Sofia", notas: [5.0, 4.8, 4.9] },
    { nombre: "Pedro", notas: [3.0, 3.2, 2.9] },
    { nombre: "William", notas: [4.0, 3.5, 5.0] }
];



function calcularPromedio(notas) {

    let suma = 0;

    for (let nota of notas) {
        suma += nota;
    }

    return suma / notas.length;
}



for (let estudiante of estudiantes) {
    estudiante.promedio = calcularPromedio(estudiante.notas);
}



let mejor = estudiantes[0];

for (let estudiante of estudiantes) {

    if (estudiante.promedio > mejor.promedio) {
        mejor = estudiante;
    }
}

console.log("Mejor estudiante:", mejor);



let sinDuplicados = [];
let nombres = [];

for (let estudiante of estudiantes) {

    if (!nombres.includes(estudiante.nombre)) {
        sinDuplicados.push(estudiante);
        nombres.push(estudiante.nombre);
    }
}

console.log("\nSin duplicados:", sinDuplicados);



function busquedaLineal(lista, nombre) {

    for (let estudiante of lista) {

        if (estudiante.nombre.toLowerCase() === nombre.toLowerCase()) {
            return estudiante;
        }
    }

    return null;
}



function busquedaBinaria(lista, nombre) {

    let izquierda = 0;
    let derecha = lista.length - 1;

    while (izquierda <= derecha) {

        let medio = Math.floor((izquierda + derecha) / 2);

        if (lista[medio].nombre.toLowerCase() === nombre.toLowerCase()) {
            return lista[medio];
        }

        else if (lista[medio].nombre.toLowerCase() < nombre.toLowerCase()) {
            izquierda = medio + 1;
        }

        else {
            derecha = medio - 1;
        }
    }

    return null;
}



function ordenBurbuja(lista) {

    let n = lista.length;

    for (let i = 0; i < n; i++) {

        for (let j = 0; j < n - i - 1; j++) {

            if (lista[j].promedio < lista[j + 1].promedio) {

                let temp = lista[j];
                lista[j] = lista[j + 1];
                lista[j + 1] = temp;
            }
        }
    }

    return lista;
}



function ordenSeleccion(lista) {

    let n = lista.length;

    for (let i = 0; i < n; i++) {

        let maximo = i;

        for (let j = i + 1; j < n; j++) {

            if (lista[j].promedio > lista[maximo].promedio) {
                maximo = j;
            }
        }

        let temp = lista[i];
        lista[i] = lista[maximo];
        lista[maximo] = temp;
    }

    return lista;
}

console.log("\n=== SISTEMA ACADÉMICO ===");

let ordenados = ordenBurbuja(sinDuplicados);

console.log("\nEstudiantes ordenados:");

for (let estudiante of ordenados) {
    console.log(estudiante.nombre, "-", estudiante.promedio);
}



const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Ingrese nombre a buscar: ", function(buscar) {

    let resultado = busquedaLineal(ordenados, buscar);

    if (resultado) {
        console.log("Encontrado:", resultado);
    } else {
        console.log("No encontrado");
    }

   
    console.log("\nMejor estudiante:");
    console.log(mejor.nombre, "-", mejor.promedio);

   
    console.log("\nFactorial de 5:", factorial(5));
    console.log("¿7 es primo?", esPrimo(7));

    rl.close();
});




console.log("\nMejor estudiante:");
console.log(mejor.nombre, "-", mejor.promedio);



console.log("\nFactorial de 5:", factorial(5));
console.log("¿7 es primo?", esPrimo(7));