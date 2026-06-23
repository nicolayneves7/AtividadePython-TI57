#Solicita um número inteiro ao usuario 
numero = int(input("Digite um número inteiro: "))

#Realiza a divisão inteira por 2
resultado = numero // 2 

#Verifica se o número é par ou impar 
if numero % 2 == 0:
    print("O numero é PAR")
else:
    print("O número é IMPAR")

#Exibe o resultado da divisão inteira 
print ("Resultado da divisão inteira por 2:", resultado)    