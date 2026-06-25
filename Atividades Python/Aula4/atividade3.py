#Solicita ao usuário a velocidade do carro
velocidade = float(input("Digite a velocidade do carro (km/h): "))

#Verifica se a velocidade ultrapassou o limite permitido
if velocidade > 80:
    #Calcula o valor da multa
    multa = (velocidade - 80) * 7

    #Exibe a mensagem de multa
    print("Voce foi multado!")

    #Mostra o valor da multa formatado com 2 casas decimais
    print(f"Valor da multa:R$ {multa:.2f}")

    #Caso a velocidade esteaj dentro do limite
else: 
    print("Boa viagem! Dirija com segurança.")