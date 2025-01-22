print("="*10)
print("10 TERMOS DE UMA PA")
print("="*10)

pri_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
decimo = pri_termo+(11-1) * razao

for c in range(pri_termo, decimo, razao):
    print(c, end="->")
print("ACABOU!")
