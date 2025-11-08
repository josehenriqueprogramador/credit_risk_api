# Credit Risk API

## 🧠 1️⃣ O que é este sistema

Eu acabei de criar a **API de Previsão de Risco de Crédito**, um projeto Python/Django com:

* Backend **Django + Django REST Framework**
* Banco de dados **PostgreSQL**
* Modelo de Machine Learning usando **PyCaret**
* Comunicação via **API RESTful**
* Estrutura limpa e Dockerizada (ideal pra DevOps, CI/CD e cloud)

📈 A ideia:
Você envia dados de um cliente (renda, idade, histórico de crédito, etc.) e a API devolve uma **probabilidade de inadimplência (risco de calote)**, usando um modelo de ML.

---

## ⚙️ 2️⃣ Pré-requisitos

No **Termux** (ou em qualquer Linux), garanta que você tem:

\`\`\`bash
pkg install git python docker docker-compose -y
\`\`\`

👉 Se estiver em ambiente sem Docker, dá pra rodar com \`python manage.py runserver\` também.

---

## 🧩 3️⃣ Estrutura criada

Após rodar o comando, você tem:

\`\`\`
credit_risk_api/
├── app/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   ├── ml/
│   │   ├── train_model.py
│   │   ├── predict.py
│   └── tests/test_api.py
├── data/historico_clientes.parquet   # dataset usado para treinar o modelo
├── manage.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .env
\`\`\`

---

## 🧩 4️⃣ Configuração do Banco (PostgreSQL via Docker)

A stack já vem pronta no arquivo \`docker-compose.yml\`.

Inicie tudo com:

\`\`\`bash
docker-compose up --build
\`\`\`

Isso:

* sobe um container com **PostgreSQL**
* sobe outro com **Django**
* aplica as dependências
* roda o servidor em **[http://localhost:8000](http://localhost:8000)**

Se estiver em Termux com **Docker rodando via proot-distro** (ex: Ubuntu), o processo é igual.

---

## 🧮 5️⃣ Popular e treinar o modelo (PyCaret)

Antes de usar previsões, você precisa **treinar o modelo**.

1. Coloque um dataset \`historico_clientes.parquet\` dentro da pasta \`data/\`.

   * Esse arquivo deve conter colunas como:

     ```
     idade, renda_mensal, historico_credito, inadimplente
     25,3000,1,0
     45,8000,3,0
     32,2000,0,1
     ```
   * A última coluna (\`inadimplente\`) é o **alvo de treinamento**.

2. Treine o modelo:

\`\`\`bash
python app/ml/train_model.py
\`\`\`

Isso cria um arquivo \`app/ml/model.pkl\` com o modelo treinado.

---

## 🧠 6️⃣ Fazendo previsões (usando a API)

Com o servidor rodando (\`docker-compose up\` ou \`python manage.py runserver\`),
acesse via navegador ou com \`curl\`:

### 📤 Exemplo de requisição

\`\`\`bash
curl -X POST http://localhost:8000/api/avaliacoes/ \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "João",
    "idade": 35,
    "renda_mensal": 5000,
    "historico_credito": 2
  }'
\`\`\`

### 📥 Resposta esperada

\`\`\`json
{
  "cliente": "João",
  "probabilidade_inadimplencia": 0.27
}
\`\`\`

💡 Esse valor (0.27) vem do modelo treinado com PyCaret — representa a chance de inadimplência.

---

## 🧪 7️⃣ Testes automáticos

O projeto já vem com testes (usando \`pytest\` e \`DRF TestCase\`).

Rode:

\`\`\`bash
pytest
\`\`\`

Isso executa:

* Teste de endpoint \`/api/avaliacoes/\`
* Verifica se a API responde com o código 201
* Confirma se a previsão contém a chave \`probabilidade_inadimplencia\`

---

## 🧰 8️⃣ Personalização (Clean Code & DevOps)

* **Boas práticas aplicadas:**

  * Separação de camadas (Models, Views, Serializers, ML)
  * \`.env\` para variáveis sensíveis
  * Versionamento de dependências (\`requirements.txt\`)
  * \`docker-compose\` orquestrando tudo
  * Estrutura previsível e pronta para CI/CD
  * Testes e linting fáceis de integrar no pipeline

* **Para subir no GitHub:**

\`\`\`bash
git init
git add .
git commit -m "API de risco de crédito com Django + ML"
git branch -M main
git remote add origin https://github.com/seuuser/credit_risk_api.git
git push -u origin main
\`\`\`

---

## ☁️ 9️⃣ Deploy (opcional)

Pode subir no **Render, Railway, Fly.io, ou Google Cloud Run**.

Basta usar o Dockerfile — ele já está pronto para buildar:

\`\`\`bash
docker build -t credit_risk_api .
docker run -p 8000:8000 credit_risk_api
\`\`\`

---

## 🧭 10️⃣ Resumo dos Comandos-Chave

| Ação              | Comando                                                         |
| ----------------- | --------------------------------------------------------------- |
| Subir containers  | \`docker-compose up --build\`                                     |
| Rodar migrações   | \`docker exec -it creditrisk_web python manage.py migrate\`       |
| Treinar modelo ML | \`python app/ml/train_model.py\`                                  |
| Testar API        | \`pytest\`                                                        |
| Fazer previsão    | \`curl -X POST http://localhost:8000/api/avaliacoes/ -d '{...}'\` |
