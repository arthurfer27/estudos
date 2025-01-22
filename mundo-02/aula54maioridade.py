import datetime
ano = datetime.date.today().year
maiores = 0
menores = 0
for i in range(1, 8):
    nasc = int(input(f"Em que ano a {i}ª pessoa nasceu? "))
    if ano - nasc >= 18:
        maiores += 1
    else:
        menores += 1
print(f"Ao todo tivemos {maiores} pessoas maiores de idade.")
print(f"E também tivemos {menores} pessoas menores de idade.")
