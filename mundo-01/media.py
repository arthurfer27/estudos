nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2)/2

if (media <= 10) and (media >= 9):
    print(f"Média: {media}")
    print("Aproveitamento A!")
elif (media < 9) and (media >= 8):
    print(f"Média: {media}")
    print("Aproveitamento B!")
elif (media < 8) and (media >= 7):
    print(f"Média: {media}")
    print("Aproveitamento C!")
elif (media < 7) and (media >= 6):
    print(f"Média: {media}")
    print("Aproveitamento D!")
else:
    print(f"Média: {media}")
    print("Aproveitamento E!")