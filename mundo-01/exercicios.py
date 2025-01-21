cigarros = float(input("Digite quantos cigarros fumados por dia: "))
anos = float(input("Digite a quantidade de anos que você fumou: "))


minutos_perdidos = cigarros * 10 * 365 * anos

dias_perdidos = minutos_perdidos/1440

print(f"Já foram perdidos {dias_perdidos:.3n} dias de vida por causa do cigarro")