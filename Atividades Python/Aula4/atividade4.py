# Programa para verificar o estado civil (Apenas if, elif, else)

estado_civil = input("Digite seu estado civil: ")

# --- SOLTEIRO ---
if estado_civil == "solteiro":
    print("Você está solteiro(a).")
elif estado_civil == "Solteiro":
    print("Você está solteiro(a).")
elif estado_civil == "s":
    print("Você está solteiro(a).")
elif estado_civil == "S":
    print("Você está solteiro(a).")

# --- CASADO ---
elif estado_civil == "casado":
    print("Você está casado(a).")
elif estado_civil == "Casado":
    print("Você está casado(a).")
elif estado_civil == "c":
    print("Você está casado(a).")
elif estado_civil == "C":
    print("Você está casado(a).")

# --- DIVORCIADO ---
elif estado_civil == "divorciado":
    print("Você está divorciado(a).")
elif estado_civil == "Divorciado":
    print("Você está divorciado(a).")
elif estado_civil == "d":
    print("Você está divorciado(a).")
elif estado_civil == "D":
    print("Você está divorciado(a).")

# --- NOIVO ---
elif estado_civil == "noivo":
    print("Você está noivo(a).")
elif estado_civil == "Noivo":
    print("Você está noivo(a).")
elif estado_civil == "n":
    print("Você está noivo(a).")
elif estado_civil == "N":
    print("Você está noivo(a).")

# --- NAMORANDO ---
elif estado_civil == "namorando":
    print("Você está namorando.")
elif estado_civil == "Namorando":
    print("Você está namorando.")

# --- OUTROS ---
else:
    print("Estado civil classificado como outros.")