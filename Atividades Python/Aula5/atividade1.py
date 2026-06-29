#Programa que simula o sensor de uma lixeira inteligente 

# Solicita ao usuario o tipo de máterial descartado 

material = input("Digite o material descartado (Plástico, Papel Metal, ou Vidro): ")

#Converte o texto para minúsculo para facilitar a comparação 
material = material.lower()

#Verificar o tipo de material e mostra a cor da lixeira correta 

if material == "plástico" or material == "plastico": 
        print("Lixeira Vermelha")
elif material =="papel": 
        print("Lixeira Amarela")
elif material == "vidro":
        print("Lixeiro Verde") 
#Caso não seja nenhum dos materias recicláveis 
else: 
        print("Lixo Orgânico/Não Reciclável - Lixeira Cinza")       