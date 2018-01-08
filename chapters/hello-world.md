# Criando um Hello World

Para criar uma aplicação de Hello World no Django, primeiro utilizaremos o comando de criação de aplicação.
```
python manage.py startapp core
```

Em seguida inseriremos o seguinte código no `views.py`.

```python
from django.shortcuts import render
from django.http import HttpResponse

def home(request): # views sempre devem receber o parametro 'request'
    return HttpResponse('<h1>Hello World!</h1>')

```

Neste exemplo passamos a mensagem de forma bruta para o servidor, não utilizamos templates(o que não é a maneira mais correta).
A seguir devemos inserir a rota da aplicação no `urls.py` do projeto. Segue o código do `urls.py`.

```python
from django.conf.urls import url
from django.contrib import admin

from todo.core import views # primeiro importamos as views da aplicação

urlpatterns = [
    url(r'', views.home ), # adicionamos a rota a views.home
    url(r'^admin/', admin.site.urls),
]
```

