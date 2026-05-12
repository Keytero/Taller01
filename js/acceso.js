let usuario_correcto = "David"
let contraseña_correcta = "12345"
let usuario_correcto1 = "Keiner"
let contraseña_correcta1 = "54321"

let usuario = "Keiner"
let contraseña = "54321"

if (usuario == usuario_correcto && contraseña == contraseña_correcta) {
    console.log("Bienvenido")
    console.log("Su rol es aprendiz")
}
else if (usuario = usuario_correcto1 && contraseña == contraseña_correcta1) {
    console.log("Bienvenido")
    console.log("Su rol es ADMIN")
}
else {
    console.log("Error de ingreso")
}
