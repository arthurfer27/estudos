print("Gerador de PA")
print("=-="*10)
prim = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
c = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while c <= total:
        print(f"{prim}", end=" -> ")
        prim += razao
        c += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar mais? "))
print("FIM")
print(f"Progressão finalizada com {total} termos mostrados.")