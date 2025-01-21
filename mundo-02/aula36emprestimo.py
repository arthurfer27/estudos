valor_casa = float(input("Qual é o valor da casa: R$"))
salario = float(input("Qual é o seu salário: R$"))
anos_pagamento = int(input("Em quantos anos você vai pagar a casa? "))

prestacoes = anos_pagamento*12
valor_pretacao = valor_casa / prestacoes

if valor_pretacao <= (salario*0.3):
    print(f"Ok! Seu empréstimo está aprovado. As prestações serão de R${valor_pretacao:.2f}")
else:
    print(f"Para pagar uma casa de R${valor_casa} em {anos_pagamento} anos a prestação será de R${valor_pretacao:.2f}, eu ganho R${salario}\n" "Empréstimo Negado!")
