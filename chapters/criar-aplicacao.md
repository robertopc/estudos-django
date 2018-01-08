# Criando aplicações

Os arquivos anteriores são os arquivos de base de um projeto. 
Para inserirmos nossas regras de negócio, precisamos criar aplicações.
O Django trabalha de maneira modular, e em cada parte do projeto devemos criar uma aplicação. 
Também podemos usar estas aplicações em outros projetos.

Para criarmos as aplicações, utilizamos o código a seguir.
```
python manage.py startapp nomedaaplicacao
```

Depois de criada, devemos inserir a aplicação no `INSTALLED_APPS`.

> Nota 1: Como aplicação principal, é uma convenção usar o nome `core`.

> Nota 2: Não pode nomear a aplicação com palavras reservadas do Django, por exemplo `site`.

