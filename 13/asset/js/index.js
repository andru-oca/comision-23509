console.log("acá estoy!! no me olvides! soy tu amigo JS :) ")


// let usuario = prompt("Carolina, por favor ingresa tu nombre")

// if (usuario == "CAROLINA"){
//     document.write(usuario)
// } 

// if (usuario != "CAROLINA"){
//     alert("GUARDA QUE ESTA MAL ESCRITO! DESPEDIDA!")
// }
let usuario = prompt("Ingrese el nombre de usuario: ")
let style=prompt("elegi tu estilo (hacker & smooth)") || 'hacker'

let edad = prompt("por favor ingrese su edad")
let edadTrue = Number(edad) + 6

let respuesta = `
    <header class="${style}">
      <center>
        <h1>Bienvenida, ${usuario}</h1>
        <hr />
        <marquee>Gracias por usar nuestros servicios</marquee>
        <h3>Edad declarada ${edad}</h3>
        <h4>Edad real es ${edadTrue}</h4>
      </center>
    </header>
`
document.write(respuesta)




