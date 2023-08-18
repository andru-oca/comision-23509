import { API_URL } from "./config.js";

document.querySelector("form").addEventListener("submit", async (e) => {
    e.preventDefault();

    const form = document.querySelector("form");

    let dataForm = new FormData(form);

    dataForm.append("ticket_time", new Date().toString());

    await fetch(API_URL, {
        method: "POST",
        body: dataForm,
    });

    form.classList.add("animation");

    alert("Gracias por tu mensaje");

    window.location.href = API_URL;
});
