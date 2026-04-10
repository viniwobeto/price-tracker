# 🔍 Price Tracker

Busca e compara preços de produtos no Google Shopping direto pelo terminal.

---

## 📦 Tecnologias

* Python 3.12
* [Requests](https://requests.readthedocs.io) — requisições HTTP
* [Rich](https://rich.readthedocs.io) — interface rica no terminal
* [SerpAPI](https://serpapi.com) — busca no Google Shopping
* [python-dotenv](https://pypi.org/project/python-dotenv/) — variáveis de ambiente

---

## ⚙️ Pré-requisitos

* Python 3.10+
* Conta gratuita no SerpAPI (necessária para obter a API Key)

---

## 🚀 Como rodar

### 1. Clone o repositório

```bash
git clone https://github.com/viniwobeto/price-tracker.git
cd price-tracker
```

---

### 2. Crie e ative o ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

### 4. Configure as variáveis de ambiente 🔑

Crie um arquivo `.env` na raiz do projeto com base no exemplo:

```bash
cp .env.example .env
```

Depois edite o arquivo `.env` e adicione sua chave da SerpAPI:

```
SERPAPI_KEY=sua_chave_aqui
```

👉 Para obter sua chave gratuitamente:

1. Acesse: https://serpapi.com/manage-api-key
2. Crie uma conta
3. Copie sua API Key

---

### 5. Execute o projeto

```bash
python3 tracker/cli.py
```

---

### 6. Busque um produto

```
Informe o produto: teclado mecânico redragon
```

---

## 📊 Exemplo de saída

```
Informe o produto: teclado mecanico redragon

                        Resultados
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┓
┃ Produto                       ┃ Preço  ┃ Loja             ┃ Link        ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━┩
│ Teclado Mecânico Redragon ... │ 189.99 │ Amazon.com.br    │ Ver produto │
│ Teclado Gamer Redragon ...    │ 179.99 │ KaBuM!           │ Ver produto │
└───────────────────────────────┴────────┴──────────────────┴─────────────┘
```

