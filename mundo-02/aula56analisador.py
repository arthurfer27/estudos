media_idade = 0
cont_mulher = 0
maior=0
nomevelho=""
for d in range(1, 5):
    print(f"-----{d}ª PESSOA-----")
    nome = input("Nome: ").strip().title()
    idade = int(input("Idade: "))
    media_idade += idade
    media = (media_idade/4)
    sexo = str(input("Sexo [M/F]: ")).lower().strip()
    if d == 1 and sexo in "Mm":
        maior = idade
        nomevelho=nome
    else:
        if sexo in "Mm" and idade > maior:
            maior = idade
            nomevelho=nome
    if sexo in "Ff" and idade<20:
        cont_mulher += 1
print(f"A média de idade do grupo é de {media}.")
print(f"O homem mais velho do grupo é {nomevelho} tem {maior} anos.")
print(f"Ao todo são {cont_mulher} mulheres com menos de 20 anos.")