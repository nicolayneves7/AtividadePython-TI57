#Entrada da mensagem 
mensagem = input("Digite aqui sua mensagem: ")

# 1 - As duas primeiras letras
print ("1- Duas primeira letras: ", mensagem[:2])

# 2 - Uma sequencia de 5 letras no meio da frase 
meio = len(mensagem) // 2 

print("2- Cinco letras do meio:  ", mensagem[meio:meio+5])

# 3- Tres letras fora da sequencia

print("3- Letras fora de sequencia: ", mensagem [0] + mensagem [3] + mensagem[5])

# 4 - As quatros ultimas letras 
print("4- Quatro ultimas letras: ", mensagem[-4:])