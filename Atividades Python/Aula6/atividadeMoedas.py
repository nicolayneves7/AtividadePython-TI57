# Importa a requisição
import requests

#Entrada de dados
moeda = input("Digite a sigla da moeda estrangeira (ex: USD, EUR, BTC): ").upper()
quantidade = float(input("Digite a qauntidade que deseja converter: "))

#URL da API 
url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

#Requisições GET 
resposta = requests.get(url)

#Verifica se a resposta foi bem-sucedida
if resposta.status_code == 200:
    dados = resposta.json()
    #Nome da chave retornada pela API
    chave =f"{moeda}BRL"
    #Verifica se a moeda existe no retorno
    if chave in dados:
        #Obtem o valor de compra(bid)
        cotacao = float(dados[chave]["bid"])
        #Calcula o valor convertido 
        total_reais = quantidade * cotacao 

        #Exibe o resultado
        print(f"\nCotação atual do {moeda}: R$ {cotacao:.2f}")
        print(f"Valor convertido: R$ {total_reais:.2f}")
    else:
        print("Erro: moeda não encontrada ou invalida.")
else:
    print("Erro ao acessar a API. Tente novamente mais tarde.")