# Criando um Hello World com templates

No exemplo a seguir criaremos um Hello World com arquivos de template. 

Primeiro devemos criar os diretórios `static` e `templates` dentro da aplicação.
```bash
cd core          # diretório da aplicação
mkdir static
mkdir static/css # diretório para css
mkdir static/js  # diretório para js
mkdir templates
``` 
Criaremos 3 arquivos: 2 estáticos(css e js) e 1 template(html).

**base.html** em `templates/`
```html
<!doctype html>
<html>
<head>
    <title>Hello World</title>
</head>
<body>
    <div id="container">

        <h1 id="container-h1">Hello World<br><br><span></span></h1>

    </div>
</body>
</html>
```

> Nota: base.html é uma convenção de nome.

**custom.css** em `static/css/`
```css
body {
    background: #ccc;
}

#container {
    position: absolute;
    top: 33%;
    left: 33%;
    width: 33%;
    height: 33%;
    border: #000 1px solid;
    background: #fff;
    text-align: center;
    vertical-align: center;
}
```
**custom.js** em `static/js/`
```js
function horaAgora() {

    var horas = new Date().getHours();
    var minutos = new Date().getMinutes();
        minutos = minutos < 10 ? '0' + minutos : minutos ;
    var segundos = new Date().getSeconds();
    document.querySelector('#container-h1 span').innerHTML = horas + ':' + minutos + ':' + segundos;
}

setInterval(function() {

    horaAgora();
}, 1000);
```

Com estes arquivos somos capazes de criar a estrutura de templates do Django. Agora vamos editar o `base.html` para ele ler os arquivos estáticos.
O código a seguir é o arquivo editado com as `template tags` do Django.

```html
{% load staticfiles %}
<!doctype html>
<html>
<head>
    <title>Hello World</title>

    <link href="{% static "css/custom.css" %}" rel="stylesheet">
</head>
<body>
    <div id="container">

        <h1 id="container-h1">Hello World<br><br><span></span></h1>

    </div>

    <script src="{% static "js/custom.js" %}"></script>
</body>
</html>
```

Pra finalizar modificaremos a `views.py` da aplicação com o código.

```python
from django.shortcuts import render

def home(request):
    return render(request, 'base.html')

```
Agora é só rodar o servidor e ver o resultado!

