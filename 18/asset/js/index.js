const { log } = console;

log(document);

let header = document.getElementsByTagName("header").item(0);
header.classList.add("carolina");

header.children[0].innerHTML = "<b>I ❤ NY</b>";

const espacioPublicitario = [
  "Karinaaaaaaaa!",
  "I ❤ NY",
  "Carolina, estas despedida!",
  "Pirulino se pego una borrachera",
  "Linux >>>>>>> Windows",
];

let i = 0;

const mensajesEnH1 = (mensajes) => {
  header.children[0].textContent = mensajes[i];
  i++;

  if (i == mensajes.length) {
    i = 0;
  }
};

setInterval(mensajesEnH1, 2_000, espacioPublicitario);

let main = document.querySelector("body > main");

log(main);

let footer = document.getElementById("flavia");

let footerByQuery = document.querySelector("body > [id='flavia']");

let footerByQuerySA = document.querySelectorAll("#flavia");

log(footer, footerByQuery, footerByQuerySA);

// addd items

let input = document.createElement("input");
let btn = document.createElement("button");

input.type = "number";
input.value = 10;
input.placeholder = "ingrese # cubitos".toUpperCase();

btn.innerText = "Agregar";

log(input, btn);

header.appendChild(input);
header.appendChild(btn);

/*--------BTN---------*/

const arturoClear = (parentNode) => {
  let cubitoscreados = Array.from(parentNode.children);
  cubitoscreados.forEach((cubito) => main.removeChild(cubito));
};

// let seleccionBtn = document.querySelector("header > button");

// seleccionBtn.addEventListener("click", () => {
//   arturoClear(main);

//   let inputValue = document.querySelector("input[type='number']");
//   log(inputValue.valueAsNumber);

//   const collectionDivs = [];

//   for (let i = 0; i < inputValue.valueAsNumber; i++) {
//     let div = document.createElement("div");

//     if (i % 2 == 0) {
//       div.classList.add("federico");
//     } else {
//       div.classList.add("dario");
//     }

//     collectionDivs.push(div);
//   }
//   inputValue.value = "";
//   collectionDivs.forEach((div) => main.appendChild(div));
// });

const TOKEN = "ibc6kpjwf51zz6b9qd991l2psw9yaaed0ls6hycn";
const URL = "https://sheetdb.io/api/v1/d0vtlcfmzacuu";

const flaviaRender = (ticket) => {
  let div = document.createElement("div");
  div.style.backgroundColor = ticket.color_status;

  let os = document.createElement("p");
  let email = document.createElement("p");

  os.innerText = ticket.sistema_operativo;
  email.innerText = ticket.email;

  os.style.color = "white";
  email.style.color = "white";

  div.appendChild(os);
  div.appendChild(email);

  div.addEventListener("click", () => {
    alert(` fecha de ticket: ${ticket.ticket_time}`);
  });

  return div;
};

const getElementsByTicket = () => {
  let main = document.querySelector("body > main");
  arturoClear(main);

  let limite = document.querySelector("input[type='number']").valueAsNumber;

  let url_limite = URL + `?limit=${limite}`;
  document.querySelector("input[type='number']").value = "";

  fetch(url_limite, {
    method: "GET",
    headers: {
      Authorization: `Bearer ${TOKEN}`,
    },
  })
    .then((res) => res.json())
    .then((data) => {
      data
        .map((ticket) => flaviaRender(ticket))
        .forEach((div) => main.appendChild(div));
    })
    .catch((error) => log({ error }));
};

let seleccionBtn = document.querySelector("header > button");

seleccionBtn.addEventListener("click", getElementsByTicket);
