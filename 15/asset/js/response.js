const getContainer = (containerID) => document.getElementById(containerID);

const response = (containerID) => {
  // Closures
  let contenedor = document.getElementById(containerID);

  return (texto) => (contenedor.innerHTML = texto);
};

export { getContainer, response };
