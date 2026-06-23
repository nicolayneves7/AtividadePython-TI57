#Qunatidade de vendas na primeira quinzena
primeira_quinzena = int(input("Digite a quantidade vendida na primeira quinzena: "))

#Entrada de vendas da segunda quinzena 
segunda_quinzena = int(input("Digite a quantidade vendida na segunda quinzena: "))

#Calculo do total de vendas 
total_vendas = primeira_quinzena + segunda_quinzena

#Exibição do total
print("Total de vendas no mes: ", total_vendas)
#Verificação da meta
if total_vendas == 100:
    print("Meta atingida exatamente!")
else: 
    print("Meta não foi atingida exatamente.")