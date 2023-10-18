const form = {
  name: {
    label: "Nombre de usuario",
    type: "text",
    placeholder: "Ingrese nombre de usuario",
  },
  email: {
    label: "Email del usuario",
    type: "email",
    placeholder: "Ingrese email",
  },
  dob: {
    label: "Fecha de nacimiento",
    type: "date",
    placeholder: "",
  },
  pass: {
    label: "Password del user",
    type: "password",
    placeholder: "Ingrese su password",
  },
  avatar: {
    label: "Ingrese link de avatar",
    type: "url",
    placeholder: "https://url/pic.jpg",
  },
};

const usuarioComponente = {
  template: `
    <div>
    <h1>{{user.name}}</h1>
    <img :src="user.avatar" width="300" />
    <hr />
    <ul>
      <li>Fecha de creacion: {{user.fecha_creacion}}</li>
      <li>Identificacion: {{user.id}}</li>
      <li>e-Mail: {{user.email}}</li>
    </ul>
  </div>
    `,
  props: {
    user: Object,
  },
};

export const mainAppCore = {
  data: function () {
    return {
      API: "https://sheetdb.io/api/v1/kft1ar9t64d45",
      errorPost: null,
      titulo: "Formulario de gestion de usuario",
      form: form,
      usuarioInput: {
        name: "",
        email: "",
        dob: "",
        pass: "",
        avatar: "",
      },
      users: [],
    };
  },
  components: {
    vueuser: usuarioComponente,
  },
  methods: {
    getUsersHandler: async function () {
      try {
        const response = await fetch(this.API, {});
        this.users = await response.json();
      } catch (error) {
        this.errorPost = error;
      }
    },
    agregarUserHandler: function (e) {
      e.preventDefault();
      const newUser = {
        id: crypto.randomUUID(),
        fecha_creacion: new Date().toISOString(),
        ...this.usuarioInput,
      };

      this.usuarioInput = {
        name: "",
        email: "",
        dob: "",
        pass: "",
        avatar: "",
      };

      fetch(this.API, {
        method: "POST",
        body: JSON.stringify(newUser),
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((respuesta) => {
          if (respuesta.ok) {
            this.errorPost = "Transaccion exitosa!";
            return;
          }

          throw new Error("Aca! un error!");
          return;
        })
        .catch((error) => (this.errorPost = error));
    },
  },
};
