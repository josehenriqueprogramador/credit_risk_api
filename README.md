# 💳 Credit Risk API

[![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-REST_Framework-092E20?logo=django)](https://www.django-rest-framework.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue?logo=docker)](https://www.docker.com/)
[![License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)

---

## 🧠 Visão Geral
**Credit Risk API** é uma aplicação **Django REST + Machine Learning (PyCaret)** que prevê o **risco de inadimplência** de um cliente com base em informações financeiras.  
Você envia dados como idade, renda e histórico de crédito — e recebe de volta uma **probabilidade de calote** estimada por um modelo de aprendizado de máquina.

---

## ⚙️ Tecnologias Principais
| Camada | Tecnologia |
|---------|-------------|
| Backend | Django + Django REST Framework |
| Banco de Dados | PostgreSQL |
| Machine Learning | PyCaret |
| Deploy / Infra | Docker & Docker Compose |
| Testes | Pytest + DRF TestCase |

---

## 🚀 Como Executar

### 🐳 Com Docker
docker-compose up --build

Isso sobe os containers do **PostgreSQL** e **Django** e roda a API em [http://localhost:8000](http://localhost:8000).

### 💻 Sem Docker
python manage.py runserver

---

## 🤖 Treinar o Modelo (PyCaret)
Antes de prever, você precisa treinar o modelo com dados históricos.  
O dataset deve estar em `data/historico_clientes.parquet`.

| idade | renda_mensal | historico_credito | inadimplente |
|:------|:--------------|:------------------|:--------------|
| 25 | 3000 | 1 | 0 |
| 45 | 8000 | 3 | 0 |
| 32 | 2000 | 0 | 1 |

Treine o modelo com:
python app/ml/train_model.py

Isso gera `app/ml/model.pkl`, usado nas previsões.

---

## 📡 Fazendo Previsões
Com o servidor rodando, envie:
curl -X POST http://localhost:8000/api/avaliacoes/ -H "Content-Type: application/json" -d '{"nome":"João","idade":35,"renda_mensal":5000,"historico_credito":2}'

### 🧾 Resposta esperada
{
  "cliente": "João",
  "probabilidade_inadimplencia": 0.27
}

> 🔢 O valor indica a probabilidade de inadimplência (ex: 27%).

---

## 🧪 Testes Automatizados
pytest  
Valida o endpoint `/api/avaliacoes/`, código 201 e a presença da chave `probabilidade_inadimplencia`.

---

## ☁️ Deploy
Compatível com:
- Render
- Railway
- Fly.io
- Google Cloud Run

Build manual:
docker build -t credit_risk_api .
docker run -p 8000:8000 credit_risk_api

---

## 🧭 Comandos Rápidos
| Ação | Comando |
|------|----------|
| 🚀 Subir containers | docker-compose up --build |
| ⚙️ Rodar migrações | docker exec -it creditrisk_web python manage.py migrate |
| 🧠 Treinar modelo | python app/ml/train_model.py |
| 🧪 Rodar testes | pytest |
| 🔍 Fazer previsão | curl -X POST http://localhost:8000/api/avaliacoes/ -d '{...}' |

---

## 👨‍💻 Autor
**José Henrique Jardim**  
📦 Projeto: *Credit Risk API — Django + PyCaret*  
🧾 Licença: MIT License
