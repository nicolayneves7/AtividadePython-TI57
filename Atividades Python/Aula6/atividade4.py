#Importando a biblioteca de matematica
import math 

#Solitica o raio da esfera
raio = float(float("Digite o raio de esfera em centímetros: "))

#Calculo o volume da esfera 
volume = (4/3) * math.pi * (raio ** 3)

#Exibe o resultando formatado com duas casas decimais
print(f"O volume da esfera é:{volume:.2f} cm³") 