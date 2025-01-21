def dobro(preco=0, format=False):
    res = preco * 2
    return res if format is False else moeda(res)


def metade(preco=0, format=False):
    res = preco / 2
    return res if format is False else moeda(res)


def aumento(preco=0, taxa=0, format=False):
    res = preco + (preco*taxa/100)
    return res if format is False else moeda(res)


def diminuir(preco=0, taxa=0, format=False):
    res = preco - (preco*taxa/100)
    return res if format is False else moeda(res)


def moeda(preco=0, moeda="R$"):
    return f"{moeda}{preco:.2f}".replace(".", ",")


def resumo(preco=0, taxaa=10, taxar=5):
    print("-"*30)
    print("RESUMO DO VALOR".center(30))
    print("-"*30)
    print(f"Preço analisado: \t{moeda(preco)}")
    print(f"Dobro do preço: \t{dobro(preco, True)}")
    print(f"Metade do preço: \t{metade(preco, True)}")
    print(f"{taxaa}% de aumento: \t{aumento(preco, taxaa, True)}")
    print(f"{taxar}% de redução: \t\t{diminuir(preco, taxar, True)}")

def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = input(msg).strip().replace(",", ".")
        if entrada.isalpha() or entrada == "":
            print(f"ERRO! \"{entrada}\" é um preço inválido.")
        else:
            valido=True
            return float(entrada)