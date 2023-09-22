import { respuesta, respuestaError, respuestaEspecial } from "./respuesta.js";
import { frutas } from "./frutas.js";
import { userName, pwd } from "./userDB.js";

console.log("hello world");

console.table({
  /*BOOL de AND*/

  true_true: true && true,
  true_false: true && false,
  false_true: false && true,
  false_false: false && false,
});

console.table({
  /*BOOL de ORs*/

  true_true: true || true,
  true_false: true || false,
  false_true: false || true,
  false_false: false || false,
});
/* 
let userName = prompt("usuario, ingrese su nombre");

let pwd = prompt("usuario, ingrese su constraseña"); */

/* if (userName == "") {
  document.body.innerHTML = respuestaError;
} else if (userName == "pepebot") {
  document.body.innerHTML = respuestaEspecial;
} else {
  if (pwd === "1234") {
    document.body.innerHTML = respuesta;
  } else {
    alert("usuario no registrado o no valido");
  }
} */

/* let edad = prompt("ingrese edad");

isNaN(Number(edad))
  ? console.log("el zapallo se olvido la edad")
  : alert("esta bien la edad dale gas"); */

/**
 *FOR - While
 *
 */

/* let cantidad = prompt("ingrese cantidad");

cantidad = isNaN(Number(cantidad)) ? 3 : cantidad;

let data = "<center class='especial'>";

for (let i = 0; i < cantidad; i++) {
  data += ` <span>${frutas[i]}</span>`;
}

data += "</center>";

document.body.innerHTML = data;

 */

/* for (let i = 0; i < 10; i++) {
  console.error("permite break");
  if (i == 2) {
    break;
  }
} */

/* let user, pass;
let acc = 0;

while (true && acc <= 2) {
  console.log("inteno numero: " + acc);

  user = prompt("ingrese su usuario");
  pass = prompt("ingrese su password");

  if (user == userName && pass == pwd) {
    document.body.innerHTML = respuesta;
    break;
  } else {
    alert("algo está mal ;) ");
    acc++;
  }
}

 */

let user, pass;
let acc = 0;

let flag = true;

while (flag && acc <= 2) {
  console.log("inteno numero: " + acc);

  user = prompt("ingrese su usuario");
  pass = prompt("ingrese su password");

  if (user == userName && pass == pwd) {
    document.body.innerHTML = respuesta;
    flag = !flag;
  } else {
    alert("algo está mal ;) ");
    acc++;
  }
}

/*

  UN LOGIN 
  - PEDIRTE TU EMAIL
  - PASS

  MATCH ==> RENDER > BIENVENIDO nombre de usuario
  !MATCH => alert ("el password es incorrecto") si el pass es incorrecto
  !MATCH => alert("el email es incorrecto") si el email es incorrecto
  */
