# Mente Segura #

Mente Segura é um projeto Django que visa fornecer uma plataforma para promover a saúde mental e o bem-estar. Este projeto tem como objetivo oferecer recursos e ferramentas para ajudar os usuários a gerenciar o estresse, a ansiedade e outras questões de saúde mental.
Tecnologias Usadas

    Django: Framework web em Python para o desenvolvimento do backend.
    Python 3.x: Linguagem de programação utilizada no desenvolvimento.
    PostgreSQL: Banco de dados relacional para armazenar os dados do aplicativo.
    Celery: Sistema de filas de tarefas assíncronas para processamento em segundo plano (se aplicável).
    Docker: Plataforma de conteinerização para facilitar a implantação e o gerenciamento do aplicativo (opcional).
    HTML, CSS e JavaScript: Para o desenvolvimento do frontend.

Requisitos

Antes de começar, você precisará ter as seguintes ferramentas instaladas:

    Python 3.x
    PostgreSQL (ou outro banco de dados de sua preferência)
    pip (gerenciador de pacotes do Python)
    virtualenv ou venv (ambiente virtual Python, recomendado)
    Docker (Opcional)

Instalação

    Clone o repositório:
    Bash

git clone https://github.com/seu-usuario/mente_segura.git
cd mente_segura

Crie e ative um ambiente virtual:
Bash

python3 -m venv venv
source venv/bin/activate # No Linux/macOS
venv\Scripts\activate # No Windows

## Instale as dependências:
Bash

pip install -r requirements/base.txt
pip install -r requirements/local.txt

## Crie o banco de dados (PostgreSQL):

No terminal, entre no PostgreSQL:
Bash

psql -U postgres

Crie o banco de dados:
SQL

CREATE DATABASE nome_do_banco;

## Execute as migrações:
Bash

python manage.py migrate

## Crie um superusuário para acessar o painel de administração:
Bash

python manage.py createsuperuser

Inicie o servidor de desenvolvimento:
Bash

    python manage.py runserver

Agora você pode acessar o projeto no navegador em http://127.0.0.1:8000/.

    Acesse o painel de administração:

    Acesse http://127.0.0.1:8000/admin/.
    Faça login com o superusuário criado.

