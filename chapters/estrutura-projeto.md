# Estrutura do projeto

Ao criar o projeto, o Django possui a seguinte estrutura.

```
__init__.py
settings.py
urls.py
wsgi.p
```

## __init__.py
Arquivo vazio para indicar ao Python que é um módulo.

## settings.py
Este é o arquivo principal do projeto, nele contém todas as configurações do projeto.

A seguir algumas das principais configurações a serem alteradas.
```python
DEBUG = True # Alterar para False em produção

LANGUAGE_CODE = 'en-us' # mudar para pt-br

TIME_ZONE = 'UTC' # mudar para America/Sao_Paulo

INSTALLED_APPS = [
... # lista com as aplicações instaladas
'nomedoprojeto.nomedaaplicacao', # adicionar as aplicações criadas dessa maneira
]
```
## urls.py

Este arquivo contém as rotas pra nossas aplicações, ou seja, as urls que direcionam para as Views.

## wsgi.py

Este arquivo é responsável pela interface entre o servidor web e o projeto.
