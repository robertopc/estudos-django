# Models

Modelo é a parte responsável pela estrutura de dados da aplicação.
Nela criamos as Classes que serão transformadas em tabelas no banco de dados pelo ORM.
Cada modelo deve herdar de `django.db.models.Model`, 
assim o Django nos dá uma API de acesso ao banco de dados no objeto.
Os atributos desta Classe são os campos da tabela no banco.

Abaixo segue um Exemplo de Model:
```python
from django.db import models

class Pessoa(models.Model):
  nome = models.CharField(max_length=20)
  sobrenome = models.CharField(max_length=30)
```

Este Model criará uma tabela no banco de dados chamada `Pessoa` e terá os campos: `nome` e `sobrenome`.

Após criado o modelo, é necessário rodar dois comandos no terminal pra criar as tabelas.

```bash
python manage.py makemigrations # cria as migrações
python manage.py migrate # migra os modelos
``` 

> Nota 1: Só será criada migrações das aplicações em `INSTALLED_APPS`.
