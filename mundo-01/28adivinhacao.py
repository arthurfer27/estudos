import random
from time import sleep

print("Vou pensar em um número entre 0 e 5. Tente adivinhar")

print("-="*30)

chute = int(input("Em que número eu pensei? "))
num = random.randint(0, 5)

print("PROCESSANDO...")
sleep (1)

if chute == num:
    print(f"Parabéns você acertou! O número escolhido foi o {num}")
else:
    print(f"Não foi dessa vez! O número escolhido foi {num}")
