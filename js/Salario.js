let ingreso = 3500000
if (ingreso < 1500000) {
    console.log("Sin impuesto")
    console.log("Valor neto", ingreso);
}
else if (ingreso >= 1500000 && ingreso <= 3000000) {
    console.log("Impuesto del 10%")
    console.log("Valor neto", ingreso * 0.90);
}
else {
    console.log("Impuesto de 20%")
    console.log("Valor neto", ingreso * 0.80)
}