# API de Gerenciamento de Consultas Médicas

API RESTful desenvolvida com **Django + Django REST Framework**, focada em boas práticas, segurança e pronta para ambiente de produção. Este projeto permite o gerenciamento de **profissionais da saúde** e **consultas médicas**, servindo como base para futuras integrações (pagamentos, deploy, monitoramento).

---

## Objetivo do Projeto

Desenvolver uma API funcional e segura para:

* Cadastro e gerenciamento de profissionais da saúde
* Agendamento e consulta de atendimentos médicos
* Autenticação segura via JWT
* Controle de permissões
* Retornos padronizados em JSON

---

```
OBS: 
- Optei por origens explícitas para evitar exposição indevida da API.
- Em ambiente de produção, *DEBUG* será desativado e os logs serão direcionados para serviços como CloudWatch
- Em ambiente Docker, o DB_HOST aponta para o nome do serviço (db).
- Em ambiente local sem Docker, o valor pode ser localhost.

```

## Arquitetura do Projeto

```
voluntariado/
├── profissionais/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│
├── consultas/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│
├── voluntariado/
│   ├── settings.py
│   ├── urls.py
│
└── manage.py
```

---

## Tecnologias Utilizadas

* Python 3
* Django
* Django REST Framework
* Simple JWT (Autenticação)
* SQLite (ambiente de desenvolvimento)
* Swagger / OpenAPI (documentação)

---

## Autenticação

A API utiliza **JWT (JSON Web Token)** para autenticação.

### Obter token

```http
POST /api/token/
```

```json
{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```

Resposta:

```json
{
  "refresh": "...",
  "access": "..."
}
```

Utilize o token de acesso no header das requisições protegidas:

```
Authorization: Bearer SEU_ACCESS_TOKEN
```

---

## Permissões

* **GET, HEAD, OPTIONS** → acesso público
* **POST, PUT, PATCH, DELETE** → apenas usuários autenticados

---

## 📌 Endpoints Principais

### sProfissionais

* `GET /api/profissionais/`
* `POST /api/profissionais/`
* `GET /api/profissionais/{id}/`
* `PUT /api/profissionais/{id}/`
* `DELETE /api/profissionais/{id}/`

### Consultas

* `GET /api/consultas/`
* `POST /api/consultas/`
* `GET /api/consultas/{id}/`
* `DELETE /api/consultas/{id}/`

🔎 Filtro por profissional:

```http
GET /api/consultas/?profissional=1
```

---

## Documentação da API

A documentação interativa está disponível via Swagger:

```http
GET /api/docs/
```

---

## Como Executar o Projeto

### 1️⃣ Clonar o repositório

```bash
git clone <url-do-repositorio>
cd voluntariado
```

### 2️⃣ Criar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Rodar migrações

```bash
python manage.py migrate
```

### 5️⃣ Criar superusuário

```bash
python manage.py createsuperuser
```

### 6️⃣ Executar servidor

```bash
python manage.py runserver
```

---

## Status do Projeto

* [x] CRUD Profissionais
* [x] CRUD Consultas
* [x] Filtro por profissional
* [x] Autenticação JWT
* [x] Permissões
* [x] Documentação Swagger

---

## Desenvolvido por Bárbara Lopes

Projeto desenvolvido como desafio técnico com foco em impacto social e boas práticas de engenharia de software.
