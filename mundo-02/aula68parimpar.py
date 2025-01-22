import random
print("=-="*30)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("=-="*30)
computador = random.randint(0,20)
total=cont=0
while True:
    jogador=int(input("Diga um valor: "))
    opcao = str(input("Par ou ímpar? [P/I]")).strip().upper()[0]
    while opcao not in "PI":
        print("Opção inválida! Tente novamente.")
        opcao = str(input("Par ou ímpar? [P/I]")).strip().upper()[0]
    total = jogador+computador
    if total%2==0:
        opcao2="PAR"
    elif total%2==1:
        opcao2="ÍMPAR"
    print("-"*30)
    print(f"Você jogou {jogador} e o computador {computador}. Total de {total} deu {opcao2}")
    if opcao=="P" and opcao2=="PAR" or opcao=="I" and opcao2=="ÍMPAR":
        print("Você venceu!")
    else:
        print(f"GAME OVER! Você venceu {cont} vezes.")
        break
    cont+=1
    print("Vamos jogar novamente...\n")