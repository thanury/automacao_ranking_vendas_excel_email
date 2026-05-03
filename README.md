# 🏆 Automação de Ranking de Vendas

Este projeto automatiza a leitura de planilhas de vendas de diversas lojas, calcula o faturamento total de cada uma, gera um ranking e envia o resultado por e-mail para a diretoria.

## 🚀 Funcionalidades

- Leitura de arquivos Excel (`.xlsx`) de várias lojas
- Cálculo do faturamento total por loja
- Geração de ranking ordenado do maior para o menor faturamento
- Formatação dos valores em moeda brasileira (R$)
- Envio automático do ranking por e-mail via yagmail

## 📋 Pré-requisitos

- Python 3.11+
- Pip (gerenciador de pacotes do Python)

## 🔧 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/automacao_ranking_vendas_excel_email.git
cd automacao_ranking_vendas_excel_email
```

2. Crie e ative um ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# ou
venv\Scripts\activate  # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Configure o arquivo `.env` com suas credenciais de e-mail:

```env
login=seu_email@gmail.com
senha_app=sua_senha_de_app
```

> ⚠️ **Importante:** Use uma senha de app do Gmail. Ative a verificação em duas etapas e gere uma senha de app em: https://myaccount.google.com/apppasswords

## 🧠 Como usar

Coloque os arquivos Excel das lojas na raiz do projeto com o seguinte padrão de nome:

```
Loja BH.xlsx
Loja DF.xlsx
Loja Manaus.xlsx
Loja Rio.xlsx
Loja Salvador.xlsx
Loja SP.xlsx
```

Cada planilha deve conter uma coluna chamada **Vendas** com os valores a serem somados.

Depois, execute:

```bash
python app.py
```

## 📁 Estrutura do projeto

```
📁 automacao_ranking_vendas_excel_email/
├── app.py               # Script principal
├── .env                 # Credenciais de e-mail (não versionado)
├── requirements.txt     # Dependências do projeto
├── README.md            # Documentação
└── Loja *.xlsx          # Planilhas de vendas
```

## 🛠️ Dependências

- [pandas](https://pandas.pydata.org/) — Leitura e manipulação dos dados
- [yagmail](https://github.com/kootenpv/yagmail) — Envio de e-mails
- [python-dotenv](https://github.com/theskumar/python-dotenv) — Gerenciamento de variáveis de ambiente
