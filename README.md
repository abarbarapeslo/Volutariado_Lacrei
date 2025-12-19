<div align="center">
  <img src="https://img.icons8.com/color/96/000000/caduceus.png" width="100px" alt="Lacrei Saúde" />
  <h1>API de Gerenciamento de Consultas Médicas</h1>
  <p>API RESTful desenvolvida com Django + Django REST Framework para gerenciamento de profissionais da saúde e consultas médicas.</p>
</div>

<p align="center">
  <a href="https://github.com/abarbarapeslo/Volutariado_Lacrei/actions">
    <img alt="CI Status" src="https://github.com/abarbarapeslo/Volutariado_Lacrei/workflows/CI/badge.svg" />
  </a>
  <a href="https://github.com/abarbarapeslo/Volutariado_Lacrei/actions">
    <img alt="CD Status" src="https://github.com/abarbarapeslo/Volutariado_Lacrei/workflows/CD/badge.svg" />
  </a>
  <a href="https://github.com/abarbarapeslo/Volutariado_Lacrei">
    <img alt="Python" src="https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white" />
  </a>
  <a href="https://github.com/abarbarapeslo/Volutariado_Lacrei">
    <img alt="Django" src="https://img.shields.io/badge/Django-6.0-green?logo=django&logoColor=white" />
  </a>
  <a href="https://github.com/abarbarapeslo/Volutariado_Lacrei">
    <img alt="PostgreSQL" src="https://img.shields.io/badge/PostgreSQL-16-blue?logo=postgresql&logoColor=white" />
  </a>
  <a href="https://github.com/abarbarapeslo/Volutariado_Lacrei">
    <img alt="Docker" src="https://img.shields.io/badge/Docker-Ready-blue?logo=docker&logoColor=white" />
  </a>
</p>

<p align="center">
  <a href="http://18.188.58.173:8000/api/docs/">Ver Demo (Swagger)</a>
  ·
  <a href="#-deploy">Deploy</a>
  ·
  <a href="#-endpoints-da-api">Endpoints</a>
  ·
  <a href="#-setup-local">Setup Local</a>
  ·
  <a href="#-cicd">CI/CD</a>
</p>

---

## 🌐 Deploy

| Ambiente | URL |
|----------|-----|
| **API** | http://18.188.58.173:8000/api/ |
| **Swagger Docs** | http://18.188.58.173:8000/api/docs/ |
| **Admin** | http://18.188.58.173:8000/admin/ |

---

<details>
<summary><b>📋 Índice (Clique para expandir)</b></summary>

- [Critérios de Aceite](#-critérios-de-aceite)
- [Arquitetura](#-arquitetura)
- [Tecnologias](#-tecnologias)
- [Setup Local](#-setup-local)
- [Docker](#-docker)
- [Endpoints da API](#-endpoints-da-api)
- [Autenticação](#-autenticação)
- [Segurança](#-segurança)
- [Testes](#-testes)
- [CI/CD](#-cicd)
- [Deploy](#-deploy-1)
- [Rollback](#-rollback)
- [Proposta de Integração com Asaas](#-proposta-de-integração-com-asaas)
- [Decisões Técnicas](#-decisões-técnicas)

</details>

---

## 🏗️ Critérios de Aceite

| Item | Status | Observações |
|------|:------:|-------------|
| CRUD funcional de profissionais e consultas | ✅ | Incluindo busca por ID do profissional |
| Segurança (sanitização, CORS, autenticação) | ✅ | Proteção contra SQL Injection, API segura |
| Docker + PostgreSQL configurados | ✅ | Setup replicável para qualquer ambiente |
| Poetry (gerenciamento de dependências) | ✅ | pyproject.toml configurado |
| GitHub Actions (CI/CD) | ✅ | Lint, testes, build e deploy automatizados |
| Deploy funcional (AWS EC2 + RDS) | ✅ | Ambiente de produção |
| Testes unitários e de erro com APITestCase | ✅ | Cobertura dos endpoints principais |
| README completo + rollback | ✅ | Setup local, CI/CD, rollback e justificativas |
| Documentação da API (Swagger) | ✅ | Disponível em `/api/docs/` |
| Proposta de integração com Asaas | 🟨 | Documentada abaixo |

---

## 🏛️ Arquitetura

```
lacrei/
├── .github/
│   └── workflows/
│       ├── ci.yml              # Pipeline de CI (lint, testes)
│       └── cd.yml              # Pipeline de CD (build, deploy)
├── consultas/
│   ├── models.py               # Modelo Consulta
│   ├── serializers.py          # Serialização
│   ├── views.py                # ViewSet com filtro por profissional
│   └── teste/
│       └── test_consultas.py   # Testes de API
├── profissionais/
│   ├── models.py               # Modelo Profissional
│   ├── serializers.py          # Serialização
│   ├── views.py                # ViewSet CRUD
│   └── teste/
│       └── test_profissionais.py
├── voluntariado/
│   ├── settings.py             # Configurações Django
│   ├── urls.py                 # Rotas da API
│   └── permissoes.py           # Permissões customizadas
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml              # Poetry
└── manage.py
```

---

## 🛠️ Tecnologias

<table>
<tr>
<td>

| Backend | Versão |
|---------|--------|
| Python | 3.12 |
| Django | 6.0 |
| Django REST Framework | 3.16 |
| Simple JWT | 5.5 |

</td>
<td>

| Infraestrutura | Versão |
|----------------|--------|
| PostgreSQL | 16 |
| Docker | Latest |
| Gunicorn | 23.0 |
| AWS EC2 + RDS | - |

</td>
<td>

| DevOps | - |
|--------|---|
| Poetry | Dependências |
| GitHub Actions | CI/CD |
| drf-spectacular | Swagger |
| Flake8 | Lint |

</td>
</tr>
</table>

---

## 🚀 Setup Local

### Pré-requisitos

- Python 3.12+
- Poetry
- PostgreSQL 16+ (ou Docker)

### Instalação

```bash
# Clonar repositório
git clone https://github.com/abarbarapeslo/Volutariado_Lacrei.git
cd Volutariado_Lacrei

# Instalar dependências com Poetry
poetry install

# Configurar variáveis de ambiente
cp .env.example .env
# Editar .env com suas configurações

# Rodar migrações
poetry run python manage.py migrate

# Criar superusuário
poetry run python manage.py createsuperuser

# Iniciar servidor
poetry run python manage.py runserver
```

---

## 🐳 Docker

### Iniciar com Docker Compose

```bash
# Build e iniciar containers
docker-compose up --build

# Em outro terminal, rodar migrações
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

### Variáveis de Ambiente

| Variável | Descrição | Padrão |
|----------|-----------|--------|
| `DB_NAME` | Nome do banco | `voluntariado` |
| `DB_USER` | Usuário do banco | `postgres` |
| `DB_PASSWORD` | Senha do banco | - |
| `DB_HOST` | Host do banco | `localhost` |
| `DB_PORT` | Porta do banco | `5432` |
| `SECRET_KEY` | Chave secreta Django | - |
| `DEBUG` | Modo debug | `True` |
| `ALLOWED_HOSTS` | Hosts permitidos | `localhost,127.0.0.1` |

---

## 📡 Endpoints da API

### Profissionais

| Método | Endpoint | Descrição | Auth |
|:------:|----------|-----------|:----:|
| `GET` | `/api/profissionais/` | Listar todos | ❌ |
| `POST` | `/api/profissionais/` | Criar | ✅ |
| `GET` | `/api/profissionais/{id}/` | Buscar por ID | ❌ |
| `PUT` | `/api/profissionais/{id}/` | Atualizar | ✅ |
| `DELETE` | `/api/profissionais/{id}/` | Remover | ✅ |

### Consultas

| Método | Endpoint | Descrição | Auth |
|:------:|----------|-----------|:----:|
| `GET` | `/api/consultas/` | Listar todas | ❌ |
| `GET` | `/api/consultas/?profissional={id}` | Filtrar por profissional | ❌ |
| `POST` | `/api/consultas/` | Criar | ✅ |
| `GET` | `/api/consultas/{id}/` | Buscar por ID | ❌ |
| `DELETE` | `/api/consultas/{id}/` | Remover | ✅ |

### Documentação

| Endpoint | Descrição |
|----------|-----------|
| `/api/docs/` | Swagger UI |
| `/api/schema/` | OpenAPI Schema |

---

## 🔐 Autenticação

A API utiliza **JWT (JSON Web Token)** para autenticação.

### Obter Token

```bash
curl -X POST http://18.188.58.173:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "seu_usuario", "password": "sua_senha"}'
```

**Resposta:**
```json
{
  "refresh": "eyJ0eXAi...",
  "access": "eyJ0eXAi..."
}
```

### Usar Token

```bash
curl -X POST http://18.188.58.173:8000/api/profissionais/ \
  -H "Authorization: Bearer SEU_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"nome_social": "Maria", "profissao": "Médica", "endereco": "Rua A", "contato": "999999999"}'
```

| Configuração | Valor |
|--------------|-------|
| Access Token Lifetime | 30 minutos |
| Refresh Token Lifetime | 1 dia |

---

## 🛡️ Segurança

| Proteção | Implementação |
|----------|---------------|
| **SQL Injection** | ORM do Django com queries parametrizadas |
| **CORS** | `django-cors-headers` com origens explícitas |
| **Autenticação** | JWT com tokens de curta duração |
| **Permissões** | `IsAuthenticatedOrReadOnly` |
| **CSRF** | Middleware habilitado |
| **Secrets** | Variáveis de ambiente |
| **Container** | Usuário não-root no Docker |

---

## 🧪 Testes

### Executar Testes

```bash
# Local com Poetry
poetry run python manage.py test

# Com coverage
poetry run coverage run manage.py test
poetry run coverage report

# Docker
docker-compose exec web python manage.py test
```

### Cobertura

| Módulo | Testes |
|--------|--------|
| Profissionais | Listagem, criação autenticada/não autenticada, validação |
| Consultas | Listagem, criação, filtro por profissional, validação |

---

## ⚙️ CI/CD

### Pipeline

```
Push → Lint (flake8) → Testes → Build Docker → Deploy EC2
```

### CI (`.github/workflows/ci.yml`)

| Trigger | Jobs |
|---------|------|
| Push/PR para `master`, `develop` | Lint → Test → Build |

### CD (`.github/workflows/cd.yml`)

| Trigger | Ação |
|---------|------|
| Push para `master` | Build → Push ECR → Deploy EC2 |

---

## 🌐 Deploy

### Infraestrutura AWS

| Serviço | Uso |
|---------|-----|
| **EC2** | Instância t2.micro com Docker |
| **RDS** | PostgreSQL 17 |
| **ECR** | Container Registry |

### Deploy Manual

```bash
# SSH na EC2
ssh -i "key.pem" ec2-user@18.188.58.173

# Atualizar container
docker pull 290795853785.dkr.ecr.us-east-2.amazonaws.com/voluntariado-lacrei:latest
docker stop voluntariado && docker rm voluntariado
docker run -d -p 8000:8000 --name voluntariado \
  -e DB_HOST=... -e DB_PASSWORD=... \
  290795853785.dkr.ecr.us-east-2.amazonaws.com/voluntariado-lacrei:latest
```

---

## 🔄 Rollback

### Via Git

```bash
# Identificar commit anterior estável
git log --oneline

# Reverter para commit anterior
git revert HEAD
git push origin master
# CI/CD será acionado automaticamente
```

### Via Docker

```bash
# Listar imagens disponíveis no ECR
aws ecr list-images --repository-name voluntariado-lacrei

# Deploy de versão anterior
docker pull 290795853785.dkr.ecr.us-east-2.amazonaws.com/voluntariado-lacrei:<tag-anterior>
docker stop voluntariado && docker rm voluntariado
docker run -d -p 8000:8000 --name voluntariado \
  290795853785.dkr.ecr.us-east-2.amazonaws.com/voluntariado-lacrei:<tag-anterior>
```

---

## 💳 Proposta de Integração com Asaas

### Visão Geral

Integração com a API do [Asaas](https://www.asaas.com/) para gerenciamento de pagamentos de consultas.

### Fluxo Proposto

```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│ Paciente │ → │ Agendar  │ → │ Criar    │ → │ Webhook  │
│ agenda   │    │ Consulta │    │ Cobrança │    │ Confirma │
└──────────┘    └──────────┘    └──────────┘    └──────────┘
```

### Modelo de Dados Proposto

```python
class Pagamento(models.Model):
    consulta = models.OneToOneField(Consulta, on_delete=models.CASCADE)
    asaas_id = models.CharField(max_length=100, unique=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(choices=[
        ('PENDING', 'Pendente'),
        ('CONFIRMED', 'Confirmado'),
        ('RECEIVED', 'Recebido'),
    ])
```

### Endpoints Propostos

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `POST` | `/api/consultas/{id}/pagamento/` | Criar cobrança no Asaas |
| `GET` | `/api/consultas/{id}/pagamento/` | Status do pagamento |
| `POST` | `/api/webhooks/asaas/` | Receber notificações |

---

## 📝 Decisões Técnicas

| Decisão | Justificativa |
|---------|---------------|
| **Django REST Framework** | Framework maduro com serialização, autenticação e permissões |
| **JWT** | Stateless, escalável, ideal para APIs REST |
| **PostgreSQL** | Banco robusto para produção |
| **Poetry** | Gerenciamento moderno de dependências Python |
| **Gunicorn** | Servidor WSGI de produção, multi-worker |
| **Docker** | Ambiente replicável, facilita deploy |
| **GitHub Actions** | CI/CD integrado ao GitHub |
| **EC2 + RDS** | Infraestrutura AWS escalável |

---

## 👩‍💻 Desenvolvido por

<div align="center">
  <b>Bárbara Lopes</b>
  <br />
  <sub>Projeto desenvolvido como desafio técnico com foco em impacto social e boas práticas de engenharia de software.</sub>
</div>

---

<div align="center">
  <sub>Made with ❤️ and Python</sub>
</div>
