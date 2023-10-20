import { serie } from "./serie.Component.js";

export const mainCore = {
  data: function () {
    return {
      form: null,
      errorForm: null,
      errorPost: null,
      form_config_json: "./asset/js/form.Config.json",
      API_SERIES: "https://sheetdb.io/api/v1/al4zdaqjfcp8w",
      series: null,
      serie: {
        name: "",
        img: "",
        rating: "",
        episodes: "",
        release_year: "",
        sinopsis: "",
      },
    };
  },
  components: {
    serie: serie,
  },
  created: async function () {
    const response = await fetch(this.form_config_json);
    const error = response.statusText;

    if (!response.ok) {
      this.errorForm = error;
      return;
    }

    this.form = await response.json();
  },
  methods: {
    selectClick: function (id) {
      this.series = this.series.filter((serie) => serie.id == id);
    },
    getSeriesHandler: async function () {
      try {
        const response = await fetch(this.API_SERIES);

        if (!response.ok) {
          this.errorPost = response.statusText;
        }

        this.errorPost = "Aqui tá! ";

        this.series = await response.json();
      } catch (e) {
        this.errorPost = e;
      }
    },
    postSerieHandler: async function (event) {
      event.preventDefault();
      this.serie = {
        id: crypto.randomUUID(),
        created_: new Date().toISOString(),
        ...this.serie,
      };

      try {
        const response = await fetch(this.API_SERIES, {
          method: "POST",
          body: JSON.stringify(this.serie),
          headers: {
            "Content-Type": "application/json",
          },
        });

        if (!response.ok) {
          this.errorPost = response.statusText;
        }

        this.errorPost = "Se cargo con exito! :) ";
      } catch (e) {
        this.errorPost = e;
      }
    },
  },
};
