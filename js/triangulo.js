let lado1 = 8
let lado2 = 8
let lado3 = 8

if (lado1 === lado2 && lado1 === lado3) {
    console.log("El triangulo es Equilatero");
}
else if (lado1 === lado2 && lado1 === lado3 && lado2 === lado3) {
    console.log("El triangulo es Isoceles");
}
else {
    console.log("El triangulo es Escaleno")
}