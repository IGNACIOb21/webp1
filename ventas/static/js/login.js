// ADMIN = admin Pass = 1234

$(document).ready(function() {
    $("h2.texto.container").click(function() {
        window.location.href = "bienvebida.html";
    });
});

function loguear(){
    let user = document.getElementById("usuario").value;
    let pass = document.getElementById("clave").value;

    if (user == "admin" && pass == "1234"){
        window.location = "bienvebida.html";
    } else {
        alert("El nombre o la contraseña esta incorrecta");
    } 
}



