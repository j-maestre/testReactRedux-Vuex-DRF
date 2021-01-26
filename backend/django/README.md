# Users REST API

API REST para gerenciamento, consulta e pesquisa de informações básicas de usuários, endereços e informações profissionais. Desenvolvida com Django Rest Framework e utilizando Docker, PostgreSQL e Redis.

## Pré requisitos

Para executar o projeto são necessários o docker e docker-compose instalados.

Para instalar o docker no ubuntu são necessários os comandos:  

`sudo apt update`  

`sudo apt install apt-transport-https ca-certificates curl software-properties-common`  

`curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`  

`sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"`  

`sudo apt update`  

`sudo apt install docker-ce`  


Para instalar o docker-compose são necessários os comandos:  

`sudo curl -L "https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`  

`sudo chmod +x /usr/local/bin/docker-compose`  


Para instalar no Linux Manjaro são necessários os comandos:  

`sudo pacman -S docker`  

`sudo pacman -S docker-compose`  


Para iniciar o docker:  

`sudo systemctl start docker`

No Windows basta fazer o download e instalação do Docker Community Edition for Windows onde já estão presentes o docker e docker-compose

## Instalação

Para executar o projeto abra um terminal e vá até o diretório do projeto. Dentro do diretório execute o comando `sudo docker-compose build` e depois o comando `sudo docker-compose up -d`. Com esses comandos as imagens e containers serão criados. Segundo as configurações dos arquivos originais a API estará ouvindo em localhost:8000 ou 0.0.0.0:8000.

Para confirmar se a aplicação está funcionando pode ser enviada uma requisição HTTP GET utilizando o programa Postman ou similar para o endpoint /users (localhost:8000/users/ ou 0.0.0.0:8000/users/).

A resposta recebida deve ser similar a seguinte:  
```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Connection: keep-alive
Content-Length: 2
Content-Type: application/json
Date: Wed, 19 Sep 2018 02:50:09 GMT
Server: nginx/1.15.3
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

[]
```  

## Autenticação 

A api pode ser executada utilizando autenticação ou não. A variavel de ambiente para configurar o uso de autenticação é definida no comando `export API_AUTHENTICATION="False"` no arquivo docker-compose.yml, para usar a autenticação o comando deve ser alterado para export API_AUTHENTICATION="True". Caso a autenticação não seja utilizada nenhum dado poderá ser adicionado ou alterado, os dados estarão disponiveis apenas para visualização.

Para utilizar a autenticação crie um usuario administrador para realizar autenticação e adição e alteração de usuarios no endpoint /users:
- `docker exec -ti usersRestAPI01 /bin/bash`
- `python manage.py createsuperuser --username admin --email admin@admin.com`

E digitar a senha para o usuario duas vezes.

## Como usar

### Listar todos os usuários cadastrados:
URL: 0.0.0.0:8000/users/
Método GET

Resposta:
Status: 200 OK
```
[
    {
        "id": 1,
        "name": "teste 1",
        "deion": "teste 1 - profession 1",
        "RG": "178318966",
        "CPF": "84586107014",
        "phoneNumber": "11123456789",
        "dateOfBirth": "1971-08-16",
        "address": {
            "line1": "line1",
            "line2": "line 2",
            "city": "city 1",
            "state": "sp",
            "latitude": 547,
            "longitude": 899
        },
        "professionalInformation": {
            "profession": "profession 1",
            "companyName": "company 1",
            "position": "position 1"
        },
        "createdAt": "2018-09-20T04:40:23.368523Z"
    },
    {
        "id": 2,
        "name": "teste 2",
        "deion": "teste 2 - profession 2",
        "RG": "260204201",
        "CPF": "66819672055",
        "phoneNumber": "21987656787",
        "dateOfBirth": "1990-10-20",
        "address": {
            "line1": "rua xyz",
            "line2": "",
            "city": "city 2",
            "state": "sp",
            "latitude": 547,
            "longitude": 899
        },
        "professionalInformation": {
            "profession": "profession 2",
            "companyName": "company 2",
            "position": "position 2"
        },
        "createdAt": "2018-09-20T04:43:07.341223Z"
    },
    {
        "id": 3,
        "name": "teste 3",
        "deion": "teste 3 - profession 3",
        "RG": "275682717",
        "CPF": "69903923040",
        "phoneNumber": "21987656787",
        "dateOfBirth": "1999-05-01",
        "address": {
            "line1": "rua teste 3",
            "line2": "complemento",
            "city": "city 3",
            "state": "sp",
            "latitude": 123,
            "longitude": 321
        },
        "professionalInformation": {
            "profession": "profession 3",
            "companyName": "company 3",
            "position": "position 3"
        },
        "createdAt": "2018-09-20T04:44:32.032515Z"
    }
]
```

### Cadastrar um novo usuário:
Método POST
URL: 0.0.0.0:8000/users/
Content-Type: application/json

Requisição:
```
{
    "name": "teste 1",
    "RG": "178318966",
    "CPF": "84586107014",
    "phoneNumber": "11123456789",
    "dateOfBirth": "1971-08-16",
    "address": {
        "line1": "line1",
        "line2": "line 2",
        "city": "city 1",
        "state": "sp",
        "latitude": 547,
        "longitude": 899
    },
    "professionalInformation": {
        "profession": "profession 1",
        "companyName": "company 1",
        "position": "position 1"
    }
}
```

Resposta:
Status: 201 Created
```
{
    "id": 1,
    "name": "teste 1",
    "deion": "teste 1 - profession 1",
    "RG": "178318966",
    "CPF": "84586107014",
    "phoneNumber": "11123456789",
    "dateOfBirth": "1971-08-16",
    "address": {
        "line1": "line1",
        "line2": "line 2",
        "city": "city 1",
        "state": "sp",
        "latitude": 547,
        "longitude": 899
    },
    "professionalInformation": {
        "profession": "profession 1",
        "companyName": "company 1",
        "position": "position 1"
    },
    "createdAt": "2018-09-20T04:40:23.368523Z"
}
```

### Alterar dados de um usuário já cadastrado:
URL: 0.0.0.0:8000/users/1/
Método PUT
Content-Type: application/json

Requisição:
```
{
    "name": "alteracao 1",
    "RG": "178318966",
    "CPF": "84586107014",
    "phoneNumber": "11123456789",
    "dateOfBirth": "1971-08-16",
    "address": {
        "line1": "line1",
        "line2": "line 2",
        "city": "city 1",
        "state": "sp",
        "latitude": 547,
        "longitude": 899
    },
    "professionalInformation": {
        "profession": "profession alterado 1",
        "companyName": "company alterado 1",
        "position": "position alterado 1"
    }
}
```

Resposta:
Status: 200 OK
```
{
    "id": 1,
    "name": "alteracao 1",
    "deion": "alteracao 1 - profession alterado 1",
    "RG": "178318966",
    "CPF": "84586107014",
    "phoneNumber": "11123456789",
    "dateOfBirth": "1971-08-16",
    "address": {
        "line1": "line1",
        "line2": "line 2",
        "city": "city 1",
        "state": "sp",
        "latitude": 547,
        "longitude": 899
    },
    "professionalInformation": {
        "profession": "profession alterado 1",
        "companyName": "company alterado 1",
        "position": "position alterado 1"
    },
    "createdAt": "2018-09-20T04:40:23.368523Z"
}
```

### Deletar um usuário:
URL: 0.0.0.0:8000/users/1/
Método DELETE

Resposta:
Status: 204 No Content

### Listar um usuário especifico:
URL: 0.0.0.0:8000/users/1/
Método GET

Resposta:
Status: 200 OK

```
{
    "id": 1,
    "name": "alteracao 1",
    "deion": "alteracao 1 - profession alterado 1",
    "RG": "178318966",
    "CPF": "84586107014",
    "phoneNumber": "11123456789",
    "dateOfBirth": "1971-08-16",
    "address": {
        "line1": "line1",
        "line2": "line 2",
        "city": "city 1",
        "state": "sp",
        "latitude": 547,
        "longitude": 899
    },
    "professionalInformation": {
        "profession": "profession alterado 1",
        "companyName": "company alterado 1",
        "position": "position alterado 1"
    },
    "createdAt": "2018-09-20T04:40:23.368523Z"
}
```

### Pesquisar usuários cadastrados:
Pode ser pesquisado o contéudo de qualquer campo

URL: 0.0.0.0:8000/users?search=rua xyz
Método GET

Resposta:
Status: 200 OK

```
[
    {
        "id": 2,
        "name": "teste 2",
        "deion": "teste 2 - profession 2",
        "RG": "260204201",
        "CPF": "66819672055",
        "phoneNumber": "21987656787",
        "dateOfBirth": "1990-10-20",
        "address": {
            "line1": "rua xyz",
            "line2": "",
            "city": "city 2",
            "state": "sp",
            "latitude": 547,
            "longitude": 899
        },
        "professionalInformation": {
            "profession": "profession 2",
            "companyName": "company 2",
            "position": "position 2"
        },
        "createdAt": "2018-09-20T04:43:07.341223Z"
    }
]
```

### Gerar Token de autenticação:
URL: 0.0.0.0:8000/api-token-auth/
Método: POST
Content-Type: application/json

```
{
	"username": "admin",
	"password": "admin"
}
```

Para enviar requisições para criação e alteração de usuários usando autenticação é necessário adicionar "Authorization: Token [token_gerado]" nos headers da requisição. 

## Executando testes

Neste projeto foram implementados unit tests para os metodos de validação de CPF e RG. Para que os testes sejam executados enquanto a aplicação está sendo executada é possível interagir pelo terminal com o container da aplicação. Para isso pode ser usado o comando:
`docker exec -ti usersRestAPI01 /bin/bash`

Para executar os unit tests presentes no projeto deve ser executado o comando:
`python manage.py test`

Também é possível realizar os teste usando o coverage:
`coverage run --source='.' manage.py test`

E para ver um relatório dos resultados do coverage deve ser executado o comando:
`coverage report`

## Recursos utilizados

django - Framework web utilizado  

djangorestframework - Framework para REST API's usado juntamente com o django  

django_filter - Para pesquisas parametrizadas na url  

coverage - Para testes e relatórios  

django_redis - Para integração com o servidor Redis, utilizado para armazenamento de cache  

gunicorn - Servidor HTTP para python  

nginx - Servidor proxy HTTP  

PostgreSQL - Bancos de dados para persistência dos dados.  

