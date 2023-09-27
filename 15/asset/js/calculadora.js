const suma = function (a, b) {
  return a + b;
};

const sumaPower = (...params) => {
  let total = 0;
  for (let value of params) {
    total += value;
  }
  return total;
};

const resta = (a, b) => a - b;
const multiplicacion = (a, b) => a * b;
const division = (a, b) => {
  if (b == 0) {
    console.warn("Zapallo, como vas a diviri por cero??");
    return null;
  }
  return a / b;
};

function calculadora(callback, ...params) {
  return callback(...params);
  e;
  /*   if (action == "suma") {
    return a + b;
  }

  if (action == "resta") {
    return a - b;
  }

  if (action == "multiplicar") {
    return a * b;
  }

  if (action == "dividir") {
    return a / b;
  }

  return null; */
}

export { calculadora, suma, resta, multiplicacion, division, sumaPower };
