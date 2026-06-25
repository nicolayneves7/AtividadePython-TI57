# Programa para calcular desconto em uma compra

#Entrada para o valor da compra 
valor_compra = float(input("Digite o valor total da compra: R$ "))

#Verifica se há desconto
if valor_compra > 150:
    desconto = valor_compra * 0.10 #10% de desconto??
    valor_final = valor_compra - desconto 
else: 
    valor_final = valor_compra 

#Exibe o valor final da compra
print(f"Valor final a pagar: R$ {valor_final:.2f}")