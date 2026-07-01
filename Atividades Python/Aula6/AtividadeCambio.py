import requests

#Entrada de dados
valor_reais = float(input("Digite o valor em Reais (R$): "))

# URL da API com multiplas moedas
url = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL"

# Requisição GET 
resposta = requests.get(url)

# Verificação de sucesso requisição
if resposta.status_code == 200:
    dados = resposta.json()

    #Extraindo as cotações de compra (bid)
    cotacao_usd = float(dados["USDBRL"]["bid"])
    cotacao_eur = float(dados["EURBRL"]["bid"])
    cotacao_btc = float(dados["BTCBRL"]["bid"])

    # Conversão inversa (Reais / Cotação)
    valor_usd = valor_reais / cotacao_usd
    valor_eur = valor_reais / cotacao_eur
    valor_btc = valor_reais / cotacao_btc


    # Exibição do painel 
    print("\n========== PAINEL MULTI-MOEDAS ============")
    print(f"Valor disponivel em Reais: R$ {valor_reais:.2f}\n")

    print("DÓLAR(USD)")
    print(f"Cotação: R$ {cotacao_usd:.2f}\n")
    print(f"Conversão: US$ {valor_usd:.2f}")


    print("EURO(EUR)")
    print(f"Cotação: R$ {cotacao_eur:.2f}\n")
    print(f"Conversão: € {valor_eur:.2f}")

    
    print("BITCON(BTC)")
    print(f"Cotação: R$ {cotacao_btc:.2f}\n")
    print(f"Conversão: BTC$ {valor_btc:.8f}")

    print("=" *40)
else:
    print(f"Erro na requisição! Status Code {resposta.status_code}")