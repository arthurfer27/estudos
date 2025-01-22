numeros = list()
while True:
    num = int(input("Digite um valor: "))
    if num not in numeros:
        numeros.append(num)
        print("Valor adicionado com sucesso!")
    elif num in numeros:
        print("Valor duplicado! Não vou adicionar...")
    continuar = input("Quer continuar? [S/N] ")[0]
    if continuar not in "sSnN":
        print("Opção inválida! Tente novamente.")
        continuar = input("Quer continuar? [S/N] ")[0]
    elif continuar == "n":
        break
numeros.sort()
print(f"Os valores digitados foram {numeros}.")