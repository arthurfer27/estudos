print("Gerador de PA")
print("=-="*10)
prim=int(input("Primeiro termo: "))
razao=int(input("Razão da PA: "))
c=0
while c!=10:
    print(f"{prim}", end=" -> ")
    prim+=razao
    c+=1
print("FIM")