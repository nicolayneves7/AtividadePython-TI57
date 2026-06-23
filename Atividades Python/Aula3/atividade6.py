#Solicita os dados do usuario
ano_atual = int(input("Digite o ano atual: "))
ano_nascimento = int (input("Digite o ano do seu nascimento: "))

#Calcula a idade
idade = ano_atual - ano_nascimento

# Verifica se é maior de idade 
if idade >= 18:
    print("Acesso liberado. Voce é maior de idade")
else: print("Acesso negado. Entrada permitida apenas para maiores de idade")