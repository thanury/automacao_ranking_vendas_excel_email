# Passo a passo do projeto
# Passo 1: Pegar cada base de dados
# Passo 2: Para cada base de dados
    # calcular faturamento total (somar todos os valores da coluna de vendas)
# Criar um rank com o faturamento total de todas as lojas
# Enviar um email com esse ranking para a diretoria

import pandas as pd
import yagmail
import os
from dotenv import load_dotenv

lista_cidades = ["BH", "DF", "Manaus", "Rio", "Salvador", "SP"]

faturamentos = {}

for cidade in lista_cidades:    
    # df = dataframe = tabela no excel
    vendas_df = pd.read_excel(f"Loja {cidade}.xlsx")
    faturamento_cidade = sum(vendas_df["Vendas"])
    faturamentos[cidade] = faturamento_cidade

ranking_df = pd.DataFrame.from_dict(faturamentos, orient="index", columns=["Vendas"])
ranking_df = ranking_df.sort_values(by="Vendas", ascending=False)
ranking_df = ranking_df.map("R${:,.2f}".format)

mensagem_email = f"""
Prezados,
Segue em anexo o ranking de vendas das lojas.

Ranking:
{ranking_df.to_string().replace(" ", "-")}

Qualquer dúvida, estou a disposição.
Atensionamente,
Thanury
"""

load_dotenv() # carrega as variáveis do .env
login = os.getenv("login") # pega o valor de login
senha_app = os.getenv("senha_app") # pega o valor de senha_app

usuario = yagmail.SMTP(login, senha_app)
usuario.send(
    to="meh.lucas@gmail.com",
    subject="Ranking das lojas",
    contents=mensagem_email
)
print("Email enviado!")