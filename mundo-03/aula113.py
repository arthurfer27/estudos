def leiaInt(msg):
    while True:
        try:
            n=int(input(msg))
        except (ValueError, TypeError):
            print("ERRO! Por favor digite um número válido")
            continue
        except (KeyboardInterrupt):
            print("O usuário preferiu não digitar esse número.")
            return 0
        else:
            return n

def leiaReal(msg):
    while True:
        try:
            n=float(input("Digite um valor real: "))
        except (ValueError, TypeError):
            print("ERRO. Por favor digite um número real válido.")
            continue
        except (KeyboardInterrupt):
            print("O usuário preferiu não digitar esse número.")
            return 0
        else:
            return n

num=leiaInt("Digite um valor inteiro: ")
real=leiaReal("Digite um número real: ")
print(f"O número inteiro digitado foi {num} e o número real foi {real}.")