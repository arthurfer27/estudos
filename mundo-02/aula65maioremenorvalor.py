soma = maior = menor = cont = 0
continuar = "S"
while continuar in "Ss":
    num = int(input("Digite um número: "))
    soma += num
    cont += 1
    continuar = input("Quer continuar? [S/N]").strip().upper()[0]
    if cont == 1:
        maior = menor = num
    else:
        if num>maior:
            maior=num
        if num<menor:
            menor = num
print(f"Você digitou {cont} números e a média foi {soma/cont:.2f}.")
print(f"O maior valor foi {maior} e o menor valor foi {menor}.")
