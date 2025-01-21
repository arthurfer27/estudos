inicio = int(input("Digite o número inicial: "))
fim = int(input("Digite o número final: "))


while True:

    if inicio > fim:
        inicio = inicio - 1 
        print(inicio,"...")
    
        if inicio == fim:
            break
    
    elif fim > inicio:
        inicio = inicio + 1 
        print(inicio,"...")
    
        if inicio == fim:
            break
