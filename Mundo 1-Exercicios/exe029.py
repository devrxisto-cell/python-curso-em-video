velocidade = int(input('Digite a velocidade do seu carro atual :'))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Voce foi multado! ')
    print('Sua multa é de R$ {:.2f}'.format(multa))

else:
    print('Tudo certo! Dirija com cuidado!')