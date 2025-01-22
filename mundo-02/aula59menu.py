import time
v1 = int(input("Primeiro valor: "))
v2 = int(input("Segundo valor: "))
opcao = ""
maior = 0
while opcao != 5:
    print("=-="*10)
    print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
    opcao = int(input(("Qual é a sua opção? ")))
    if opcao == 1:
        print(f"A soma entre {v1} e {v2} é de {v1+v2}.")
    elif opcao == 2:
        print(f"A multiplicação entre {v1} e {v2} é {v1*v2}.")
    elif opcao == 3:
        if v1 > v2:
            maior=v1
            print(f"O maior número entre os escolhidos é {maior}.")
        elif v2 > v1:
            maior=v2
            print(f"O maior número entre os escolhidos é {maior}.")
        else:
            print("Os números escolhidos são iguais.")
    elif opcao == 4:
        v1 = int(input("Digite um novo valor para o primeiro número: "))
        v2 = int(input("Digite um novo valor para o segundo número: "))
    elif opcao == 5:
        print("Finalizando...")
        print("=-="*10)
        time.sleep(0.5)
    else:
        print("Opção inválida. Tente novamente.")
print("Fim do programa! Volte sempre!")