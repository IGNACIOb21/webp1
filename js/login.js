
$(document).ready(function() {
    $("h1").click(function() {
        window.location.href = "http://127.0.0.1:5500/index.html";
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



