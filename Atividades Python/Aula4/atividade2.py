# Recebe as duas notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Verifica se as notas estão dentro do intervalo válido
if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:

    # Calcula a média aritmética
    media = (nota1 + nota2) / 2

    # Exibe a média
    print(f"Média final: {media:.2f}")

    # Verifica se o aluno foi aprovado
    if media >= 6.0:
        print("Parabéns! Você foi aprovado(a).")
    else:
        print("Você está de recuperação. Estude um pouco mais!")

else:
    print("Erro: As notas devem estar entre 0 e 10.")