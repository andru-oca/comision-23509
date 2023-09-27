/**
 * Que son las funciones ?
 * Son objetos que nos permite simplificar , dividir, darle una responsabilididad unica y ser reutilizable bloques de codigo con funcionalidades
 * https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions
 * Formas simples > DeclaraciÃ³n | invocacion
 * Diferencia entre parametros y argumentos
 * RestParams
 * https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters
 * Valores de Retorno
 * https://medium.com/swlh/return-early-pattern-3d18a41bba8
 * Fail Fast | Guard Clause | Happy Path
 *
 * Tipos de funciones
 * https://www.linkedin.com/feed/update/urn:li:activity:7111533784428101632?utm_source=share&utm_medium=member_desktop
 *
 * SCOPE de una variable en una funcion
 * CALLBACKS
 * CLOUSURE
 */

/**
 * https://stackoverflow.com/questions/3922599/is-it-a-bad-practice-to-use-break-in-a-for-loop
 *
 */

/**
 * 
 keyword function

function <nombre_function>(params){
    ...code
    return 
}
*/
//

import {
  calculadora,
  suma,
  resta,
  multiplicacion,
  division,
  sumaPower,
} from "./calculadora.js";

/* function saludar(nombre = "patricio") {
  let apellido = "plumifero";
  return `${nombre} ${apellido}`;
}

let valorRetorno = saludar();

console.log(valorRetorno); */

// CALCULADORA que me trabaje con n parametros

let valorRetorno = calculadora(multiplicacion, 1, -1, 2, 3);

console.log(valorRetorno);

// INPUT que al ingresar un año me valide si es bisiesto
// que me retorne una impresion en un h1 de mi html

import { leapYear, leapYearNewWave } from "./leapYear.js";
import { getContainer, response } from "./response.js";

let inputContainer = getContainer("year");
let writer = response("response");

inputContainer.addEventListener("keydown", (event) => {
  if (event.key == "Enter") {
    let bisiesto = leapYearNewWave(inputContainer.valueAsNumber);
    writer(
      bisiesto
        ? "YUJU!! TENEMOS UN DIA MAS DE VACAS 🍢"
        : "Uh! SE me termina las vacas 😕"
    );
  }
});
