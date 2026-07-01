import requests
 
# 1. Primeiro, pedimos o CEP para o usuário
cep = input("Digite o CEP (apenas números): ")
 
# 2. Agora, definimos a URL da API usando o CEP que o usuário digitou
url = f"https://viacep.com.br/ws/{cep}/json/"
 
# 3. Fazemos a requisição do tipo GET com a URL dinâmica
resposta = requests.get(url)
 
# 4. Verificamos se a requisição deu certo (Status Code 200 significa Sucesso)
if resposta.status_code == 200:
    # Tudo o que acontece se der certo ganha 4 espaços de recuo (uma tecla TAB)
    dados = resposta.json()
    print("Dados recebidos da API:")
    print(f"Logradouro: {dados['logradouro']}")
    print(f"Bairro: {dados['bairro']}")
    print(f"Cidade: {dados['localidade']}")
else:
    print(f"Erro ao acessar a API. Status: {resposta.status_code}")