def leiaInt(msg):
    while True:
        n=input(msg)
        if n.isnumeric():
            return int(n)
        else: 
            print("ERRO! Digite um número inteiro válido.")

a = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {a}.")