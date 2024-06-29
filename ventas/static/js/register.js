
function submitForm() {
var email = $("#exampleInputEmail1").val();
var password = $("#exampleInputPassword1").val();
var repeatPassword = $("#exampleInputPassword2").val();
var termsAccepted = $("#exampleCheck1").is(":checked");

if (email.trim() === "") {
    alert("Por favor, ingrese su dirección de correo electrónico.");
    return;
}

if (password.trim() === "") {
    alert("Por favor, ingrese su contraseña.");
    return;
}

if (repeatPassword.trim() === "") {
    alert("Por favor, repita su contraseña.");
    return;
}

if (password !== repeatPassword) {
    alert("Las contraseñas no coinciden.");
    return;
}

if (!termsAccepted) {
    alert("Debe aceptar los términos de la empresa.");
    return;
}

alert("¡Registro exitoso!\n\nEmail: " + email + "\nContraseña: " + password);


setTimeout(function() {
    window.location.href = "index.html";
}, 3000);
}