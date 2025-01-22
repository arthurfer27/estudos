cont = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove","dez")
while True:
    num = int(input("Digite um número entre 0 e 10: "))
    if 0<=num<=10:
       break
    print("Número inválido! Tente novamente.")
print(f"Você escolheu o número {cont[num]}.")