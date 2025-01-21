
def area(larg, comp):
    a = larg * comp
    print(f"A área de um terreno {larg}x{comp} é de {a}m²")


print("Controle de Terrenos")
print("-"*15)
l = int(input("Largura (m): "))
c = int(input("Comprimento (m): "))
area( l, c)