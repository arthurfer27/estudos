from random import randint
from time import sleep
num = []

def sorteia(num):
    for c in range(0, 5):
        num.append(randint(1, 10))
    print(f"Sorteando 5 valores da lista: ", end="")
    for c in num:
        print(f"{c} ", end=" ", flush=True)
        sleep(0.2)
    print()

def pares():
    som = 0
    for c in num:
        if c % 2 == 0:
            som += c
    print(f"Somando os valores pares de {num}, temos {som}.")

sorteia(num)
pares()