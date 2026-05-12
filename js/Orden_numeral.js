let num1 = 7
let num2 = 16
let num3 = 4

let numeros = [num1, num2, num3];

numeros.sort(function(a, b) {
    return a - b;
});
console.log("Numeros en orden ascendente: ", numeros)