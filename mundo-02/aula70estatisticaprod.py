print("-"*25)
print("LOJA SUPER BARATÃO")
print("-"*25)
menor=cont=total=maior1000=0
menor_prod=""
while True:
    prod=str(input("Nome do produto: "))
    preco=float(input("Preço do produto: "))
    cont+=1
    total+=preco
    if preco>1000:
        maior1000+=1
    if cont==1 or preco<menor:
        menor=preco
        menor_prod=prod
    continuar=str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if continuar not in "SN":
        print("Opção inválida. Tente novamente.")
    if continuar=="N":
        break
print("-"*10, "FIM DO PROGRAMA", "-"*10)
print(f"O total da compra foi de R${total:.2f}.")
print(f"Temos {maior1000} produtos custando mais de R$1000,00.")
print(f"O produto mais barato foi {menor_prod} que custa R${menor:.2f}.")