sexo = input("Informe seu sexo: ").strip().upper()[0]
while sexo not in "MF":
    if sexo != "m" or "f":
        sexo = input("Dados inválidos. Por favor, informe seu sexo: ").strip().upper()[0]
print(f"Sexo {sexo} registrado com sucesso.")