const { log } = console;

function Persona({ nombre, email, lenguajes, credenciales, status }) {
  this.nombre = nombre;
  this.email = email;
  this.lenguajes = lenguajes;
  this.credenciales = credenciales;
  this.status = status ?? true;
}

Persona.prototype.declararLenguajes = function () {
  let mensajes = "";
  for (let lenguaje of this.lenguajes) {
    mensajes += `yo, ${this.nombre} sé ${lenguaje}\n`;
  }
  log(mensajes);
};

// Persona.prototype.saludar = () => log(`soy , ${this.nombre}`);

export { Persona };
