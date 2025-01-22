n1 = float(input("Digite a primeira nota do aluno: "))
n2 = float(input("Digite a segunda nota do aluno: "))
media = (n1+n2)/2

if media<5:
    print(f"A média das notas do aluno foi {media}, portanto, está REPROVADO!")
elif media > 5 and media < 6.9:
    print(f"A média das notas do aluno foi {media}, portanto, está de RECUPERAÇÃO!")
elif media >=7 and media<= 10:
    print(f"A média das notas do aluno foi {media}, portanto, está APROVADO!")
else:
    print("Notas inválidas!")