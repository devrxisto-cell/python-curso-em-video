salario = float(input('Qual é o seu sálario?R$ '))
if salario > 1250:
    novo_salario = salario + (salario * 0.10)
else:
    novo_salario = salario + (salario * 0.15)

print('Quem ganhava {:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novo_salario))
