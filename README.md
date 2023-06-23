# socketio-api

#### Uma simples api feita em fastapi que manda mensagem para um client socketio
<hr>
#### 🎲 Rodando o Back End (servidor)

```bash
# Instale o pipenv 
$ pip install pipenv

# Instale as depedencias 
$ pipenv install

# Execute a aplicação em modo de desenvolvimento
$ uvicorn app.main:app --reload --port 8080

# Execute o comando no socketio cliente
$ python client.py

acesse <http://localhost:8080/docs>
```
#### 🎲 Rodando o Back End (cliente)

```bash
$ python client.py

```
