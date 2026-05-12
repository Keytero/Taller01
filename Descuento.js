let valor = 350000
let descuento = valor * 0.10
let total = valor - descuento

if (valor >= 100000) {
    console.log ("descuento:", descuento)
    console.log ("total:", total, "pesos");
}
else {
    console.log ("no aplica descuento")
    console.log ("total:", valor, "pesos")
}