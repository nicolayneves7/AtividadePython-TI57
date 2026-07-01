#Entrada da frase 

frase = input ("Digite uma frase em minusulo: ")

#Transformando em maiusculo
frase_maiuscula = frase.upper()

#Cortando na Letra A
corte = frase_maiuscula.split("A")

#Exibição dos resultados
print("Frase em maiusculo: ")
print("frase_maiuscula")

print("\nFrase cortada na letra A: ")
print(corte)