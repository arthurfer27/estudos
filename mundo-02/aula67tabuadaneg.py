while True:
    tabuada = int(input("Quer ver a tabuada de qual valor? "))
    if tabuada<0:
        break
    for t in range(1,11):
        print(f"{tabuada} x {t} = {tabuada*t}")
print("PROGRAMA TABUADA ENCERRADO. Volte sempre!")