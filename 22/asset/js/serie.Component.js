export const serie = {
  template: `
  <div>
  <h2>{{serie.name}}</h2>
  <img v-bind:src="serie.img" :alt="serie.name" width="200" />
  <hr />
  <details>
    <p>La sinopsis es : {{serie.sinopsis}}</p>
    <p>Fecha lanzamiento : {{serie.release_date}}</p>
    <p>Rating es : {{serie.rating}} ⭐</p>
  </details>
</div>
  
  `,
  props: {
    serie: Object,
  },
};
