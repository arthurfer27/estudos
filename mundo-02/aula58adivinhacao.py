import random
print("Sou seu computador...")
print("Acabei de pensar em um número de 0 a 10.")
print("Será que você consegue adivinhar qual foi?")
computador = random.randint(0, 10)
chute = int(input("Qual é o seu palpite? "))
cont = 1
while chute != computador:
    if chute < computador:
        print("Mais...Tente mais uma vez.")
    elif chute > computador:
        print("Menos...Tente mais uma vez.")    
    cont += 1
    chute = int(input("Qual é o seu palpite? "))
print(f"Acertou com {cont} tentativas. Parabéns!")