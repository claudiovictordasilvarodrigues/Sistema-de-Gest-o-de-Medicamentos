# 💊 Sistema de Gerenciamento de Medicamentos

API desenvolvida para gerenciar medicamentos, permitindo cadastro, controle de estoque e organização de informações essenciais.

## 🚀 Tecnologias

* Python 3
* FastAPI
* Uvicorn
* Banco de dados (a definir: PostgreSQL, SQLite, etc.)

## 📁 Estrutura do Projeto

```
.
├── app/
│   ├── main.py
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── schemas/
│   └── services/
├── venv/
├── requirements.txt
└── README.md
```

## ⚙️ Configuração do Ambiente

### 1. Criar ambiente virtual

```bash
python3 -m venv venv
```

### 2. Ativar o ambiente

```bash
source venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

## ▶️ Executando o Projeto

```bash
uvicorn app.main:app --reload
```

Acesse em: http://127.0.0.1:8000

Documentação automática:

* Swagger: http://127.0.0.1:8000/docs
* Redoc: http://127.0.0.1:8000/redoc

## 🗄️ Banco de Dados

Configuração inicial do banco já estruturada no projeto.

> Detalhes adicionais serão documentados conforme evolução.

## 📌 Funcionalidades (planejadas)

* Cadastro de medicamentos
* Controle de estoque
* Atualização de informações
* Exclusão de registros
* Alertas de vencimento (futuro)

## 📄 Status do Projeto

🚧 Em desenvolvimento inicial

## 👨‍💻 Autor

Desenvolvido por [Seu Nome]
