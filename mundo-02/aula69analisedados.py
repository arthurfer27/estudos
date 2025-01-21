maior=homens=mulheres_menos20=0
while True:
    print("-"*20)
    print("CADASTRE UMA PESSOA")
    print("-"*20)
    idade=int(input("Idade: "))
    while idade<0:
        print("Idade inválida. Tente novamente.")
        idade=int(input("Idade: "))
    if idade>18:
        maior+=1
    sexo=str(input("Sexo [M/F]: ")).strip().upper()[0]
    while sexo not in "MF":
        print("Opção inválida. Tente novamente.")
        sexo=str(input("Sexo [M/F]: ")).strip().upper()[0]
    if sexo=="M":
        homens+=1
    if sexo=="F" and idade<20:
        mulheres_menos20+=1
    continuar=str(input("Quer continuar? ")).strip().upper()[0]
    while continuar not in "SN":
        print("Opção inválida. Tente novamente.")
        continuar=str(input("Quer continuar? ")).strip().upper()[0]
    if continuar == "N":
        break
print(f"Total de pessoas com mais de 18 anos: {maior}.")
print(f"Ao todo temos {homens} homem(ns) cadastrado(s).")
print(f"E temos {mulheres_menos20} mulher(es) com menos de 20 anos.")