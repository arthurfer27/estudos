import datetime
atual = datetime.date.today().year
nasc = int(input("Digite o ano de nascimento do atleta: "))
idade = atual - nasc

if idade <= 9:
    print(f"O atleta tem {idade} anos. Ele é da categoria MIRIM.")
elif idade <=14:
    print(f"O atleta tem {idade} anos. Ele é da categoria INFANTIL.")
elif idade <= 19:
    print(f"O atleta tem {idade} anos. Ele é da categoria JUNIOR.")
elif idade <= 25:
    print(f"O atleta tem {idade} anos. Ele é da categoria SÊNIOR.")
else:
    print(f"O atleta tem {idade} anos. Ele é da categoria MASTER.")