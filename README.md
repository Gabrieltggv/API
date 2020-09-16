# API
Code developed for training to create an api

Configurando ambiente virtual e instalando dependências:
```
* Pipenv shell
* Pipenv install 
```
Para conferir a qualidade do codigo:
```
* flake8
```
Para configurar e rodar a api:

```
export FLASK_APP=app/app.py
export FLASK_DEBUG=True
export FLASK_ENV=Development

flask run
``` 

Realizando as migrações:
```
flask db init
flask db migrate
flask db upgrade
```

Estudo com flask e suas ferramentas:

* flask
* flask_sqlalchemy
* flask_migrate 
* flask_marshmallow
* marshmallow_sqlalchemy