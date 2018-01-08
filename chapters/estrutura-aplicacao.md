# Estrutura da Aplicação

Ao criarmos a aplicação, é gerada a estrutura padrão a seguir.

```
__init__.py  
admin.py  
apps.py  
migrations/
    __init__.py
models.py  
tests.py  
views.py
```

### \_\_init\_\_.py

O mesmo que o \_\_ini\_\_.py do Projeto[¹](#initpy).

### admin.py

Este arquivo contém os modelos para o backend desta aplicação.

### apps.py

Este arquivo descreve configurações da aplicação.

### migrations/

Diretório contendo as migrações para o banco de dados, ou seja, um versionamento do banco de dados feito pelo ORM.

### models.py

Este arquivo contém os modelos de dados da aplicação. As classes deste arquivo são usadas pelo ORM para criar a estruturas de dados do banco de dados.

### tests.py

Este é o arquivo onde devem ser escritos os testes da aplicação.

### views.py

Este é o arquivo controlador da aplicação, ele faz a interface entre os modelos e os templates.

