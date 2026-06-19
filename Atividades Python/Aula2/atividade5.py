# Entrada das vendas
primeira_quinzena = int(input("Digite a quantidade de vendas primeira quinzena: "))
segunda_quinzena = int(input("Digite a quantidade da segunda quinzena: "))

#Cálculo de total 
total_vendas = primeira_quinzena + segunda_quinzena

#Verificação se atingiu exatamente 50 
print(total_vendas == 50)
