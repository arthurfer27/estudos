vel = int(input("Qual é a sua velocidade? "))

if vel > 80:
    print(f"Você foi multado!!! Você excedeu o limite permitido que é de 80km/h. Você deverá pagar uma multa de R${(vel - 80)*7}.")
elif vel <= 80:
    print(f"Tenha um bom dia, dirija com segurança!")