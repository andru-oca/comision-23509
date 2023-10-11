// le indico las funcionalidades y los valores de inicializacion
import { textoLargo, vinos } from "./data_value.js";
export const appCore = {
  data: function () {
    return {
      // los valores de inicializacion
      count: 10,
      msg: "bienvenidos a Vue",
      textoLargo: textoLargo,
      display: true,
      vinos: vinos,
      vinosStyle: "vinoImage",
      cantidadVinos: vinos.length,
      vinosMostrados: vinos,
      mensaje: "",
    };
  },
};
