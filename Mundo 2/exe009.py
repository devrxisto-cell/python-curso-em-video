print("==========LOJA XISTO===========")
compra = float(input("Digite o valor da compra R$: "))

print(""" 
Formas de pagamento:
[1] Á vista no dinheiro ou cheque (10% de desconto)
[2] Á vista no cartão (5% de desconto)
[3] 2x no cartão (preço normal)
[4] 3x ou mais no cartão (20% de juros)
""")

opcao = int(input("Escolha uma forma de pagamento: "))

if opcao == 1:
    total = compra - (compra * 0.10)
    print(f"Você recebeu 10% de desconto. Valor final: R$ {total:.2f}")
elif opcao == 2:
    total = compra - (compra * 0.05)
    print(f"Você recebeu 5% de desconto. Valor final: R$ {total:.2f}")
elif opcao == 3:
    total = compra
    parcela = total / 2
    print(f"Sua compra será parcelada em 2x de R$ {parcela:.2f} SEM JUROS.")
    print(f"Valor final: R$ {total:.2f}")
elif opcao == 4:
    parcelas = int(input("Escolha em quantas vezes pagar? "))
    if parcelas < 3:
        print("Números de parcelas inválido! Tem que ser 3 ou mais vezes.")
    else:
        total = compra + (compra * 0.20)
        parcela = total / parcelas
        print(f"Sua compra será parcelada em {parcelas}x de R$ {parcela:.2f} COM JUROS!")
        print(f"Valor final: R$ {total:.2f}")
else:
    print("Opção inválida! Tente novamente.")

