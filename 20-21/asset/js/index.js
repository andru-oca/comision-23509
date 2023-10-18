import * as Vue from "https://unpkg.com/vue@3/dist/vue.esm-browser.js";
import { mainAppCore } from "./mainAppCore.Vue.js";
const { createApp } = Vue;

const mainId = "#main";
const mainApp = createApp(mainAppCore);

mainApp.mount(mainId);
