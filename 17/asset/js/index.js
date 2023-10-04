// Array
const { log } = console;

const dbUser = [];

dbUser.push("Carolina");
dbUser.push("Leo");

class Person {
  constructor({ name, credenciales }) {
    this.name = name;
    this.credenciales = credenciales ?? {
      obraSocial: "Sancor",
      id: crypto.randomUUID(),
    };
  }
}

dbUser.push(new Person({ name: "Axel" }));
dbUser.push(() => crypto.randomUUID());

log(dbUser);

dbUser[1] = "Leonardo Da Michi";

log(dbUser);

for (let user of dbUser) {
  log(user);
}

dbUser.forEach((u) => log(u));

dbUser.forEach((u) => {
  if (typeof u == "string") {
    log(u.toUpperCase());
    return;
  }
});

const resulta = dbUser.map((items) => items.length);
log(resulta);

let functionCreada = dbUser.pop();
log(functionCreada);
log(dbUser);

// import users from "./userDB.json" assert { type: "json" };

// log(users);

const URL = "./asset/js/userDB.json";

// fetch(URL, {})
//   .then((res) => res.json())
//   .then((data) => {
//     let usersPerson = data.map((u) => new Person({ name: u.name }));
//     log(usersPerson);
//   })
//   .catch((error) => log({ error }));

let cache = {};

function operacionPesada(num) {
  if (Object.keys(cache).includes(num)) {
    log(" ya lo calculé el valor es: ", cache[num]);
    return cache[num];
  }

  let valorRetorno = Number(num) ** 10;
  log(" no lo he calculado aun: ", valorRetorno);
  cache[num] = valorRetorno;
  return valorRetorno;
}

operacionPesada("7000000");
operacionPesada("7000000");

fetch(URL, {})
  .then((res) => res.json())
  .then((data) => {
    let usersPerson = data.map((u) => new Person({ name: u.name }));

    sessionStorage.setItem("users", JSON.stringify(usersPerson));
  })
  .catch((error) => log({ error }));

const [primerItem, ...resto] = JSON.parse(sessionStorage.getItem("users"));

log(primerItem.credenciales);

import { Render } from "./Render.js";
import { caroVirus as printer } from "./caroVirus.js";
const app = new Render("app");

const URL_LOCAL = "./asset/js/beer.json";
const API_URL = "https://api.sampleapis.com/beers/ale";

app.getData(API_URL, printer);
