import requests

# Entrada de dados
valor_reais = float(input("Digite o valor em Reais (R$): "))

# URL da API com múltiplas moedas
url = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL,GBP-BRL,JPY-BRL,ARS-BRL"

# Requisição GET
resposta = requests.get(url)

# Verificação da requisição
if resposta.status_code == 200:

    dados = resposta.json()

    # Extraindo as cotações (bid)
    usd = float(dados["USDBRL"]["bid"])
    eur = float(dados["EURBRL"]["bid"])
    btc = float(dados["BTCBRL"]["bid"])
    gbp = float(dados["GBPBRL"]["bid"])
    jpy = float(dados["JPYBRL"]["bid"])
    ars = float(dados["ARSBRL"]["bid"])

    # Conversões
    convertido_usd = valor_reais / usd
    convertido_eur = valor_reais / eur
    convertido_btc = valor_reais / btc
    convertido_gbp = valor_reais / gbp
    convertido_jpy = valor_reais / jpy
    convertido_ars = valor_reais / ars

    # Painel de saída
    print("\n" + "=" * 55)
    print("      PAINEL MULTI-MOEDAS DE CÂMBIO")
    print("=" * 55)

    print(f"\nDólar (USD)")
    print(f"Cotação: R$ {usd:.2f}")
    print(f"Conversão: US$ {convertido_usd:.2f}")

    print(f"\nEuro (EUR)")
    print(f"Cotação: R$ {eur:.2f}")
    print(f"Conversão: € {convertido_eur:.2f}")

    print(f"\nBitcoin (BTC)")
    print(f"Cotação: R$ {btc:.2f}")
    print(f"Conversão: BTC {convertido_btc:.8f}")

    print(f"\nLibra Esterlina (GBP)")
    print(f"Cotação: R$ {gbp:.2f}")
    print(f"Conversão: £ {convertido_gbp:.2f}")

    print(f"\nIene Japonês (JPY)")
    print(f"Cotação: R$ {jpy:.2f}")
    print(f"Conversão: ¥ {convertido_jpy:.2f}")

    print(f"\nPeso Argentino (ARS)")
    print(f"Cotação: R$ {ars:.2f}")
    print(f"Conversão: ARS {convertido_ars:.2f}")

    print("\n" + "=" * 55)

else:
    print("Erro ao acessar a API.")
