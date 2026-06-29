# Receba a pontuação do evento 
pontuacao = int(input("Digite a pontuação do alerta (1 a 10): "))


#Classifica o alerta 
if pontuacao >=1 and pontuacao <= 3:
    print("Alerta Baixo")
elif pontuacao >= 4 and pontuacao <= 7:
    print("Alerta medio")
elif pontuacao >=8 and pontuacao <= 10:
    print("Alerta Alto/Critico")
else:
    print("Pontuação inválida")