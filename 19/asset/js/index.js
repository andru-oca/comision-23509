import * as Vue from "https://unpkg.com/vue@3/dist/vue.esm-browser.js";
import { appCore } from "./appCore.vue.js";
const { createApp } = Vue;

// le indico donde voy a renderizar
const appID = "#app";

// genero la app a trabajar por Vue
const app = createApp(appCore);

// montar o renderizar mi app
app.mount(appID);

// createApp({
//   data() {
//     return {
//       count: 0,
//     };
//   },
// }).mount("#app");
