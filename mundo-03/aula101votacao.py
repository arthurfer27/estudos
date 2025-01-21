def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f"Com {idade} anos: NÃO VOTA."
    elif idade>= 16 and idade <65:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO."
    elif idade<16 or idade>65:
        return f"Com {idade} anos: VOTO OPCIONAL."


print(voto(1998))