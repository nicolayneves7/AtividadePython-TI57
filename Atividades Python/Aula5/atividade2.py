#Receba a quantidade de vagas ocupadas 
vagas_ocupadas = int(input("Digite a quantidade de vagas ocupadas: "))

#Verifica a situação do estacionamento 
if vagas_ocupadas < 0  or vagas_ocupadas > 100:
    print("Erro: Quantidade invalida")
elif vagas_ocupadas == 0:
    print("Estacionamento Vazio")
elif vagas_ocupadas == 100:
    print("Estacionamento Lotado")
else: 
    print("Vagas Disponíveis")