import moeda

preco = int(input("Digite o preço: "))

print(f"A metade de {preco} é {(moeda.metade(preco))}")
print(f"O dobro de {preco} é {moeda.dobro(preco)}")
print(f"Aumentando em 10%, temos {moeda.aumento(preco, 10)}")
print(f"Diminuindo 20%, temos {moeda.diminuir(preco, 20)}")