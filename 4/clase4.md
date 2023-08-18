Clase 4
---

## FORMULARIOS 

Todos los formularios estan pensado para realizar una accion en particular, que puede permitir enviar por 
medio de metodos de ingesta.

Existen distintos tipos de datos que permitimos generar por medio de distintos inputs.

Si bien esto se puede realizar de distintas maneras, la forma tradicional es enviando estos datos a distintas
fuentes de almacenaje, que por ahora y que se va a ver con mayor ahinco es con una API en la nube.

Todas los tipos de input :
[ETIQUETA DEL TIPO INPUT](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input)


---

Existe una pagina que me permite generar una api en donde me permite ingestar datos de un formulario.

[SheetDB](https://sheetdb.io/)

```
Formas de hacer un fetch segun documentacion hacia una API

Getting Data

data =
{
 nombre
,apellido
,email
,genero
,edad
,sistema operativo
,ticket
,mensaje
}


URL to connect : https://sheetdb.io/api/v1/qda6n8oloujo9

await fetch(
    url ,
    {
        method : "POST" ,
        headers: {
            "Content-Type":"application/json"
        }
        body: JSON.stringify(data)
    }
)

```
