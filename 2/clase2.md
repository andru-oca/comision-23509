HTML Clase 2
----
## Repaso Clase 1
-    Template de una Pagina Web con las etiquetas semanticas que se realiza como formato general de todo proyecto.
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nombre WebSite</title>
</head>
<body>
    <header></header>
    <main></main>
    <footer></footer>
</body>
</html>

```
---

### tags comunes a aprender :

h1 ---> h6 :: encabezados necesarios para dar informacion a html que es un encabezadp

p    :: parrafos
br   :: salto de linea o quiebre

b        :: negrita
strong   :: negrita con importancia semantica

i        :: cursiva 
em       :: cursiva con importancia semantica

u        :: subrayado

---
Estructura base de carpetas a trabajar : 

```
└──nombre_project
    index.html
    └── pages
    └── assets
        ├── css
        ├── js
        └── media
            ├── audio
            ├── images
            └── video

```
---

Temario de clase:
*   Listas y enlaces.
*   Rutas absolutas y relativas.
*   Elementos en bloque y en línea.

---
Ejemplos:

### lista >> que es una lista? basicamente eso >> una lista tanto ordenada y sin tipo de orden cardinal

ol    ::    ordered list
ul    ::    unordered list

li    ::    items de la lista

dl    ::    definition list (muy bueno cuando tenemos que desarrollar items de informacion)

dl
    dt >> header
        dd >> sub-items


### enlaces | anchors

a    :: anchor - linkers
Son linkers que nos permiten relacionar tanto sectores como paginas
-    atributos importantes de los anchors
     -    href        ::    #id | email*
     -    target      ::    _blank , _parent ... etc
     -    download    ::    descarga desde un hipervinculo

* _email >> mailto:<mail@mail.com>?subject=Contancto de informacion?body=Quiero recibir un email con informacion_

_++ Detalle a tener en cuenta :: siempre te lo tiende a enviar a *SPAM*_

* _[data-extra sobre el mailto](https://www.w3docs.com/snippets/html/how-to-create-mailto-links.html)_

* Detalles muy interesantes:
    * Elementos en linea
      ```
        - <br>, <a>, <img>, <span>, <b>, <strong>, <mark>, <sub>
      ```
    * Elementos en bloque
      ```
        - <div>, <p>, <h1>..<h6>, <ul>, <ol>, <li>, <table>, <form>     
      ```
### RUTAS RELATIVAS Y ABSOLUTAS

-    ABSOLUTA : */usr/user-name/home/img/logos/html.png*
-    RELATIVA :  *./img/logos/html.png*

---
Lista para deploy

*    [Deploy en Netlify](https://www.netlify.com/?attr=homepage-modal)
*    [Deploy en Github Actions](https://pages.github.com/)
---

Herramientas para maquetado del proyecto : 
* [FIGMA](https://www.figma.com/)
* [DrawIo](https://app.diagrams.net/)
* [Excalidraw](https://excalidraw.com/)


---
Tarea para el Proyecto:
- Continuar con la formación de los grupos/equipos de 4 personas.

- Los estudiantes deberán armar una única planilla por comisión
para comenzar a anotarse. Luego lo informarán a través de un
formulario de Google. (:check)

- Comenzar a diagramar los layouts/estructura de cada página del
sitio web.

- Seleccion final del proyecto a trabajar
{{ Proyecto a trabajar }}
---
