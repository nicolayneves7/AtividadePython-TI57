# Leitura do valor da carga
valor_carga = float(input("Digite o valor da carga: R$ "))

# Verificação do desconto
if valor_carga <= 1000:
    desconto = 0
elif valor_carga <= 5000:
    desconto = valor_carga * 0.05
else:
    desconto = valor_carga * 0.10

# Cálculo do valor final
valor_final = valor_carga - desconto

# Exibição dos resultados
print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Valor final a pagar: R$ {valor_final:.2f}")