valor_prod = float(input("Digite o valor do produto: R$"))
print('''FORMAS DE PAGAMENTO
      [1] à vista dinheiro/cheque
      [2] à vista cartão
      [3] 2x no cartão
      [4] 3x ou mais no cartão ''')

opcao = int(input("Digite uma opção de pagamento: "))

if opcao == 1:
    total = valor_prod * 0.9
elif opcao == 2:
    total = valor_prod * 0.95
elif opcao == 3:
    total = valor_prod
    parcela = total / 2
    print(f"Sua compra será parcelada em 2x de R${parcela} SEM JUROS.")
elif opcao == 4:
    total = valor_prod * 1.2
    qnt_parcelas = int(input("Digite o número de parcelas: "))
    parcela = valor_prod/qnt_parcelas
    print(f"Sua compra será parcelada em {qnt_parcelas}x de {parcela} COM JUROS.")

print(f"Sua compra de R${valor_prod} vai custar R${total} no final")