# API de Gerenciamento de Consultas Médicas

API RESTful desenvolvida com **Django + Django REST Framework**, focada em boas práticas, segurança e pronta para ambiente de produção. Este projeto permite o gerenciamento de **profissionais da saúde** e **consultas médicas**.

## 🌐 Deploy

- **API (Produção):** http://18.188.58.173:8000/api/
- **Swagger Docs:** http://18.188.58.173:8000/api/docs/
- **Admin:** http://18.188.58.173:8000/admin/

---

## 🏗️ Critérios de Aceite

| Item | Status | Observações |
|------|--------|-------------|
| CRUD funcional de profissionais e consultas | ✅ | Incluindo busca por ID do profissional |
| Segurança (sanitização, CORS, autenticação) | ✅ | Proteção contra SQL Injection, API segura |
| Docker + PostgreSQL configurados | ✅ | Setup replicável para qualquer ambiente |
| GitHub Actions (CI/CD) | ✅ | Build, testes e deploy automatizados |
| Deploy funcional (staging e produção) | ✅ | Na AWS ou serviço equivalente |
| Testes unitários e de erro com APITestCase | ✅ | Cobertura dos endpoints principais |
| README completo + rollback | ✅ | Setup local, CI/CD, rollback e justificativas |
| Documentação da API (Swagger) | ✅ | Disponível em `/api/docs/` |
| Proposta de integração com Asaas | 🟨 | Documentada abaixo |

---

## 📋 Índice

- [Arquitetura](#-arquitetura)
- [Tecnologias](#-tecnologias)
- [Setup Local](#-setup-local)
- [Docker](#-docker)
- [Endpoints da API](#-endpoints-da-api)
- [Autenticação](#-autenticação)
- [Segurança](#-segurança)
- [Testes](#-testes)
- [CI/CD](#-cicd)
- [Deploy](#-deploy)
- [Rollback](#-rollback)
- [Proposta de Integração com Asaas](#-proposta-de-integração-com-asaas)
- [Decisões Técnicas](#-decisões-técnicas)

---

## 🏛️ Arquitetura

```
lacrei/
├── .github/
│   └── workflows/
│       ├── ci.yml              # Pipeline de CI (testes, lint)
│       └── cd.yml              # Pipeline de CD (build, push Docker)
├── consultas/
│   ├── models.py               # Modelo Consulta
│   ├── serializers.py          # Serialização de consultas
│   ├── views.py                # ViewSet com filtro por profissional
│   └── teste/
│       └── test_consultas.py   # Testes de API
├── profissionais/
│   ├── models.py               # Modelo Profissional
│   ├── serializers.py          # Serialização de profissionais
│   ├── views.py                # ViewSet CRUD
│   └── teste/
│       └── test_profissionais.py
├── voluntariado/
│   ├── settings.py             # Configurações Django
│   ├── urls.py                 # Rotas da API
│   └── permissoes.py           # Permissões customizadas
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── manage.py
```

---

## 🛠️ Tecnologias

| Tecnologia | Versão | Finalidade |
|------------|--------|------------|
| Python | 3.12 | Linguagem principal |
| Django | 6.0 | Framework web |
| Django REST Framework | 3.16 | API RESTful |
| Simple JWT | 5.5 | Autenticação JWT |
| PostgreSQL | 16 | Banco de dados |
| Docker | - | Containerização |
| Gunicorn | 23.0 | Servidor WSGI de produção |
| drf-spectacular | 0.29 | Documentação OpenAPI/Swagger |
| GitHub Actions | - | CI/CD |

---

## 🚀 Setup Local

### Pré-requisitos

- Python 3.12+
- PostgreSQL 16+ (ou Docker)

### Instalação

```bash
# Clonar repositório
git clone https://github.com/abarbarapeslo/Volutariado_Lacrei.git
cd Volutariado_Lacrei

# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Configurar variáveis de ambiente
cp .env.example .env
# Editar .env com suas configurações

# Rodar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Iniciar servidor
python manage.py runserver
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
| `DB_PASSWORD` | Senha do banco | `postgres` |
| `DB_HOST` | Host do banco | `localhost` / `db` (Docker) |
| `DB_PORT` | Porta do banco | `5432` |
| `SECRET_KEY` | Chave secreta Django | - |
| `DEBUG` | Modo debug | `True` |
| `ALLOWED_HOSTS` | Hosts permitidos | `localhost,127.0.0.1` |

---

## 📡 Endpoints da API

### Profissionais

| Método | Endpoint | Descrição | Autenticação |
|--------|----------|-----------|--------------|
| `GET` | `/api/profissionais/` | Listar todos | Não |
| `POST` | `/api/profissionais/` | Criar profissional | Sim |
| `GET` | `/api/profissionais/{id}/` | Buscar por ID | Não |
| `PUT` | `/api/profissionais/{id}/` | Atualizar | Sim |
| `PATCH` | `/api/profissionais/{id}/` | Atualização parcial | Sim |
| `DELETE` | `/api/profissionais/{id}/` | Remover | Sim |

### Consultas

| Método | Endpoint | Descrição | Autenticação |
|--------|----------|-----------|--------------|
| `GET` | `/api/consultas/` | Listar todas | Não |
| `GET` | `/api/consultas/?profissional={id}` | Filtrar por profissional | Não |
| `POST` | `/api/consultas/` | Criar consulta | Sim |
| `GET` | `/api/consultas/{id}/` | Buscar por ID | Não |
| `DELETE` | `/api/consultas/{id}/` | Remover | Sim |

### Documentação

- **Swagger UI:** `GET /api/docs/`
- **OpenAPI Schema:** `GET /api/schema/`

---

## 🔐 Autenticação

A API utiliza **JWT (JSON Web Token)** para autenticação.

### Obter Token

```bash
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "seu_usuario", "password": "sua_senha"}'
```

**Resposta:**
```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### Usar Token

```bash
curl -X POST http://localhost:8000/api/profissionais/ \
  -H "Authorization: Bearer SEU_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"nome_social": "Maria", "profissao": "Médica", "endereco": "...", "contato": "..."}'
```

### Refresh Token

```bash
curl -X POST http://localhost:8000/api/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{"refresh": "SEU_REFRESH_TOKEN"}'
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
| **Permissões** | `IsAuthenticatedOrReadOnly` - leitura pública, escrita autenticada |
| **CSRF** | Middleware habilitado |
| **Secrets** | Variáveis de ambiente (não commitadas) |
| **Usuário não-root** | Container Docker roda com usuário `appuser` |

### CORS Configurado

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
```

---

## 🧪 Testes

### Executar Testes

```bash
# Local
python manage.py test

# Docker
docker-compose exec web python manage.py test
```

### Cobertura de Testes

| Módulo | Testes |
|--------|--------|
| Profissionais | Listagem, criação autenticada/não autenticada, validação |
| Consultas | Listagem, criação, filtro por profissional, validação |

### Estrutura de Testes

```python
class ProfissionalAPITestCase(APITestCase):
    def test_list_profissionais(self)              # GET público
    def test_create_profissional_authenticated(self)   # POST autenticado
    def test_create_profissional_unauthenticated(self) # POST bloqueado
    def test_create_profissional_invalid_data(self)    # Validação
```

---

## ⚙️ CI/CD

### Pipeline de CI (`.github/workflows/ci.yml`)

Executado em: **push/PR para `main` e `develop`**

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Checkout  │ → │  Setup      │ → │   Lint      │ → │   Testes    │
│             │    │  Python 3.12│    │  (flake8)   │    │  (pytest)   │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

### Pipeline de CD (`.github/workflows/cd.yml`)

Executado em: **push para `main`** ou **tags `v*`**

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Checkout  │ → │ Build Image │ → │ Push to     │
│             │    │  Docker     │    │ GHCR        │
└─────────────┘    └─────────────┘    └─────────────┘
```

**Imagem publicada em:** `ghcr.io/abarbarapeslo/volutariado_lacrei`

---

## 🌐 Deploy

### Estratégia de Deploy

| Ambiente | Branch | Trigger |
|----------|--------|---------|
| Staging | `develop` | Push automático |
| Produção | `main` | Push ou tag `v*` |

### Deploy na AWS (Exemplo com ECS)

```bash
# 1. Fazer login no ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.us-east-1.amazonaws.com

# 2. Tag da imagem
docker tag ghcr.io/abarbarapeslo/volutariado_lacrei:main <aws_account_id>.dkr.ecr.us-east-1.amazonaws.com/voluntariado:latest

# 3. Push para ECR
docker push <aws_account_id>.dkr.ecr.us-east-1.amazonaws.com/voluntariado:latest

# 4. Atualizar serviço ECS
aws ecs update-service --cluster voluntariado-cluster --service voluntariado-service --force-new-deployment
```

### Variáveis de Ambiente em Produção

```bash
SECRET_KEY=<chave-segura-gerada>
DEBUG=False
ALLOWED_HOSTS=api.seudominio.com
DB_HOST=<rds-endpoint>
```

---

## 🔄 Rollback

### Rollback via Git

```bash
# Identificar commit anterior estável
git log --oneline

# Reverter para commit anterior
git revert HEAD
git push origin main
# CI/CD será acionado automaticamente
```

### Rollback via Docker

```bash
# Listar tags disponíveis
docker images ghcr.io/abarbarapeslo/volutariado_lacrei

# Fazer deploy de versão anterior
docker-compose down
docker-compose up -d --no-build ghcr.io/abarbarapeslo/volutariado_lacrei:<tag-anterior>
```

### Rollback na AWS ECS

```bash
# Listar task definitions
aws ecs list-task-definitions --family-prefix voluntariado

# Atualizar serviço para revisão anterior
aws ecs update-service \
  --cluster voluntariado-cluster \
  --service voluntariado-service \
  --task-definition voluntariado:<revisao-anterior>
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
        ('REFUNDED', 'Reembolsado'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
```

### Endpoints Propostos

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `POST` | `/api/consultas/{id}/pagamento/` | Criar cobrança no Asaas |
| `GET` | `/api/consultas/{id}/pagamento/` | Status do pagamento |
| `POST` | `/api/webhooks/asaas/` | Receber notificações do Asaas |

### Exemplo de Integração

```python
import requests

class AsaasService:
    BASE_URL = "https://api.asaas.com/v3"
    
    def __init__(self):
        self.headers = {
            "access_token": os.getenv("ASAAS_API_KEY")
        }
    
    def criar_cobranca(self, consulta, valor):
        payload = {
            "customer": consulta.paciente.asaas_id,
            "billingType": "PIX",
            "value": float(valor),
            "dueDate": consulta.data.strftime("%Y-%m-%d"),
            "description": f"Consulta com {consulta.profissional.nome_social}"
        }
        response = requests.post(
            f"{self.BASE_URL}/payments",
            json=payload,
            headers=self.headers
        )
        return response.json()
```

---

## 📝 Decisões Técnicas

| Decisão | Justificativa |
|---------|---------------|
| **Django REST Framework** | Framework maduro com serialização, autenticação e permissões prontas |
| **JWT** | Stateless, escalável, ideal para APIs REST |
| **PostgreSQL** | Banco robusto para produção, suporte a JSON e full-text search |
| **Gunicorn** | Servidor WSGI de produção, multi-worker |
| **Docker** | Ambiente replicável, facilita deploy e CI/CD |
| **GitHub Actions** | Integração nativa com GitHub, gratuito para repos públicos |
| **CORS explícito** | Segurança: evita exposição indevida da API |
| **Variáveis de ambiente** | Secrets não commitados, configuração por ambiente |

---

## 👩‍💻 Desenvolvido por

**Bárbara Lopes**

Projeto desenvolvido como desafio técnico com foco em impacto social e boas práticas de engenharia de software.

---

## 📄 Licença

Este projeto está sob a licença MIT.
