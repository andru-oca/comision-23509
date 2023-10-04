export function caroVirus(data) {
  let items = "";

  data.forEach((pinta) => {
    let template = `
            <div>
            <img src="${pinta.image}" alt="${pinta.name}">
            <div>
            <h2>precio : ${pinta.price}</h2>
            <p>${pinta.name}</p>
            </div>
            </div>
            `;

    items += template;
  });

  return items;
}
