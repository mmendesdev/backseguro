# Mente Segura

Mente Segura é um projeto Django que tem como objetivo (descrever a finalidade do seu projeto). Este projeto visa (descrever os objetivos principais).

## Tecnologias Usadas 

- **Django** - Framework web em Python.
- **Python 3.x** - Linguagem utilizada no desenvolvimento.
- **PostgreSQL** - Banco de dados relacional.
- **Celery** - Gerenciamento de tarefas assíncronas (se aplicável).
- **Docker** (opcional) - Contêineres para facilitar o deploy.

## Requisitos

Antes de começar, você precisa ter as seguintes ferramentas instaladas:

- Python 3.x
- PostgreSQL (ou outro banco de dados, dependendo da sua configuração)
- pip (gerenciador de pacotes do Python)
- Virtualenv (opcional, mas recomendado para isolar o ambiente do seu projeto)

## Instalação

### 1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/mente_segura.git
cd mente_segura

2. Crie e ative um ambiente virtual:

python3 -m venv venv
source venv/bin/activate   # No Linux/Mac
venv\Scripts\activate      # No Windows

3. Instale as dependências:

pip install -r requirements/base.txt  
pip install -r requirements/local.txt  


5. Crie o banco de dados (se estiver usando PostgreSQL):

No terminal, entre no PostgreSQL:

psql -U postgres

Crie o banco de dados:

CREATE DATABASE nome_do_banco;

6. Execute as migrações:

python manage.py migrate

7. Crie um superusuário para acessar o painel de administração:

python manage.py createsuperuser

8. Inicie o servidor de desenvolvimento:

python manage.py runserver

Agora você pode acessar o projeto no navegador em http://127.0.0.1:8000/.
9. Acesse o painel de administração:

    Acesse http://127.0.0.1:8000/admin/.
    Faça login com o superusuário criado.




