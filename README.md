# API de Gerenciamento de Tarefas - ToDo List


## Descrição
Um projeto desenvolvido com FastAPI e gerenciado pelo Poetry, que fornece uma API para o gerenciamento de tarefas e usuários. A aplicação permite a criação, leitura, atualização e exclusão (CRUD) de tarefas, além de funcionalidades completas para a administração de usuários.

## Tecnologias
- Python: Linguagem principal do projeto
- FastAPI: Framework web para criação da API
- Poetry: Gerenciador de dependências e ambiente virtual
- Pytest: Framework para testes automatizados
- Pylint: Analisador de código para garantir boas práticas
- Uvicorn: Servidor ASGI para execução da aplicação
- Docker: Ferramenta para criação de containers
- PostgreSQL: Banco de dados relacional
- SQLAlchemy: ORM para interação com o banco de dados
- Alembic: Ferramenta para migração de banco de dados
- Pydantic: Biblioteca para validação de dados
- JWT (JSON Web Token): Biblioteca para autenticação de usuários

## Funcionalidades
- Autenticação de usuários via JWT
- CRUD de Tarefas: Criação, leitura, atualização e exclusão de tarefas
- Gerenciamento de Usuários: Criação e listagem de usuários
- Documentação interativa: A API oferece acesso à documentação via Swagger e Redoc.


## Aplicação
A aplicação está hospedada na plataforma Fly.io e pode ser acessada através deste [link](https://fast-zero-divine-water-3043.fly.dev/)


## Instalação

### Requisitos
- Python 3.7 ou superior
- Docker


Para instalar a aplicação, siga os passos abaixo:

1. Clone o repositório:
```bash
git clone https://github.com/juniors719/API_Gerenciamento_Tarefas_Python.git 
```

2. Acesse o diretório do projeto:
```bash
cd API_Gerenciamento_Tarefas_Python
```

3. Crie um arquivo `.env` usando o seguinte comando:
```bash
cp .env.example .env
```

4. Construa e inicie os containers com Docker Compose:
```bash
docker-compose -f compose.yml up --build
```



## Endpoints
A API oferece os seguintes endpoints:

#### Usuários
- POST /users/: Cria um novo usuário
- GET /users/: Lista todos os usuários
- GET /users/{user_id}: Obtém detalhes de um usuário específico
- PUT /users/{user_id}: Atualiza os dados de um usuário
- DELETE /users/{user_id}: Deleta um usuário
#### Autenticação
- POST /auth/token: Gera um token de acesso para autenticação
- POST /auth/refresh: Refresca o token de acesso
#### Tarefas (ToDos)
- POST /todos/: Cria uma nova tarefa
- GET /todos/: Lista todas as tarefas do usuário autenticado
- GET /todos/{todo_id}: Obtém os detalhes de uma tarefa
- PATCH /todos/{todo_id}: Atualiza os detalhes de uma tarefa
- DELETE /todos/{todo_id}: Deleta uma tarefa


## Documentação
- [Swagger](https://fast-zero-divine-water-3043.fly.dev/docs) 
- [Redoc](https://fast-zero-divine-water-3043.fly.dev/redoc)

## Licença
Este projeto está licenciado sob a GNU General Public License v3.0