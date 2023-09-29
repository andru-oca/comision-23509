/*

    OBJECT
    attr
        - name
        - CBU
        - edad

    metodos
        greet()
        aprobarTP()

*/

const log = console.log;

const flavia = {
  nombre: "flavia",
  email: "flavia@mail.com",
  lenguajes: ["js", "golang", "ASM"],

  declararLenguajes: function () {
    let mensajes = "";
    for (let lenguaje of this.lenguajes) {
      mensajes += `yo, ${this.nombre} sé ${lenguaje}\n`;
    }
    log(mensajes);
  },
};

log(flavia);

import { Persona } from "./Persona.js";

const caro = new Persona({
  cbu: 891729387189237,
  cantiDespidos: 6,
  nombre: "carolina",
  email: "caro@mail.com",
  lenguajes: ["Js", "Python", "Jeringozo", "Cantones"],
  credenciales: {
    osde: "OSDE-666",
    netflix: "Arg-Pirulo",
    marDelPlata: {
      alias: "coraline",
      tajer: 888123123123,
    },
  },
});

log(caro);
caro.declararLenguajes();
//caro.saludar();

// ===>

import { User } from "./User.js";
const dario = new User({ userName: "Dario" });

log(dario);

dario.showdata();
dario.changeStatus();
dario.showdata();

import { AndruFW } from "./AndruFW.js";

const app = new AndruFW("app");
app.render(
  `
  <center>
    <marquee behavior="" direction="">
      <h1> TIEMBAL REACT!!</h1>
    </marquee>
  </center>`
);
