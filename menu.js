console.log("MENÚ");
console.log("1. Saludar");
console.log("2. Fecha");
console.log("3. Salir");

let opcion = 3

if (opcion === 1) {
    console.log("Elegiste Saludar")
    console.log("Hola, cómo estás?");
} else if (opcion === 2) {
    console.log("Elegiste Fecha")
    console.log("Estamos a 12 de enero del 1099");
} else if (opcion === 3) {
    console.log("Elegiste Salir")
    console.log("Saliendo del programa...");
} else {
    console.log ("Error")
}