import random
import time

itens = ("Pedra", "Papel", "Tesoura")
computador = random.randint(0,2)
print('''Escolha sua opção:
    [0] PEDRA
    [1] PAPEL
    [2] TESOURA ''')
jogada = int(input("Qual é a sua jogada? "))

print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO')
time.sleep(0.5)
print("=-="*11)
print(f"Computador jogou {itens[computador]}")
print(f"Jogador jogou {itens[jogada]}")
print("=-="*11)

if jogada==0 and computador==1 or jogada==1 and computador==2 or jogada==2 and computador==0:
    print("COMPUTADOR VENCE!")
elif jogada==0 and computador==2 or jogada==1 and computador==0 or jogada==2 and computador==1:
    print("JOGADOR VENCE")
elif jogada==computador:
    print("EMPATE") 