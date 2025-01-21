lar = float(input("Qual é a largura da parede? "))
alt = float(input("Qual é a altura da parede? "))

print(f"Sua parede tem a dimensão de {lar}x{alt} e sua área é de {lar*alt}m²")
print(f"Para pintar sua parede, você precisará de {(lar*alt)/2:.2f}l de tinta")