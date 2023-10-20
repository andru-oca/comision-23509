// importo libreria
import * as Vue from "https://unpkg.com/vue@3/dist/vue.esm-browser.js";
// asigno el metodo de vue a usar

import { mainCore } from "./mainCore.Vue.js";

const { createApp } = Vue;
// el id a ingestar
const mainID = "#main";
// la applicacion donde voy a renderizar
const mainApp = createApp(mainCore);
//renderizado
mainApp.mount(mainID);
