CLASE 3
--- 

Multimedia con HTML:

* imágenes, video, audio,iframes.
* Tablas.
    Herramienta de inspección.
    Validación de nuestro   HTML.

---

Bibliografia Recomendada: 
* TAG IMAGENES
    - Banco de Imagenes : 
        ▪️ Pixabay —
        🔗 https://pixabay.com/es/
    
        ▪️ Freepik —
        🔗 https://www.freepik.com/
    
        ▪️ Rawpixel —
        🔗 https://www.rawpixel.com/
    
        ▪️ Canva Stock Photos —
        🔗 https://lnkd.in/dfZibWEA
    
        ▪️ Flickr —
        🔗 https://flickr.com/
    
        ▪️ StockSnap —
        🔗 https://stocksnap.io/
    
        ▪️ Unsplash —
        🔗 https://lnkd.in/dYDKtPZm
    
        ▪️ StockVault —
        🔗 https://lnkd.in/d24_WrxU
    
        ▪️ Freeimages —
        🔗 https://lnkd.in/dpzBk6wQ
    
        ▪️ ShutterStock —
        🔗 https://lnkd.in/dYc7Krgb
    
        ▪️ Startup Stock —
        🔗 https://lnkd.in/d7vAUPCi
    
        ▪️ Burst —
        🔗 https://burst.shopify.com/
  *    TAG TABLE:
        [TABLE DOCUMENTATION](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table            )


---

Multimedia con HTML: 
- imágenes
- video
- audio
- iframes
---

* Tablas.
* Herramienta de inspección
* Validación de nuestro HTML


Imagenes : 
 se basa en el tipo de imagenes que te permite cargar desde la ruta de la fuente, puede ser una ruta local del server o URL
 - otro atributo es ALT ==> es lo que te sirve para poder colocar los nombres alternativos o incluso para  que el reader funcione.
 - medidas con {width && height}
[POR QUE ES IMPORTANTE LA ETIQUETA TAG](https://www.elegantthemes.com/blog/wordpress/what-is-an-alt-tag-and-how-should-you-use-it?retargeting=off)

_Adicional: Existe una etiqueta relativamente nueva que permite hacer lo mismo pero te da la posibilidad de tener distintas versiones de una imagen en distintos escenarios_

```
<picture>
    <source srcset="/media/cc0-images/surfer-240-200.jpg"
            media="(orientation: portrait)">
    <img src="/media/cc0-images/painted-hand-298-332.jpg" alt="">
</picture>

<picture>
  <source srcset="mdn-logo-wide.png" media="(min-width: 600px)" />
  <img src="mdn-logo-narrow.png" alt="MDN" />
</picture>

```

# FAVICON

Es el icono de nuestra app o website que le querramos colocar.

# AUDIO

Permiten cargar audio como elemento dentro de la website ==> utilidad? muchas si estas usando una website pensada para elementos que contenga inmersion, ivestigacion o una bodega de data.

# Video
Idem que la anterior, existen unas formas un poco más interesantes, sin embargo se usan para hacer muy buenos fondos de bg o mucho más detallados como pasajes interesantes de back

# iFrame
Elementos independientes no referidos a algo intrinsecos.
Existen muchos y que son dependientes de las plataformas a embeber


# TABLAS

Permiten concederle las posibilidades de organizar en tablas informacion requerida para muestra de datos

COMO SE COMPONE?

```
Me permite tener un espacio
    &nbsp;
```

table [

    th => TABLE header
    td => table data

    thead -> tr -> th
    tbody -> tr -> td
    tfoot -> tr -> th td
]

[ESTRUCTURA BASICA](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table)
[GENERADOR DE TABLAS](https://codebeautify.org/html-table-generator)