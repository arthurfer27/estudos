import datetime

atual = datetime.date.today().year
nascimento = int(input("Digite o ano de nascimento: "))
idade = atual - nascimento

if idade > 18:
    tempo_alistamento = idade - 18
    print(f"Quem nasceu em {nascimento} tem {idade} em {atual}.")
    print(f"Você já deveria ter se alistado há {atual-(nascimento+18)} anos.")
    print(f"Seu alistamento foi em {atual-tempo_alistamento}.")
elif idade< 18:
    tempo_alistamento = 18 - idade
    print(f'''Quem nasceu em {nascimento} terá {idade} em {atual}.
          Ainda faltam {tempo_alistamento} anos para o alistamento
          Seu alistamento será em {atual+tempo_alistamento} ''')
else:
    print(f"Quem nasceu em {nascimento} tem {idade} anos em {atual}.")
    print("Você tem que se alistar IMEDIATAMENTE!")